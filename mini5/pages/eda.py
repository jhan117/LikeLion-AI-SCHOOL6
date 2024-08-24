import streamlit as st

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from text.contents import *

sns.set_theme()


def catplot(col):
    name_list = ['income_type', 'edu_type', 'house_type', 'family_type']

    fig, axes = plt.subplots(1, 3)

    if col in name_list:
        axes[0].tick_params(rotation=90)
        axes[1].tick_params(rotation=90)
        axes[2].tick_params(rotation=90)

    if col != 'occyp_type':
        sns.countplot(data=train_0, x=col,
                      order=train_0[col].value_counts().index, ax=axes[0])
        sns.countplot(data=train_1, x=col,
                      order=train_1[col].value_counts().index, ax=axes[1])
        sns.countplot(data=train_2, x=col,
                      order=train_2[col].value_counts().index, ax=axes[2])

        plt.subplots_adjust(wspace=0.3)
    else:
        sns.countplot(data=train_0, y=col,
                      order=train_0[col].value_counts().index, ax=axes[0])
        sns.countplot(data=train_1, y=col,
                      order=train_1[col].value_counts().index, ax=axes[1])
        sns.countplot(data=train_2, y=col,
                      order=train_2[col].value_counts().index, ax=axes[2])

        axes[1].set(xlabel='occyp_type')

        plt.subplots_adjust(wspace=0.8)

    axes[0].set_title('credit=0')
    axes[0].tick_params(labelsize=6)
    axes[0].set(xlabel=None, ylabel=None)

    axes[1].set_title('credit=1')
    axes[1].tick_params(labelsize=6)
    axes[1].set(ylabel=None)

    axes[2].set_title('credit=2')
    axes[2].tick_params(labelsize=6)
    axes[2].set(xlabel=None, ylabel=None)

    st.pyplot(fig)


def numplot(col):
    fig, axes = plt.subplots(1, 3)

    sns.boxplot(data=train_0, y=col,
                order=train_0[col].value_counts().index, width=0.3, ax=axes[0], palette='Set3')
    sns.boxplot(data=train_1, y=col,
                order=train_1[col].value_counts().index, width=0.3, ax=axes[1], palette='Paired')
    sns.boxplot(data=train_2, y=col,
                order=train_2[col].value_counts().index, width=0.3, ax=axes[2], palette='Spectral')

    axes[0].set_title('credit=0')
    axes[0].tick_params(labelsize=8)
    axes[0].set(xlabel=None, ylabel=None)

    axes[1].set_title('credit=1')
    axes[1].tick_params(labelsize=8)
    axes[1].set(xlabel=col, ylabel=None)

    axes[2].set_title('credit=2')
    axes[2].tick_params(labelsize=8)
    axes[2].set(xlabel=None, ylabel=None)

    plt.subplots_adjust(wspace=0.5)
    st.pyplot(fig)


train = pd.read_csv('./data/train.csv')
train = train.fillna('NaN')
test = pd.read_csv('./data/test.csv')

train_0 = train.loc[train['credit'] == 0]
train_1 = train.loc[train['credit'] == 1]
train_2 = train.loc[train['credit'] == 2]

independent_list = ['gender', 'car', 'reality', 'child_num',
                    'income_type', 'edu_type', 'family_type', 'house_type', 'FLAG_MOBIL', 'work_phone', 'phone', 'email',
                    'occyp_type', 'family_size']
numerical_list = ['DAYS_BIRTH', 'DAYS_EMPLOYED', 'begin_month', 'income_total']

st.markdown("""**목차**
- [데이터 확인하기](#데이터-확인하기)
- [EDA](#eda)""")

with st.container():
    st.markdown(
        '### [데이터 확인하기](https://www.dacon.io/competitions/official/235713/talkboard/402821/)')
    st.markdown('신용카드 사용자들의 개인 신상정보 데이터이다.')

    st.markdown('#### train.csv (26457, 20)')
    st.markdown('`credit` 열 포함')
    st.dataframe(train.head())

    st.markdown('#### test.csv (10000, 19)')
    st.markdown('`credit` 열 미포함')
    st.dataframe(test.head())

st.markdown('---')

with st.container():
    st.markdown('### EDA')
    st.markdown('#### 피처 이해')
    radio_data = st.radio('데이터 종류를 선택하세요', ('train', 'test'))
    if radio_data == 'train':
        st.code(train_info, language=None)
    else:
        st.code(test_info, language=None)
    st.markdown(
        'number type은 `credit`을 포함해 12개이고 object type은 8개이다. 또한, `occyp_type`만 `null` 값이 존재함을 알 수 있다.')

    st.image('./histogram.png', use_column_width=True)

    eda_col1, eda_col2 = st.columns(2)
    eda_col1.markdown('##### 수치형 데이터')
    eda_col1.markdown("""- 이산형 데이터
    - DAYS_BIRTH : 출생일
    - DAYS_EMPLOYED : 업무 시작일
    - begin_month : 신용카드 발급 월
- 연속형 데이터
    - income_total : 연간 소득""")

    eda_col2.markdown('##### 범주형 데이터')
    eda_col2.markdown("""- 명목형 데이터
    - gender : 성별
    - car : 차량 소유 여부
    - reality : 부동산 소유 여부
    - income_type : 소득 분류
    - family_type : 결혼 여부
    - house_type : 생활 방식
    - FLAG_MOBIL : 핸드폰 소유 여부
    - work_phone : 업무용 전화 소유 여부
    - phone : 전화 소유 여부
    - email : 이메일 소유 여부
    - occyp_type : 직업 유형
- 순서형 데이터
    - child_num : 자녀 수
    - edu_type : 교육 수준
    - family_size : 가족 규모
    - credit : 사용자의 신용카드 대금 연체를 기준으로 한 신용도""")

    # == 범주형 시각화 그래프 그리기
    st.markdown('#### 피처 시각화')
    independent_var = st.radio(
        '독립변수 설정', independent_list, horizontal=True)

    if independent_var == independent_list[0]:
        catplot(independent_var)
    elif independent_var == independent_list[1]:
        catplot(independent_var)
    elif independent_var == independent_list[2]:
        catplot(independent_var)
    elif independent_var == independent_list[3]:
        catplot(independent_var)
    elif independent_var == independent_list[4]:
        catplot(independent_var)
    elif independent_var == independent_list[5]:
        catplot(independent_var)
    elif independent_var == independent_list[6]:
        catplot(independent_var)
    elif independent_var == independent_list[7]:
        catplot(independent_var)
    elif independent_var == independent_list[8]:
        catplot(independent_var)
    elif independent_var == independent_list[9]:
        catplot(independent_var)
    elif independent_var == independent_list[10]:
        catplot(independent_var)
    elif independent_var == independent_list[11]:
        catplot(independent_var)
    elif independent_var == independent_list[12]:
        catplot(independent_var)
    else:
        catplot(independent_var)

    # 수치형 시각화 그래프 그리기
    st.markdown('#### 수치형 시각화')
    option = st.selectbox('변수명을 선택해주세요', numerical_list)

    if option == numerical_list[0]:
        numplot(option)
    elif option == numerical_list[1]:
        numplot(option)
    elif option == numerical_list[2]:
        numplot(option)
    else:
        numplot(option)
