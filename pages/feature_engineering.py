import streamlit as st

from text.contents import *

# 1. days_to_year
# 2. minus
# 3. remove_outlier
# 4. add_var
# 5. numeric_process
# 6. occyp_process
# 7. make_bin
st.markdown('### Feature Engineering')
st.markdown("""**목차**
- [days_to_year](#days-to-year)
- [minus](#minus)
- [remove_outlier](#remove-outlier)
- [add_var](#add-var)
- [numeric_process](#numeric-process)
- [occyp_process](#occyp-process)
- [make_bin](#make-bin)""")

# == 1. days_to_year ==
st.markdown('#### days_to_year')
st.markdown('##### day를 year로 변경해주는 함수')
st.code(days_to_year, language='python')

# == 2. minus ==
st.markdown("#### minus")
st.markdown("##### 마이너스 변환")
st.code(convert_minus, language='python')

# == 3. remove_outlier ==
st.markdown('#### remove_outlier')
st.markdown('컬럼별 Q3, Q1, IQR 값 구하기 -> 각 값의 이상치 여부 판별하기 -> 이상치 행 제거')
st.code(remove_outlier, language='python')

# == 4. add_var ==
st.markdown('#### add_var')
st.markdown("변수조합으로 추가 변수(object)생성하기 -> 개인을 구분할 수 있는 변수들을 묶어서 생성 -> 카드를 생성한 기간도 같은 경우가 있어서 begin을 추가하여 하나의 변수를 더 생성 -> 그외의 변수들을 조합하여 하나의 변수로 추가 생성", unsafe_allow_html=True)
st.code(add_var, language='python')

# == 5. numeric_process ==
st.markdown('#### numeric_process')
st.markdown('##### income_total 변수 전처리')
st.code(income_total_code, language='python')
st.markdown('##### DAYS_EMPLOYED 변수 전처리')
st.code(DAYS_EMPLOYED_code, language='python')
st.markdown('##### begin_month 변수 전처리')
st.code(begin_month_code, language='python')
st.markdown('##### DAYS_BIRTH 변수 전처리')
st.code(DAYS_BIRTH_code, language='python')
st.markdown('##### DAYS_BIRTH, DAYS_EMPLOYED, income_total변수를 조합하여 RATIO 변수 생성')
st.code(ratio_code, language='python')
st.markdown('##### 가족수 - 자식수')
st.code(fam_child_code, language='python')
st.markdown('##### child_num과 family_size는 다음과 같이 최대 2와 5가 되도록 전처리')
st.code(fam_child_outlier_code, language='python')
st.markdown('##### 가족수와 자녀수 sum 변수 추가')
st.code(fam_child_sum_code, language='python')
st.markdown('##### income을 가족 수 및 자식 수로 나눈 비율')
st.code(income_ratio_code, language='python')
st.markdown('##### 일을 하게 된 시점 변수 추가')
st.code(minus_code, language='python')
st.markdown('##### income total 변수에 before_EMPLOYED로 나눈 변수 추가')
st.code(income_minus_code, language='python')

# == 6. occyp_process ==
st.markdown("#### occyp_process")
st.markdown("##### occyp_type 변수 전처리")
st.markdown("###### occyp_type 변수에만 있는 결측치를 'NAN' 값으로 대체")
st.code(def_occype, language='python')
st.code(replace_na, language='python')
st.markdown("###### 경력이 없고 직업군이 none인 사람은 no_work로 대체")
st.code(replace_no_work, language='python')
st.code(def_occype_return, language='python')

# == 7. make_bin ==
st.markdown('#### make_bin')
st.markdown('##### 구간화 함수')
st.code(make_bin, language='python')
