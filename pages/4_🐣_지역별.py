from data_state import *
import streamlit as st

st.set_page_config(layout='wide')
st.markdown('## 지역별 학교-학생수 분석')

st.markdown("""<p style=" color:gray; font-size: 14px;">
        출산율 저하에 따른 학생수 감소 문제에 대비하여, 학교와 교원의 적정 수에 대한 논의가 활발해지고 있다. <br>
        이에 대한 자료로서 지역별로 상당한 차이가 있기 때문에 지역별 자료도 제작하였다.<br>
        <br>  
        </p>""", unsafe_allow_html=True)


st.markdown('### 지역별 교원당 학생수')

st.markdown("""<p style=" color:gray; font-size: 14px;">
        'OECD 교육지표 2021'에 따르면 2019년 기준 OECD 평균 교원당 학생수는 14.5명이다.  <br>
        일부 수도권 지역을 제외하고는 모두 그 이하를 만족하는데, OECD 교육지표 기준에서 제외됐던 교장과 교감, 영양, 사서, 보건, 상담교사 까지 망라하다보니   <br>
        교육기본통계상 교원 1인당 학생수가 OECD교육지표 보다 항상 적게 나온다.  
        </p>""", unsafe_allow_html=True)

with st.container():
    StateStuTchCol1, StateStuTchCol2 = st.columns([1, 2])
    with StateStuTchCol1:
        option_tch = st.selectbox(
            '초등학교 또는 유치원을 선택하세요.',
            ('초등학교', '유치원'))

        st.write(""" 
                
                """)
        start_opt_tch, end_opt_tch = st.select_slider(
            '비교하고 싶은 시작연도와 끝연도를 선택하세요.',
            options=[2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2021],
            value=(2012, 2021))

        st.plotly_chart(draw_graph4(option_tch, start_opt_tch, end_opt_tch),
                        use_container_width=True)
    with StateStuTchCol2:
        st.markdown("""<p style=" color:gray; font-size: 14px;">
        <br>
        <br>
        <br>
        </p>""", unsafe_allow_html=True)
        st.plotly_chart(draw_graph3(option_tch, end_opt_tch),
                        use_container_width=True)


# === 지역별 학교 ===
st.markdown('### 지역별 학급당 학생수')
st.markdown("""<p style=" color:gray; font-size: 14px;">
        교사 1인당 학생수의 지표의 계산이 현실을 제대로 반영하지 못한다는 지적이 있어 최근에는 학급당 학생수에 기반하여 학급 규모에 대해 연구되고 있다.<br>
        학급규모는 교육의 질을 결정하는 데 있어 매우 큰 영향을 미친다.   <br> 
        학급당 학생 수가 많을수록 학생에게 균등한 학습의 질과 기회를 제공하는 데 문제가 있음이 다수의 연구를 통해 밝혀졌다.  <br> 
        반면, 학급규모가 작아질수록 수업에서 요구하는 과제 행동이 증가하고 수업과 무관한 행동이 감소한다는 결과가 일반적이다.  <br> 
        　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　<수업방식 다양화에 따른 학급규모 분석> - 교육정책네트워크 
        </p>""", unsafe_allow_html=True)


with st.container():
    StateStuSchCol1, StateStuSchCol2 = st.columns([1, 2])
    with StateStuSchCol1:
        option_sch = st.selectbox(
            ' ',
            ('초등학교', '유치원'))

        st.write(""" 
                
                """)
        start_opt_sch, end_opt_sch = st.select_slider(
            '비교하고 싶은 시작연도와 끝연도를 선택하세요.',
            options=[2012, 2013, 2014, 2015, 2016,
                     2017, 2018, 2019, 2020, 2021],
            value=(2012, 2021))

        st.plotly_chart(draw_graph2(option_sch, start_opt_sch, end_opt_sch),
                        use_container_width=True)
    with StateStuSchCol2:

        st.markdown("""<p style=" color:gray; font-size: 14px;">
        <br>
        <br>
        <br>
        </p>""", unsafe_allow_html=True)

        st.plotly_chart(draw_graph1(option_sch, end_opt_sch),
                        use_container_width=True)
