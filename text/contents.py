train_info = """<class 'pandas.core.frame.DataFrame'>
RangeIndex: 26457 entries, 0 to 26456
Data columns (total 20 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   index          26457 non-null  int64  
 1   gender         26457 non-null  object 
 2   car            26457 non-null  object 
 3   reality        26457 non-null  object 
 4   child_num      26457 non-null  int64  
 5   income_total   26457 non-null  float64
 6   income_type    26457 non-null  object 
 7   edu_type       26457 non-null  object 
 8   family_type    26457 non-null  object 
 9   house_type     26457 non-null  object 
 10  DAYS_BIRTH     26457 non-null  int64  
 11  DAYS_EMPLOYED  26457 non-null  int64  
 12  FLAG_MOBIL     26457 non-null  int64  
 13  work_phone     26457 non-null  int64  
 14  phone          26457 non-null  int64  
 15  email          26457 non-null  int64  
 16  occyp_type     18286 non-null  object 
 17  family_size    26457 non-null  float64
 18  begin_month    26457 non-null  float64
 19  credit         26457 non-null  float64
dtypes: float64(4), int64(8), object(8)
memory usage: 4.0+ MB"""

test_info = """<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 19 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   index          10000 non-null  int64  
 1   gender         10000 non-null  object 
 2   car            10000 non-null  object 
 3   reality        10000 non-null  object 
 4   child_num      10000 non-null  int64  
 5   income_total   10000 non-null  float64
 6   income_type    10000 non-null  object 
 7   edu_type       10000 non-null  object 
 8   family_type    10000 non-null  object 
 9   house_type     10000 non-null  object 
 10  DAYS_BIRTH     10000 non-null  int64  
 11  DAYS_EMPLOYED  10000 non-null  int64  
 12  FLAG_MOBIL     10000 non-null  int64  
 13  work_phone     10000 non-null  int64  
 14  phone          10000 non-null  int64  
 15  email          10000 non-null  int64  
 16  occyp_type     6848 non-null   object 
 17  family_size    10000 non-null  float64
 18  begin_month    10000 non-null  float64
dtypes: float64(3), int64(8), object(8)
memory usage: 1.4+ MB"""

# == numeric_process ==
income_total_code = """# 만단위로 생성
data['income_total'] = data['income_total']/10000
# 편차 제곱 변수 생성
data['income_total_dev'] = (data['income_total'] - data['income_total'].mean())**2
# 로그 변환
data['income_total_log'] = data['income_total'].apply(np.log1p)"""
DAYS_EMPLOYED_code = """# 0 이상인 경우 0으로 모두 변환
data.loc[data['DAYS_EMPLOYED'] >= 0,'DAYS_EMPLOYED']=0
# day를 year로 변환
data['DAYS_EMPLOYED'] = data['DAYS_EMPLOYED'].apply(days_to_year) 
# 로그 변환
data['DAYS_EMPLOYED_log'] = data['DAYS_EMPLOYED'].apply(np.log1p)"""
begin_month_code = """# 마이너스 변환
data['begin_month'] = data['begin_month'].apply(minus)"""
DAYS_BIRTH_code = """# day를 year로 변환
data['DAYS_BIRTH'] = data['DAYS_BIRTH'].apply(days_to_year)"""
ratio_code = """data['EMPLOYED_BIRTH_RATIO'] = data['DAYS_EMPLOYED']/data['DAYS_BIRTH']
data['INCOME_EMPLOYED_RATIO'] = data['income_total']/data['DAYS_EMPLOYED']
data['INCOME_BIRTH_RATIO'] = data['income_total']/data['DAYS_BIRTH']"""
fam_child_code = """data['diff_fam_child'] = data['family_size'] - data['child_num']"""
fam_child_outlier_code = """data.loc[data['child_num'] >= 2,'child_num'] = 2
data.loc[data['family_size'] >= 5,'child_num'] = 5"""
fam_child_sum_code = """data['FAM_CHILD_SUM'] = data[['child_num', 'family_size']].sum(axis=1)"""
income_ratio_code = """data['INCOME_FAM_RATIO'] = data['income_total']/data['family_size']
data['INCOME_child_num_RATIO'] = data['income_total']/data['child_num']"""
minus_code = """data['BIRTH_MINUS_EMPLOYED'] = data['DAYS_BIRTH'] - data['DAYS_EMPLOYED']"""
income_minus_code = """data['INCOME_BIRTH_MINUS_EMPLOYED_RATIO'] = data['income_total']/data['BIRTH_MINUS_EMPLOYED']"""

# == days_to_year ==
days_to_year = '''def days_to_year(x):
    return (x*-1)/365'''

# == minus ==
convert_minus = '''def minus(x):
    return x * -1'''

# == remove_outlier ==
remove_outlier = """df = train[column]

# 1분위수
quan_25 = np.percentile(df.values, 25)

# 3분위수
quan_75 = np.percentile(df.values, 75)

iqr = quan_75 - quan_25 

lowest = quan_25 - iqr * 5
highest = quan_75 + iqr * 5
outlier_index = df[(df < lowest) | (df > highest)].index
print('outlier의 수 : ' , len(outlier_index))
print(df.iloc[outlier_index])
train.drop(outlier_index, axis = 0, inplace = True)

# 함수를 만들어 child_num 컬럼의 이상치를 제거한다.
train = remove_outlier(train, 'child_num')"""


# == add_var ==
add_var = """ # 개개인의 구분할 수 있는 변수들을 묶어서 생성
data['personal_id'] = data['gender'] + "_" +
data['DAYS_BIRTH'].astype(str) + "_" + 
data['income_total'].astype(str) + "_" + 
data['income_type'].astype(str) 

# 카드를 생성한 기간도 같은 경우가 있어서 begin을 추가하여 하나의 변수를 더 생성
data['personal_begin_id'] = data['gender'] + "_" + 
data['DAYS_BIRTH'].astype(str) + "_" + 
data['income_total'].astype(str) + "_" + 
data['income_type'].astype(str) + "_" + 
data['begin_month'].astype(str)

# 그외의 변수들을 조합하여 하나의 변수로 추가 생성
data['g_r_c'] = data['gender'] + "_" + data['reality'] + "_" + data['car'] 
data['p_w_e'] = data['phone'].astype(str) + "_" + data['work_phone'].astype(str) + "_" + data['email'].astype(str) 
data['d_c_r_i'] = data['DAYS_BIRTH'].astype(str) + "_" + data['car'] + "_" + data['reality'] + "_" + data['income_total'].astype(str)
data['d_c_r_i_t'] = data['DAYS_BIRTH'].astype(str) + "_" + data['car'] + "_" + data['reality'] + "_" + data['income_total'].astype(str) + "_" + data['income_type'].astype(str)"""


# == 6. occyp_process ==
def_occype = '''def occype_process(data):'''
replace_na = '''    data['occyp_type'] = data['occyp_type'].fillna('NAN')'''
replace_no_work = '''   data.loc[(data['DAYS_EMPLOYED'] == 0) & (data['occyp_type'] == 'NAN'), 'occyp_type'] = 'no_work'''
def_occype_return = '''    return data'''

# == make_bin ==
make_bin = """def make_bin(df, variable, n):
    
data = df
count, bin_dividers = np.histogram(data[variable], bins=n)
bin_names=[str(i) for i in range(n)]
data['%s_bin' % variable] = pd.cut(x=data[variable], bins=bin_dividers, labels=bin_names, include_lowest=True)
data['%s_bin' % variable] = pd.factorize(data['%s_bin' % variable])[0]
print(data['%s_bin' % variable], '\n\n')
    
return data"""
