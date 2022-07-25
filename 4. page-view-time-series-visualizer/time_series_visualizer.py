import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 parse_dates=True,index_col=['date'])
# Clean data
'''
Clean the data by filtering out days when the page views 
were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
height is less than the 2.5th percentile 
'''

mask1=df['value'] >= df['value'].quantile(0.025)
mask2=df['value'] <= df['value'].quantile(0.975)
df=df[mask1&mask2]

'''
Create a draw_line_plot function that uses Matplotlib to draw a line chart similar
to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019.
The label on the x axis should be Date and the label on the y axis should be Page Views.
'''
def draw_line_plot():
    # Draw line plot

    fig, axes = plt.subplots(figsize=(16, 6))

    x=df.index
    y=df['value']
    axes.plot(x , y,color='red')
    
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    axes.legend()
    fig
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    '''
    Create a draw_bar_plot function that draws a bar chart similar to 
    "examples/Figure_2.png". 
    It should show average daily page views for each month 
    grouped by year. 
    The legend should show month labels and have a title of Months.
    '''  
    df_bar=df.groupby([(df.index.year), (df.index.month)]).mean()
    df_bar.index.set_names(['Years','Months'],inplace=True)
    df_bar=(df_bar.reset_index())
    df_bar=df_bar.set_index(['Years','Months']).value
   
    # Draw bar plot
    '''
    It should show average daily page views for each month 
    grouped by year. 
    The legend should show month labels and have a title of Months.
    On the chart, the label on the x axis should be Years and
    the label on the y axis should be Average Page Views.
    '''
    months=[ 'January', 'February',  'March', 'April',  'May',
             'June', 'July', 'August', 'September',
             'October', 'November',  'December']
    df_bar=df_bar.unstack()
    
    fig=df_bar.plot(kind='bar',figsize=(  12, 8) ).figure

    plt.legend(labels=months,title='Months')
    plt.ylabel('Average Page Views')
    
    fig
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig



def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    '''
    These box plots should show how the values are distributed within a given year 
    or month and how it compares over time. 
    
    Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly.
    The boilerplate includes commands to prepare the data.
    '''
    # Draw box plots (using Seaborn)
    fig, axes= plt.subplots(1, 2, figsize=(18, 8), sharey=True)
    
    sns.boxplot(ax=axes[0], x='year', y='value',data=df_box)
    
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    
    sns.boxplot(ax=axes[1], x='month', y='value',data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
