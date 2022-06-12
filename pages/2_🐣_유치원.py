from charts_kinder import *

import streamlit as st

st.set_page_config(layout='wide')

# === 유치원 ===
with st.container():
    st.markdown('## 유치원')
    st.markdown('### 유치원/원아수')
    with st.container():
        kinder_t_col1, kinder_t_col2, kinder_t_col3, empty_t = st.columns([
                                                                          1, 1, 1, 3])
        kinder_t_col1.metric('2021년 유치원', current_sch, vol_sch)
        kinder_t_col2.metric('2021년 원아수', current_stu, vol_stu)
        kinder_t_col3.metric('2021년 유치원당 원아수', current_sch_stu, vol_sch_stu)

        chart_t_col1, chart_t_col2 = st.columns([1, 2])
        with chart_t_col1:
            st.markdown('유치원/원아수에 대해서 비교해봤다.')
            st.markdown(
                "유치원은 2021년 전년비 0.52% 하락한 8,660개로 '18년부터 감소 추세를 보이고 있으며, 원아수는 4.89% 감소한 58.26만명으로 '16년부터 감소하는 추세를 보인다. 또한, 유치원당 원아수는 4.4% 감소한 67.27명으로 '16년부터 감소하는 추세를 보인다.")
            st.markdown("유치원은 원아수에 따라서 학교수가 조절되는 특징이 보인다.")
            st.plotly_chart(kinder_fig1, use_container_width=True)
        with chart_t_col2:
            st.plotly_chart(kinder_fig2, use_container_width=True)

    st.markdown('### 교원/원아수')
    with st.container():
        kinder_b_col1, kinder_b_col2, kinder_b_col3, empty_b = st.columns([
                                                                          1, 1, 1, 3])
        kinder_b_col1.metric('2021년 교원수', current_teach, vol_teach)
        kinder_b_col2.metric('2021년 원아수', current_stu, vol_stu)
        kinder_b_col3.metric('2021년 교원 1인당 원아수',
                             current_teach_stu, vol_teach_stu)

        chart_b_col1, chart_b_col2 = st.columns([1, 2])
        with chart_b_col1:
            st.markdown('교원/원아수에 대해서 비교해봤다.')
            st.markdown(
                "교원수는 2021년 전년비 0.36% 하락한 53.46천명으로 '18년부터 감소 추세를 보이고 있으며, 원아수는 4.89% 감소한 58.26만명으로 '16년부터 감소하는 추세를 보인다. 또한, 교원 1인당 원아수는 4.55% 감소한 10.9명으로 계속 감소하는 추세를 보인다.")
            st.markdown(
                "원아수가 감소하지만 교원수는 그다지 영향을 받지 않았다. 그러나 교원 1인당 원아수가 계속해서 감소하는 특징이 보인다.")
            st.plotly_chart(kinder_fig3, use_container_width=True)
        with chart_b_col2:
            st.plotly_chart(kinder_fig4, use_container_width=True)
