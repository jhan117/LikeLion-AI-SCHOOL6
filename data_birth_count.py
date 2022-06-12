import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


# 한글 에러 안 나게 넣어주기
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


# style 설정은 꼭 폰트설정 위에서 합니다.
# style 에 폰트 설정이 들어있으면 한글폰트가 초기화 되어 한글이 깨집니다.
plt.style.use('dark_background')
# 폰트설정
plt.rc("font", family=get_font_family())
# 마이너스폰트 설정
plt.rc("axes", unicode_minus=False)

# 데이터 불러오기
df = pd.read_csv("data/birth_count_2008-2022.csv")
df_f = pd.read_csv("data/fertility_rate_2008-2022.csv")

#####
# 출생자 수 데이터 전처리
df_m = df.melt(id_vars="행정구역(시군구)별", value_vars=df.columns)
df_m.columns = ["행정구역별", "연도", "출생자수"]
df_m = df_m.sort_values(by=["행정구역별", "연도"]).reset_index(drop=True)

# # 행정구역&연도별 출생자수, 출생자수 변화율 (df_p로 설정)
df_p = df_m.set_index("행정구역별")
df_p["연도"] = df_p["연도"].str.strip(" 년").astype(int)
df_p["출생자수_변화율"] = df_p["출생자수"].groupby("행정구역별").pct_change() * 100
df_p = df_p.reset_index()

# 전국 출생자수, 출생자수 변화율 (df_all로 설정)
df_all = df_p[df_p["행정구역별"] == "전국"]
df_all = df_all.drop(df_all.index[-1])
#####

#####
# 전국 출산율 (df_all_f)
df_all_f = df_f[df_f["행정구역별"] == "전국"].reset_index(drop=True)
######
# 그래프 작업
######

# 그래프를 그리기 위한 x, y에 데이터 지정
x = df_all["연도"]
y1 = df_all_f["출산율"].astype(float)
y2 = df_all["출생자수"]

# 출생자수와 출산율 변화 그래프
birth_fig, ax1 = plt.subplots()

plt.title('출생아수와 출산율 변화')
plt.grid(False)

# w = 480 / birth_fig.dpi
h = 320 / birth_fig.dpi
# birth_fig.set_figwidth(w)
birth_fig.set_figheight(h)

ax2 = ax1.twinx()
ax1.bar(x, y2, color='lightblue', width=0.4, label='출생아수(명)')
ax1.set_ylim(150000, 500000)
ax1.set_ylabel('출생아수(명)')

ax2.plot(x, y1, color='red', markersize=7,
         linewidth=5, alpha=0.6, label='출산율(%)')
ax2.set_ylim(0.5, 1.5)
ax2.set_xlabel('연도')
ax2.set_ylabel('출산율(%)')

ax2.set_zorder(10)
ax1.set_zorder(5)
ax2.patch.set_visible(False)

ax2.legend(loc='upper left')
ax1.legend(loc='upper right')

if __name__ == '__main__':
    # plt.show()
    # print(y2)
    pass
