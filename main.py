from data import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Initialize figure with subplots
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type': 'choropleth'}, {'type': 'bar'}]],
    column_widths=[0.6, 0.4])

# 컬럼 값 : [min, max, color_cho, color_bar]
crime_setting = {'범죄발생총건수': [1700, 5850, 'Reds'],
                 '형법범': [1010, 2800, 'Oranges', '#ff7f0e'], '특별법범': [670, 3060, 'Blues', '#1f77b4']}

# Add chart
# trace = [all_cho 0 ~ 6, (criminal_cho, criminal_bar) 7 ~ 20, (special_cho, special_bar) 21 ~ 34]
for key, value in crime_setting.items():
    for year in df_crime['시점'].unique():
        df_segmented = df_crime[(df_crime['시점'] == year)]

        # Add choropleth chart
        fig.add_trace(
            go.Choropleth(
                visible=False,

                # design
                marker_line_color='white',

                # colorbar setting
                colorscale=value[2],
                colorbar_title='인구 10만명당 범죄율',
                colorbar_x=0,
                zmin=value[0],
                zmax=value[1],

                # map setting
                geojson=counties,
                locations=df_segmented['발생지역별'],
                z=df_segmented[key],
                featureidkey="properties.CTP_KOR_NM"),
            # subplot location
            row=1, col=1)

        if key != '범죄발생총건수':
            # Add bar chart
            fig.add_trace(
                go.Bar(
                    visible=False,

                    # design
                    marker=dict(color=value[3]),

                    # bar setting
                    name=key,
                    x=df_segmented['발생지역별'],
                    y=df_segmented[key]
                ),
                # subplot location
                row=1, col=2)

# Make default chart visible
fig.data[0].visible = True  # 2014 전체 choropleth
fig.data[8].visible = True  # 2014 형법범 bar
fig.data[22].visible = True  # 2014 특별법범 bar

# === step ===
steps = {'all': [], 'criminal': [], 'special_law': []}
for i in range(7):  # 7년 자료
    for key in steps.keys():
        true_list = [False] * 35

        if key == 'all':
            # 전체 choropleth, 형법범 bar, 특별범 bar
            true_list[i], true_list[i*2+8], true_list[i*2+22] =\
                True, True, True
        elif key == 'criminal':
            # 형법범 choropleth, 형법범 bar
            true_list[i*2+7], true_list[i*2+8] = True, True
        else:
            # 특별법범 choropleth, 특별법범 bar
            true_list[i*2+21], true_list[i*2+22] = True, True

        steps[key].append(
            dict(method='update', label=f'{2014 + i}년', args=[dict(visible=true_list)]))

# === sliders ===
sliders = {}
for key, step in steps.items():
    slider = [dict(active=0, steps=step)]
    sliders[key] = slider

# === buttons ===
buttons = []
name_list = ['전체', '형법범', '특별법범']
for i, (key, slider) in enumerate(sliders.items()):
    # default visible
    slider_active = slider[0]["active"]
    slider_visible = slider[0]["steps"][slider_active]["args"][0]["visible"]

    buttons.append(dict(label=f'지역별 {name_list[i]} 범죄율',
                        method="update",
                        args=[dict(visible=slider_visible, sliders=slider), dict(sliders=sliders[key])]))

# === update menus ===
updatemenus = [dict(direction='down', active=0, buttons=buttons,
                    x=0.55, y=0.6, xanchor='right', yanchor='top')]

# === annotations ===
annotations = [dict(text="<b>범죄별</b>", x=0.495, xref="paper",
                    y=0.625, yref="paper", showarrow=False)]

# === title ===
title = dict(font_size=32, text='<b>한국 범죄율</b><br>데이터 출처 : KOSIS(국가 통계 포털)',
             x=0.5, y=0.95, xanchor='center', yanchor='middle')

# === default layout ===
fig.update_layout(updatemenus=updatemenus, sliders=sliders['all'], annotations=annotations, title=title,
                  barmode='stack', font_color="black", font_size=14, legend_x=0.65, yaxis_range=[0, 5850])
fig.update_geos(fitbounds="locations", visible=False)

fig.show()
