import pandas as pd
from tqdm import trange


def check_header(year):
    if year in range(2012, 2020):
        return 11
    elif year == 2020:
        return 13
    else:
        return 14


def save_parquet():
    df_list = []
    select_cols = ['조사기준일', '시도', '학교급', '나이스 학교 코드',
                   '학생수_총계_계', '교원수_총계_계']
    cols = ['연도', '시도', '학교급', '나이스 학교 코드', '학생수 총계', '교원수 총계']

    try:
        for i in trange(2012, 2022):
            file_path = f'data/{i}년'

            # read
            df = pd.read_excel(f'{file_path}.xlsx',
                               header=check_header(i), engine='openpyxl')

            # select values
            df = df.loc[df['학교급'] == '유치원']
            df = df.loc[df['상태'] != '폐(원)교']

            # select columns
            df = df.loc[:, select_cols]
            df.columns = cols

            df_list.append(df)

        # concatenate
        concatenated_df = pd.concat(df_list)

        # save
        concatenated_df.to_parquet(f'data/data.parquet.gzip',
                                   compression='gzip', index=False)
    except:
        raise Exception(f'{i}년 에러 발생')


def processing(df):
    # int -> stirng -> int
    df['연도'] = df['연도'].astype("string").str[:4].astype("int")

    # downcast
    for col in df.columns:
        dtype_name = df[col].dtypes.name
        if dtype_name.startswith('int'):
            df[col] = pd.to_numeric(df[col], downcast='unsigned')
        elif dtype_name.startswith('float'):
            df[col] = pd.to_numeric(df[col], downcast='float')

    return df


# read
# df = pd.read_parquet('data/data.parquet.gzip')

# processing
# df = processing(df)

# save
# df.to_parquet(f'data/dataframe.parquet.gzip', compression='gzip', index=False)

# read
df = pd.read_parquet('data/dataframe.parquet.gzip')

# 연도별 학교수
df_sch = df.groupby(['연도'])['나이스 학교 코드'].count().reset_index()
# 연도별 학생수
df_stu = df.groupby(['연도'])['학생수 총계'].sum().reset_index()
df_stu['학생수 총계(만명)'] = df_stu['학생수 총계'] / 10000
# 연도별 교원수
df_teach = df.groupby(['연도'])['교원수 총계'].sum().reset_index()
df_teach['교원수 총계(천명)'] = df_teach['교원수 총계'] / 1000

# 연도별 학교/학생수 (파생변수)
df_sch_stu = df_sch.merge(df_stu)
df_sch_stu['학교당 학생수'] = df_sch_stu['학생수 총계'] / df_sch_stu['나이스 학교 코드']

# 연도별 교원1인당 학생수
df_teach_stu = df_teach.merge(df_stu)
df_teach_stu['교원1인당 학생수'] = df_teach_stu['학생수 총계'] / df_teach_stu['교원수 총계']

# 현재 및 변동 유치원수
current_sch = f'{df_sch.iloc[-1, -1]}개'
vol_sch = (df_sch.pct_change() * 100).iloc[-1, -1]
vol_sch = f'{vol_sch:.2f}%'

# 현재 및 변동 원아수
current_stu = f'{df_stu.iloc[-1, -1]:.2f}만명'
vol_stu = (df_stu.pct_change() * 100).iloc[-1, -1]
vol_stu = f'{vol_stu:.2f}%'

# 현재 및 변동 교원수
current_teach = f'{df_teach.iloc[-1, -1]:.2f}천명'
vol_teach = (df_teach.pct_change() * 100).iloc[-1, -1]
vol_teach = f'{vol_teach:.2f}%'

# 현재 및 변동 유치원당 원아수
current_sch_stu = f'{df_sch_stu.iloc[-1, -1]:.2f}명'
vol_sch_stu = (df_sch_stu.pct_change() * 100).iloc[-1, -1]
vol_sch_stu = f'{vol_sch_stu:.2f}%'

# 현재 및 변동 교원 1인당 원아수
current_teach_stu = f'{df_teach_stu.iloc[-1, -1]:.2f}명'
vol_teach_stu = (df_teach_stu.pct_change() * 100).iloc[-1, -1]
vol_teach_stu = f'{vol_teach_stu:.2f}%'

if __name__ == '__main__':
    # print(df.info())
    # print(df.head())
    # save_parquet()
    print(df_teach_stu)
    pass
