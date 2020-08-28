
# -------------- Answer Question 1:

def answer_three():
    gold_column = df['Gold']
    max_value_medals = gold_column.max()

    answer_country = ''.join(df[(df['Gold'] == max_value_medals)].index.values)
    return answer_country

# ------------ Answer Question 2:

def answer_two():
    max_difference_medals = df['Gold'] - df['Gold.1']
    country_answer = ''.join(df[(df['Gold'] - df['Gold.1'] == max_difference_medals.max())].index.values)
    
    return country_answer


# ------------ Answer Question 3:

def answer_three():
    countries_comply_condition = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]

    difference_medals = countries_comply_condition['Gold'] - countries_comply_condition['Gold.1']
    total_gold_medals = countries_comply_condition['Gold'] + countries_comply_condition['Gold.1']

    operation_result = difference_medals / total_gold_medals

    df['Relative_Result'] = operation_result

    country_answer = ''.join(df[(df['Relative_Result'] == operation_result.max())].index.values)
    
    return country_answer

# -------------- Answer Question 4:

def answer_four():
    gold_weight = 3
    silver_weight = 2
    bronze_weight = 1
    total_weight = 6

    df['estimate'] = ((df['Gold.2'] * gold_weight) + (df['Silver.2'] * silver_weight) + (df['Bronze.2'] * bronze_weight)) / total_weight

    Points = pd.Series(df['estimate'])
    return Points


# ---------- Answer Question 5:

def answer_five():
    copy_df = census_df.copy()

    group_states_result = copy_df.STNAME.value_counts().reset_index(name='SUM_COUNTIES').sort_values(["index"], ascending=True)
    group_states_result = group_states_result.rename(columns={"index" : "STATE"})
    group_states_result = group_states_result.set_index('STATE')

    final_answer = ''.join(group_states_result[group_states_result['SUM_COUNTIES'] == group_states_result['SUM_COUNTIES'].max()].index.values)
    
    return final_answer


# -------- Answer Question 6:
def answer_six():
    filtering_data = census_df[census_df['SUMLEV'] == 50]
    filtering_data = filtering_data.groupby('STNAME')['CENSUS2010POP']
    filtering_data = filtering_data.apply(lambda x: x.nlargest(3).sum()).nlargest(3)
    filtering_data = filtering_data.index.values.tolist()
    return "YOUR ANSWER HERE"


# ----------- Answer Question 7:

def answer_seven():
    census_copy = census_df.copy()
    census_copy = census_copy[(census_copy['SUMLEV'] == 50)]
    columns_to_keep = ['STNAME', 'CTYNAME', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
    census_copy = census_copy[columns_to_keep]

    census_copy = census_copy.set_index('CTYNAME') 

    census_copy['CHANGE_TOTAL_VALUE'] = census_copy.max(axis=1) - census_copy.min(axis=1)
    answer_final = ''.join(census_copy[census_copy['CHANGE_TOTAL_VALUE'] == census_copy['CHANGE_TOTAL_VALUE'].max()].index.values)
    return answer_final


# ------------ Answer Question 8:

def answer_eight():
    final_copy = census_df.copy()
    final_copy = final_copy[(final_copy['REGION'] == 1) | (final_copy['REGION'] == 2)]
    final_copy = final_copy[final_copy['CTYNAME'].str.contains('Washington')]
    final_copy = final_copy[final_copy['POPESTIMATE2015'] > final_copy['POPESTIMATE2014']]
    columns_to_keep = ['STNAME', 'CTYNAME']
    final_copy = final_copy[columns_to_keep]
    final_copy.sort_index(ascending=True)
    return final_copy