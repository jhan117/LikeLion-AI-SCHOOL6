import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


# 한글폰트 설정
def get_font_family():
    """
    시스템 환경에 따른 기본 폰트명을 반환하는 함수
    """
    import platform
    system_name = platform.system()

    if system_name == "Darwin":
        font_family = "AppleGothic"
    else:
        font_family = "Malgun Gothic"
    return font_family


plt.style.use('dark_background')
plt.rc("font", family=get_font_family())
plt.rc("axes", unicode_minus=False)


# 초등학교 데이터 불러오기
file_name = "data/schl_data.csv"
df = pd.read_csv(file_name)
df_elementary = df.loc[(df["학교급"] == "초등학교") & (df["상태"] != '폐(원)교')]

# groupby를 통해 시각화할 데이터 전처리 (학교수, 학생수, 교원수)
df_elementary_schl = df_elementary.groupby(
    ["연도"]).count()[["학교코드"]].reset_index()
df_elementary_stdt = df_elementary.groupby(
    ["연도"]).sum()[["학생수 총계"]].reset_index()
df_elementary_tchr = df_elementary.groupby(
    ["연도"]).sum()[["교원수 총계"]].reset_index()

# 그래프를 그리기 위한 x, y에 데이터 지정
x = df_elementary_schl["연도"]
y1 = df_elementary_stdt["학생수 총계"]
y2 = df_elementary_schl["학교코드"]
y3 = round(y1/y2, 1)
y4 = df_elementary_tchr["교원수 총계"]
y5 = round(y1/y4, 1)

# 학교수 학생수 변화 (fig_ele1)
fig_ele1, ax1_ele1 = plt.subplots()

plt.title('[초등학교] 10년간 학교수와 학생수 변화')
plt.grid(False)

ax1_ele1.plot(x, y2, '-s', color='red', markersize=7,
              linewidth=5, alpha=0.6, label='학교수')
ax1_ele1.set_ylim(6000, 6500)
ax1_ele1.set_xlabel('연도')
ax1_ele1.set_ylabel('학교수(개)')

ax2_ele1 = ax1_ele1.twinx()
ax2_ele1.bar(x, y1/10000, color='lightblue', width=0.4, label='학생수')
ax2_ele1.set_ylim(250, 300)
ax2_ele1.set_ylabel('학생수(만명)')

ax1_ele1.set_zorder(10)
ax2_ele1.set_zorder(5)
ax1_ele1.patch.set_visible(False)

ax1_ele1.legend(loc='upper left')
ax2_ele1.legend(loc='upper right')


# 학교당 학생수 변화(fig_ele2)
fig_ele2, ax1_ele2 = plt.subplots()

plt.title('[초등학교] 10년간 학교당 학생수 변화')

ax1_ele2.plot(x, y3, '-s', color='teal', markersize=7,
              linewidth=5, alpha=0.7, label=' 학교당 학생수(명)')
ax1_ele2.set_xlabel('연도')
ax1_ele2.legend()

# 10년간 교원수와 학생수 그래프 (fig_ele3)
fig_ele3, ax1_ele3 = plt.subplots()

plt.title('[초등학교] 10년간 교원수와 학생수 변화', fontsize=15)
plt.grid(False)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

ax1_ele3.plot(x, y4/10000, '-s', color='red', markersize=7,
              linewidth=5, alpha=0.7, label='교원수')
ax1_ele3.set_ylim(18, 20)
ax1_ele3.set_xlabel('연도', fontsize=12, labelpad=10)
ax1_ele3.set_ylabel('교원수(만명)', fontsize=12, labelpad=10)

ax2_ele3 = ax1_ele3.twinx()
ax2_ele3.bar(x, y1/10000, color='lightblue', width=0.4, label='학생수')
ax2_ele3.set_ylim(250, 300)
ax2_ele3.set_ylabel('학생수(만명)', fontsize=12, labelpad=10)
plt.yticks(fontsize=10)

ax1_ele3.set_zorder(10)
ax2_ele3.set_zorder(5)
ax1_ele3.patch.set_visible(False)

ax1_ele3.legend(loc='upper left')
ax2_ele3.legend(loc='upper right')

# 교원당 학생수 변화 그래프 (fig_ele4)
fig_ele4, ax1_ele4 = plt.subplots()

plt.title('[초등학교] 10년간 교원당 학생수 변화')

ax1_ele4.plot(x, y5, '-s', color='teal', markersize=7,
              linewidth=5, alpha=0.7, label=' 교원당 학생수(명)')
ax1_ele4.set_xlabel('연도')
ax1_ele4.legend()


# 현재 초등학교수 및 전년비 증감
cur_ele_sch = f'{y2[9]:,}개'
vol_ele_sch = (y2.pct_change() * 100)
vol_ele_sch = f'{vol_ele_sch[9]:.2f}%'

# 현재 초등학생수 및 전년비 증감
cur_ele_stu = f'{y1[9]/10000:,.1f}만명'
vol_ele_stu = (y1.pct_change() * 100)
vol_ele_stu = f'{vol_ele_stu[9]:.2f}%'

# 학교대비 학생수
cur_ele_stu_sch = f'{y1[9]/y2[9]:,.1f}명'
vol_ele_stu_sch = ((y1/y2).pct_change() * 100)
vol_ele_stu_sch = f'{vol_ele_stu_sch[9]:.2f}%'


# 현재 교원수 및 전년비 증감
cur_ele_teach = f'{y4[9]/10000:,.1f}만명'
vol_ele_teach = (y4.pct_change() * 100)
vol_ele_teach = f'{vol_ele_teach[9]:.2f}%'

# 교원대비 학생수
cur_ele_stu_teach = f'{y1[9]/y4[9]:,.1f}명'
vol_ele_stu_teach = ((y1/y4).pct_change() * 100)
vol_ele_stu_teach = f'{vol_ele_stu_teach[9]:.2f}%'
