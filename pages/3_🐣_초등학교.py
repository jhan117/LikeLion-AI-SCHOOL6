from data_elementary import *
import koreanize_matplotlib

import streamlit as st

st.set_page_config(layout='wide')

# === 초등학교 ===
with st.container():
    st.markdown('## 초등학교')
    st.markdown('### 초등학교/학생수')
    with st.container():
        ele_t_col1, ele_t_col2, ele_t_col3, empty_t = st.columns([1, 1, 1, 3])
        ele_t_col1.metric('2021년 초등학교 개수', cur_ele_sch, vol_ele_sch)
        ele_t_col2.metric('2021년 초등학생수', cur_ele_stu, vol_ele_stu)
        ele_t_col3.metric('2021년 초등학교당 학생수', cur_ele_stu_sch, vol_ele_stu_sch)

        with st.container():
            chart_t_col1, chart_t_col2 = st.columns([1, 2])
            with chart_t_col1:
                st.markdown('초등학교/학생수에 대해서 비교해봤다.')
                st.markdown(
                    "초등학교는 2021년 전년비 0.36% 증가한 6,341개로 증가하는 추세를 지속 보이고 있으나, 초등학생수는 0.79% 감소한 267.2만명으로 '18~'19년을 제외하고는 지속적으로 줄어드는 양상을 보인다.")
                st.markdown(
                    "그동안 학교수 대비 학생수가 많았던 곳(수도권 예상)에서는 학교당 학생수가 균형이 맞춰질 수 있으나, 어느 지역(지방 예상에서는 학생대비 학교가 너무 많은 불균형이 나타날 수도 있다.")
                st.pyplot(fig_ele1, use_container_width=True)
            with chart_t_col2:
                st.pyplot(fig_ele2, use_container_width=True)

    st.markdown('### 교원/학생수')
    with st.container():
        ele_b_col1, ele_b_col2, ele_b_col3, empty_b = st.columns([1, 1, 1, 3])
        ele_b_col1.metric('2021년 초등학교 교원수', cur_ele_teach, vol_ele_teach)
        ele_b_col2.metric('2021년 초등학생수', cur_ele_stu, vol_ele_stu)
        ele_b_col3.metric('2021년 교원당 학생수', cur_ele_stu_teach,
                          vol_ele_stu_teach)

        with st.container():
            chart_b_col1, chart_b_col2 = st.columns([1, 2])
            with chart_b_col1:
                st.markdown('교원/학생수에 대해서 비교해봤다.')
                st.markdown(
                    "초등학교 교원수는 2021년 전년비 1.02% 증가한 19.1만명으로 증가하는 추세를 지속 보이고 있으나, 초등학생수는 0.79% 감소한 267.2만명으로 감소하는 양상을 보인다.")
                st.markdown(
                    "그동안 교원수 대비 학생수가 많았던 곳에서는 균형이 맞춰질 수 있으나, 어느 곳에서는 학생대비 교원이 너무 많은 불균형이 나타날 수도 있다.")
                st.pyplot(fig_ele3, use_container_width=True)
            with chart_b_col2:
                st.pyplot(fig_ele4, use_container_width=True)
