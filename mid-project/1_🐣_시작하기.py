from data_birth_count import *

import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

image_title = Image.open('./images/title.png')
st.image(image_title, use_column_width=True)
st.markdown('저출산으로 인구가 줄어드는데 학교와 교원수도 똑같이 작용하는지 궁금했다.')
st.markdown(
    '세계적으로 살펴봤을 때 2019년 초등학교 교사 1인당 학생수는 OECD 평균 14.5명으로 나타났는데, 우리는 이에 근접한지 아니면 더 열악한 환경에 처해있는지 확인해보고자 한다.')
st.markdown('그래서 출생아수, 유치원, 초등학교, 지역별로 비교해보면서 현상이 어떤지 살펴보겠다. ')
st.markdown('<p style="color:gray;">출처: Education at a Glance 2021(OECD)</p>',
            unsafe_allow_html=True)

# === 출산율/출생아수 ===
with st.container():
    st.markdown('## 출생아수/출산율')
    with st.container():
        empty_b, birth_figure = st.columns([1, 3])
        with empty_b:
            st.markdown(
                '2015년부터 출산율과 출생아수 모두 급감하는 현상을 확인할 수 있는데 이러한 현상에는 아래와 같은 다양한 원인이 있다고 볼 수 있다.')
            st.markdown('- 인구학적 요인: 출산 적령기 인구 감소')
            st.markdown('- 경제적 요인: 부동산 가격 등')
            st.markdown('- 문화적 요인: 일과 가정의 양립 어려움')
            st.markdown('- 정책/사회적 요인:늦은 산아제한 정책 폐지')
            st.markdown(
                '상기 언급한 요인들로 인하여 최근 들어 저출산 양상이 심화되고 있고 이러한 현상이 유치원, 초등학교에 어떤 영향을 끼치는지 분석하였다.')
            st.markdown("<p style='color: gray'>출처: 보건복지부, '2017년 저출산·고령화 국민인식조사'</p>",
                        unsafe_allow_html=True)
        with birth_figure:
            st.pyplot(birth_fig, use_container_width=True)
