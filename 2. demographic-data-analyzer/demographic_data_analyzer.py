import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset?
    #This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    mask=(df['sex']=='Male' )
    average_age_men=np.round(np.mean(df[mask].age ), 1)

    # What is the percentage of people who have a Bachelor's degree?
    #print((df['education']=='Bachelors').value_counts())
    mask=(df['sex']=='Male' )
    average_age_men=np.round(np.mean(df[mask].age ), 1)
    mask=df['education']=='Bachelors'
    percentage_bachelors = np.round((100*len(df[mask]))/len(df) ,1)


    # What percentage of people with advanced education 
    #(`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    mask1= ((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')) 
    mask2= (df['salary'] =='>50K')
        
    # What percentage of people without advanced education 
    #make more than 50K?
    
    # with `Bachelors`, `Masters`, or `Doctorate`
    higher_education = np.round((100*len(df[mask1 ])/len(df), 1 ))
    lower_education = np.round((100*len(df[~mask1 ])/len(df), 1 )) 

    # percentage with salary >50K
    higher_education_rich =  np.round((100*len(df[mask1 & mask2])/len(df[mask1])), 1 )
    lower_education_rich = np.round((100*len(df[~mask1 & mask2])/len(df[~mask1])), 1 )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = np.min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  
    mask3=(df['hours-per-week']==min_work_hours)

    num_min_workers = len(df[mask3])
    rich_percentage = np.round(100*len(df[mask2 & mask3])/len(df[mask3]),0)

    # What country has the highest percentage of people that earn >50K?
    counties_num=df['native-country'].value_counts()
  
    rich_num=df[mask2]['native-country'].value_counts()
    
    highest_earning_country = (100*rich_num/counties_num).idxmax()    
    highest_earning_country_percentage=np.round((100*rich_num/counties_num).max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask4=(df['native-country']=='India')
    top_IN_occupation = df['occupation'][mask4].describe().loc['top']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
