import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv(
    'data/state_data.csv', encoding='cp949')


# 지역별 학급당 학생수 데이터 불러오는 함수
def cal_cls_per_Sch(df_name, option, st_col, year):
    df_name = df_name[df_name['상태'].isin(['기존(원)교', '신설(원)교'])]
    result_data = df_name[(df_name['연도'] == year) & (df_name['학교급'] == option)].groupby(
        [st_col]).agg({'학급당 학생수': 'mean', '학급수 총계': 'mean'}).reset_index().round(1)
    result_data.rename(columns={'학급수 총계': '평균 학급수'}, inplace=True)
    return(result_data)


# 지역별 학급당 학생수 막대 그래프
def draw_graph1(opt, end_year):
    graph1 = cal_cls_per_Sch(df, opt, '시도', end_year)
    state_fig1 = px.bar(data_frame=graph1, x='시도', y='학급당 학생수', custom_data=[
        '평균 학급수'], color='학급당 학생수', color_continuous_scale='Blues', text="학급당 학생수",
        title=str(end_year)+"년 지역별 학급당 학생수", width=800, height=600)
    state_fig1.update_xaxes(categoryorder='total descending')
    state_fig1.update_traces(marker_line_color='rgb(8,48,107)',
                             marker_line_width=1, opacity=0.6,
                             textfont={'size': 13},
                             texttemplate='%{text}',
                             textposition='outside')

    # 레이블, 배경, hover tooltip 설정 변경
    state_fig1.update_layout(annotations=[dict(
        x=1,
        y=1,  # Trying a negative number makes the caption disappear - I'd like the caption to be below the map
        xref='paper',
        yref='paper',
        text='(단위 : 명)',
        showarrow=False)],
        margin=dict(pad=5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_family="Open Sans"
    ))

    # hover : tooltip 도구설명 수정
    state_fig1.update_traces(
        hovertemplate="<br>".join([
            "지역 : %{x}",
            "학급당 학생수 : %{y}명",
            "학교당 평균 학급수 : %{customdata[0]:,.0f}개"])
    )

    state_fig1.update_xaxes(title='')
    state_fig1.update_layout(coloraxis_showscale=False,
                             yaxis=dict(showgrid=False),
                             modebar_remove=['zoom', 'pan'])
    return(state_fig1)


# 지역별 학급당 학생수 증감율

# 데이터프레임, 기준 컬럼, 시작연도, 끝연도를 넣으면 증감율을 계산해서 만들어주는 함수
def cal_Cls_per_Sch_ratio(df_name, option,  st_col, start_year, end_year):
    df_name = df_name[df_name['학교급'] == option]
    # start/end year 데이터가 없으면 drop
    element = df_name[df_name['연도'] == end_year][st_col].unique()
    mask = np.isin(df_name[df_name['연도'] == end_year][st_col].unique(
    ), df[df['연도'] == start_year][st_col].unique())
    st_col_list = element[mask]

    st_col_mask = df_name[st_col].isin(st_col_list)
    year_mask = df_name['연도'].isin([start_year, end_year])
    df_name_drop = df_name.loc[st_col_mask & year_mask, :]

    # 연도별 폐교, 휴원 제외하고 기존, 신설 학교만 포함.
    cal_df = df_name_drop.loc[df_name_drop['상태'].isin(['기존(원)교', '신설(원)교']), :]\
        .groupby([st_col, '연도']).agg({'학급당 학생수': 'mean', '학급수 총계': 'mean'})\
        .reset_index()

    cal_df['학급당 학생수 증감율'] = round(cal_df.sort_values(
        [st_col, '연도'])['학급당 학생수'].pct_change()*100, 1)

    result_data = cal_df[cal_df['연도'] == end_year].copy()
    result_data.rename(columns={'학급수 총계': '평균 학급수'}, inplace=True)
    return(result_data)


# 학급당 학생수 증감율 그래프
def draw_graph2(opt, start_year, end_year):
    graph2 = cal_Cls_per_Sch_ratio(df, opt, '시도', start_year, end_year)
    state_fig2 = px.bar(data_frame=graph2,
                        x='학급당 학생수 증감율',
                        y='시도',
                        custom_data=['평균 학급수'],
                        color='학급당 학생수 증감율',
                        color_continuous_scale='reds_r',
                        text="학급당 학생수 증감율",
                        title=str(start_year)+"년 대비 " + str(end_year) + "년 지역별 학급당 학생수 증감율")

    state_fig2.update_yaxes(categoryorder='total ascending')
    state_fig2.update_traces(marker_line_color='rgb(8,48,107)',
                             marker_line_width=1, opacity=0.6,
                             textfont={'size': 12},
                             texttemplate='%{text:}%',
                             textposition='outside')

    state_fig2.update_layout(margin=dict(pad=5),
                             paper_bgcolor='rgba(0,0,0,0)',
                             plot_bgcolor='rgba(0,0,0,0)',
                             hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_family="Open Sans"
    ))

    # hover : tooltip 도구설명 수정
    state_fig2.update_traces(
        hovertemplate="<br>".join([
            "지역 : %{y}",
            "학급당 학생수 증감율 : %{x}%",
            "학교당 평균 학급수 : %{customdata[0]:,.0f}개"])
    )

    state_fig2.update_xaxes(autorange="reversed")
    state_fig2.update_yaxes(title='')
    state_fig2.update_layout(coloraxis_showscale=False,
                             xaxis=dict(showgrid=False),
                             modebar_remove=['zoom', 'pan'])

    return(state_fig2)


