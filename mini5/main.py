import streamlit as st

st.markdown('# MINI PROJECT')
st.markdown(
    '## [신용카드 사용자 연체 예측 AI 경진대회](https://dacon.io/competitions/official/235713/overview/description)')
st.markdown('신용카드사는 신용카드 신청자가 제출한 개인정보와 데이터를 활용해 신용 점수를 산정합니다. 신용카드사는 이 신용 점수를 활용해 신청자의 향후 채무 불이행과 신용카드 대급 연체 가능성을 예측합니다.<br>현재 많은 금융업계는 인공지능(AI)를 활용한 금융 서비스를 구현하고자 합니다. 신용카드 사용자들의 개인 신상정보 데이터로 <u>**사용자의 신용카드 대금 연체 정도를 예측**</u>할 수 있는 인공지능 알고리즘을 개발해 금융업계에 제안할 수 있는 인사이트를 발굴해주세요!', unsafe_allow_html=True)
title_col1, title_col2 = st.columns([1, 1])
title_col1.markdown('- 문제 유형 : 분류')
title_col2.markdown('- 평가지표 : Log Loss')

st.markdown('---')

st.markdown('팀장 : 권기영')
st.markdown('팀원 : 김성훈, 손유선, 김재석, 김경배')
