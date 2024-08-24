import pandas as pd

import json

with open("korea.geojson", encoding='utf-8') as file:
    counties = json.load(file)

# Columns
city_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
             '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']

# (항목표두, 시점표측)로 불러오기
df = pd.read_csv("범죄발생지역(항목표두, 시점표측).csv", encoding='cp949')


# 이거보다 더 나은 건 없나?
def find_location(value):
    """
    지역 이름 변경하기
    """
    for name in city_list:
        if value in name:
            return name
        elif value == '충북':
            return city_list[-7]
        elif value == '충남':
            return city_list[-6]
        elif value == '전북':
            return city_list[-5]
        elif value == '전남':
            return city_list[-4]
        elif value == '경북':
            return city_list[-3]
        elif value == '경남':
            return city_list[-2]


def get_dataframe(keyword):
    """
    원하는 키워드 별로 dataframe 만듦
    """
    # 단어로 가져오기 및 계 제외
    df_return = df.loc[df["범죄별"].str.startswith(keyword)][7:]

    # 빈 값 및 컬럼 삭제
    df_return = df_return.drop(columns=['범죄별'], axis=1).dropna(axis=1)

    # 컬럼 값 변경
    df_return['시점'] = df_return['시점'].str.replace('년', '')
    df_return['발생지역별'] = df_return['발생지역별'].map(find_location)

    # 숫자로 변환
    df_return['시점'] = pd.to_numeric(df_return['시점'])
    df_return['범죄발생지역'] = pd.to_numeric(df_return['범죄발생지역'])

    # 인덱스 설정
    df_return = df_return.set_index(['발생지역별', '시점'])
    return df_return


# class로 하자
# make dataframe list
keyword_list = ['범죄발생총건수', '형법범', '특별법범']
df_population = get_dataframe('인구')
df_list = [get_dataframe(k) for k in keyword_list]

# 인구 10만명 당 범죄율
df_crime_list = [(df_crime / df_population) * 100000 for df_crime in df_list]

# 범죄별 dataframe
df_crime = pd.concat(df_crime_list, axis=1)

# colomns
df_crime.columns = keyword_list

# reset index -> 코드 길어지는 거 방지
df_crime = df_crime.reset_index()
