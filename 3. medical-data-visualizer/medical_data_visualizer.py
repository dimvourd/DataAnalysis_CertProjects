import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column 
'''To determine if a person is overweight, 
first calculate their BMI by dividing their weight in kilograms
 by the square of their height in METERS.
 '''
df['overweight']=(df['weight']/(df['height']/100)**2)

''' 
 If that value is > 25 then the person is overweight.
 Use the value 0 for NOT overweight and the value 1 for overweight.
'''

df['overweight']=df['overweight'].apply(lambda x: 1 if x>25  else 0)


# Normalize data by making 0 always good and 1 always bad. 
#If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
#If the value is more than 1, make the value 1.

df['cholesterol']= df['cholesterol'].apply(lambda x: 0 if x==1 else 1)
#print(df['cholesterol'].value_counts())
#print(df['gluc'].value_counts())

df['gluc']= df['gluc'].apply(lambda x: 0 if x==1 else 1)
#print(df['gluc'].value_counts())

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values 
    # from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=
                         [
                         'cholesterol','gluc',
                         'smoke','alco',
                         'active','overweight'
                         ]
                     )
    df_cat=pd.DataFrame(df_cat.value_counts())
    
    #You will have to rename one of the 
    #columns for the catplot to work correctly.
    
    df_cat=(df_cat.sort_values(by='variable').reset_index())
    df_cat.rename(columns={0:'total'},inplace=True)
    
    # Show the counts of each feature. 
    # Group and reformat the data to split it by 'cardio'.
    # Draw the catplot with 'sns.catplot()'
    fig=sns.catplot(x="variable", y = 'total', col="cardio",
                      hue = 'value' , data=df_cat , kind="bar").fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

''' Clean the data.
 Filter out the following patient segments that represent incorrect data:
diastolic pressure is higher than systolic 
1(Keep the correct data with (df['ap_lo'] <= df['ap_hi']))

height is less than the 2.5th percentile 
2(Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
3height is more than the 97.5th percentile
4weight is less than the 2.5th percentile
5weight is more than the 97.5th percentile
'''

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    mask1=df['ap_lo'] <= df['ap_hi']
    mask2=df['height'] >= df['height'].quantile(0.025)
    mask3=df['height'] <= df['height'].quantile(0.975)
    mask4=df['weight'] >= df['weight'].quantile(0.025)
    mask5=df['weight'] <= df['weight'].quantile(0.975)
    
    df_heat=df[mask1&mask2&mask3&mask4&mask5]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)

    mask[np.triu_indices_from(corr)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))
    sns.color_palette("icefire", as_cmap=True)

    # Draw the heatmap with 'sns.heatmap()'
    
    corMatrix=sns.heatmap(data=corr,fmt='.1f',center=0.00,square=True,annot=True,cbar=True,
                          mask=mask,cbar_kws={'shrink': 0.3},vmax=0.28,vmin=-0.1
                          )
    plt.show()
#,vmax=0.28,vmin=-0.08,Linewidth = .5,



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