# 지역별 교원당 학생수
# 지역별 교원 수 + 학생 수
def cal_Stu_per_Tch(df_name, option, st_col, year):
    result_data = df_name[(df_name['연도'] == year) & (df_name['학교급'] == option)].groupby(
        [st_col]).agg({'교원수 총계': 'sum', '학생수 총계': 'sum'}).reset_index()
    result_data['교원당 학생수'] = round(
        result_data['학생수 총계']/result_data['교원수 총계'], 2)
    return(result_data)


def draw_graph3(opt, end_year):
    graph3 = cal_Stu_per_Tch(df, opt, '시도', end_year)
    state_fig3 = px.bar(data_frame=graph3, x='시도', y='교원당 학생수',
                        custom_data=['교원수 총계', '학생수 총계'],
                        color='교원당 학생수',
                        color_continuous_scale='Blues',
                        text="교원당 학생수",
                        title=str(end_year)+"년 지역별 교원당 학생수",
                        width=800,
                        height=600)
    state_fig3.update_xaxes(categoryorder='total descending')
    state_fig3.update_traces(marker_line_color='rgb(8,48,107)',
                             marker_line_width=1, opacity=0.6,
                             textfont={'size': 13},
                             texttemplate='%{text}',
                             textposition='outside')

    # 레이블, 배경, hover tooltip 설정 변경
    state_fig3.update_layout(annotations=[dict(

        x=1,
        y=1,  # Trying a negative number makes the caption disappear - I'd like the caption to be below the map
        xref='paper',
        yref='paper',
        text='(단위 : 명)',
        showarrow=False)],
        margin=dict(pad=5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_family="Open Sans"
    ))

    # hover : tooltip 도구설명 수정
    state_fig3.update_traces(
        hovertemplate="<br>".join([
            "지역 : %{x}",
            "교원당 학생수 : %{y}명",
            "교원수 총계 : %{customdata[0]:,.0f}개",
            "학생수 총계 : %{customdata[1]:,.0f}명"])
    )

    state_fig3.update_xaxes(title='')
    state_fig3.update_layout(coloraxis_showscale=False,
                             yaxis=dict(showgrid=False),
                             modebar_remove=['zoom', 'pan'])
    return(state_fig3)


# 지역별 교원당 학생수 증감율
# 데이터프레임, 기준 컬럼, 시작연도, 끝연도를 넣으면 증감율을 계산해서 만들어주는 함수
def cal_Stu_per_Tch_ratio(df_name, option, st_col, start_year, end_year):
    df_name = df_name[df_name['학교급'] == option]
    # start/end year 데이터가 없으면 drop
    element = df_name[df_name['연도'] == end_year][st_col].unique()
    mask = np.isin(df_name[df_name['연도'] == end_year][st_col].unique(
    ), df[df['연도'] == start_year][st_col].unique())
    st_col_list = element[mask]

    st_col_mask = df_name[st_col].isin(st_col_list)
    year_mask = df_name['연도'].isin([start_year, end_year])
    df_name_drop = df_name.loc[st_col_mask & year_mask, :]

    # 연도별 폐교, 휴원 제외하고 기존, 신설 학교만 포함.
    cal_df = df_name_drop.loc[df_name['상태'].isin(['기존(원)교', '신설(원)교']), :]\
        .groupby([st_col, '연도']).agg({'교원수 총계': 'sum', '학생수 총계': 'sum'})\
        .reset_index()

    cal_df['교원당 학생수'] = cal_df['학생수 총계']/cal_df['교원수 총계']

    cal_df['교원당 학생수 증감율'] = round(cal_df.sort_values(
        [st_col, '연도'])['교원당 학생수'].pct_change()*100, 2)

    result_data = cal_df[cal_df['연도'] == end_year].copy()

    return(result_data)


def draw_graph4(opt, start_year, end_year):
    graph4 = cal_Stu_per_Tch_ratio(df, opt, '시도', start_year, end_year)
    state_fig4 = px.bar(data_frame=graph4, y='시도', x='교원당 학생수 증감율', custom_data=[
        '교원수 총계', '학생수 총계'], color='교원당 학생수 증감율', color_continuous_scale='reds_r', text="교원당 학생수 증감율", title=str(start_year)+"년 대비 " + str(end_year) + "년 지역별 교원당 학생수 증감율")

    state_fig4.update_yaxes(categoryorder='total ascending')
    state_fig4.update_traces(marker_line_color='rgb(8,48,107)',
                             marker_line_width=1, opacity=0.6,
                             textfont={'size': 10},
                             texttemplate='%{text:}%',
                             textposition='outside')

    state_fig4.update_layout(margin=dict(pad=5),
                             paper_bgcolor='rgba(0,0,0,0)',
                             plot_bgcolor='rgba(0,0,0,0)',
                             hoverlabel=dict(
        bgcolor="white",
        font_size=11,
        font_family="Open Sans"
    ))

    # hover : tooltip 도구설명 수정
    state_fig4.update_traces(
        hovertemplate="<br>".join([
            "지역 : %{y}",
            "교원당 학생수 증감율 : %{x}%",
            "교원수 총계 : %{customdata[0]:,.0f}개",
            "학생수 총계 : %{customdata[1]:,.0f}명"])
    )
    state_fig4.update_xaxes(autorange="reversed")
    state_fig4.update_yaxes(title='')
    state_fig4.update_layout(coloraxis_showscale=False,
                             xaxis=dict(showgrid=False),
                             modebar_remove=['zoom', 'pan'])

    return(state_fig4)
