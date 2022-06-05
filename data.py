import requests
import pandas as pd
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import json

tier_list = ['all', 'challenger', 'grandmaster', 'master',
             'diamond',  'platinum', 'gold', 'silver', 'bronze', 'iron']

stats_name = ['win_rate', 'pick_rate', 'ban_rate']


# 데이터 수집
def get_data(tier):
    try:
        time.sleep(1)
        url = 'https://www.op.gg/_next/data/jJBmp4Iu3tyDIZFxaXguO/champions.json?region=kr'
        response = requests.get(url, headers={'User-agent': 'Mozilla/5,0'},
                                params={'tier': tier, 'patch': '12.10'})
        data = response.json()['pageProps']['championMetaList']
        return data
    except:
        raise Exception(response.status_code)


# 데이터 저장하기
def save_json():
    for tier in tqdm(tier_list):
        data = get_data(tier)

        data_path = f'data/12.10_{tier}_data.json'
        with open(data_path, 'w') as f:
            json.dump(data, f)


# save_json()


# 데이터프레임 만들기
def make_dataframe():
    df_list = []
    for tier in tqdm(tier_list):
        file_name = f'12.10_{tier}_'

        data_path = f'data/{file_name}data.json'
        with open(data_path) as f:
            data = json.load(f)

        # make dict
        data_dict = {}
        for d in tqdm(data):
            champion = d['name']
            for p in d['positions']:
                stats_list = []
                position = p['name']
                for n in stats_name:
                    stats_list.append(p['stats'][n] * 100)
                data_dict[(champion, position)] = stats_list

        # make df
        df = pd.DataFrame(data_dict).T.reset_index()
        df.columns = ['champion', 'position',
                      'win_rate', 'pick_rate', 'ban_rate']
        df.insert(loc=0, column='tier', value=tier)
        df_list.append(df)
    df = pd.concat(df_list)
    # save df
    df.to_csv('dataframe.csv', index=False)


# make_dataframe()

df = pd.read_csv('dataframe.csv')

# print(df.describe())

# 데이터 특성을 위한 전처리
# df_melt = df.melt(id_vars=['tier', 'champion', 'position'], value_vars=[
#                   'win_rate', 'pick_rate', 'ban_rate'], var_name='rate_type', value_name='rate')

# print(df_melt)

# 데이터 특성을 위한 시각화
# sns.boxplot(x='rate_type', y='rate', data=df_melt)
# sns.violinplot(x='rate_type', y='rate', data=df_melt)
# plt.ylim(-10, 110)
# plt.axhline(y=0, color='r', linestyle=':', linewidth=1)
# plt.axhline(y=100, color='r', linestyle=':', linewidth=1)
# plt.show()

# 분석을 위한 시각화
fig = px.scatter(df, x='pick_rate',
                 y='ban_rate', color='position', animation_frame='tier', hover_data=['champion'], range_x=[-10, 60], range_y=[-10, 60])
fig.show()
