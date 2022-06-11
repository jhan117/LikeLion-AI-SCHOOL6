from charts import *

import streamlit as st

st.title('유치원')

with st.container():
    st.header('유치원/원아수')

    with st.container():
        col1, col2 = st.columns(2)
        col1.metric('2021년 유치원', current_sch, vol_sch)
        col2.metric('2021년 원아수', current_stu, vol_stu)

    charts1 = st.selectbox('그래프를 선택해주세요', ('유치원/원아수', '유치원당 원아수'))

    if charts1 == '유치원/원아수':
        st.write(
            '여기에 텍스트를 입력해요 ㅇ마ㅣ렁ㄴ미렁ㄴ마리ㅓㅇㄴㅁ리ㅏㄴ머리ㅏㄴㅁㄹ')
        st.write(
            '여기에 텍스트를 입력해요 ㅇ마ㅣ렁ㄴ미렁ㄴ마리ㅓㅇㄴㅁ리ㅏㄴ머리ㅏㄴㅁㄹ')
        st.plotly_chart(fig1)
    else:
        st.plotly_chart(fig2)
    st.header('교원/원아수')
    with st.container():
        col1, col2 = st.columns(2)
        col1.metric('2021년 교원수', current_teach, vol_teach)
        col2.metric('2021년 원아수', current_stu, vol_stu)

    charts1 = st.selectbox('그래프를 선택해주세요', ('교원/원아수', '교원 1인당 원아수'))

    if charts1 == '교원/원아수':
        st.write(
            '여기에 텍스트를 입력해요 ㅇ마ㅣ렁ㄴ미렁ㄴ마리ㅓㅇㄴㅁ리ㅏㄴ머리ㅏㄴㅁㄹ')
        st.write(
            '여기에 텍스트를 입력해요 ㅇ마ㅣ렁ㄴ미렁ㄴ마리ㅓㅇㄴㅁ리ㅏㄴ머리ㅏㄴㅁㄹ')
        st.plotly_chart(fig3)
    else:
        st.plotly_chart(fig4)
