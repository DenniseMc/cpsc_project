import matplotlib.pyplot as plt
from scipy import stats

def get_missing_values (key,df):
    print("\n\033[1m", key.title(), "\033[0m")
    print(df.isna().sum())

def get_outliers(key,df):
    print("\n\033[1m", key.title(), "\033[0m")
    #display descriptive statistics
    print("\n\033[1m", 'Descriptive statistics', "\033[0m")
    print(df.describe().applymap(lambda x: (((str(x).isnumeric()) and f"{x:.2f}") or x )))
    #display column data types
    print("\n\033[1m", 'Column data types', "\033[0m")
    print(df.dtypes)
    numeric_columns_index = [i for i,t in enumerate(df.dtypes) if str(t).startswith('float')]
    #display numeric columns
    print("\n\033[1m", 'Numeric columns', "\033[0m")
    numeric_columns = df.dtypes.iloc[numeric_columns_index].index
    print(numeric_columns)
    #display boxplots of numeric columns
    print("\n\033[1m", 'Boxplot', "\033[0m")
    try:
        df.plot.box(vert=False)
        plt.show()    
    except:
        print('No numeric data to plot')
    #display outliers of numeric columns
    data_z_score = stats.zscore(df[numeric_columns])
    for col in numeric_columns:        
        outliers = df[['location_key',col]][(data_z_score[col] >= 3) | (data_z_score[col] <= -3)]
        if len(outliers) > 0:
            print("\n\033[1m", 'Column outliers: ', "\033[0m", col)
            print(outliers)
