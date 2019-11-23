import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns; sns.set()

path = '/Users/hadakechi/Projects/AIDeepDive_Nov2019/PythonPandasGitNumpy_Krista/'

Composite = pd.read_csv(path + 'SPTSXComposite.csv', index_col = 'Ticker')
MktCapEmp = pd.read_csv(path + 'SPTSXCap_Employees.csv', index_col = 'Ticker')
Transactions = pd.read_csv(path + 'SP_Transactions.csv', index_col = 'Ticker')

Composite.loc[:,['Name','TotalAssets','PrimarySector']].head()

MktCapEmp.head()

Transactions.groupby('Ticker').count().head()

TotalTrns= Transactions.groupby('Ticker').sum()
TotalTrns['AvgTrnsValue'] = Transactions.groupby('Ticker').mean()
TotalTrns['TrnsCount'] = Transactions.TransactionType.groupby('Ticker').count()
TotalTrns = TotalTrns.rename(columns= {'TransactionValue' : 'TotalTrnsValue'})
TotalTrns.drop_duplicates(keep = 'first', inplace = True)

df1 = Composite.merge(MktCapEmp.loc[:,['NumberEmployees','MarketCapitalization']], on = 'Ticker', how = 'left')
df1 = df1.drop_duplicates(keep= 'first')
df1.head()

df1 = df1.drop(['TotalRevenue','GeographicSegments', 'Name'], axis=1)
df1 = df1.merge(TotalTrns.loc[:,['TrnsCount', 'AvgTrnsValue']], on = 'Ticker', how = 'left')
df1 = df1.drop_duplicates(keep= 'first')

df1.isna().any()

df1.describe().round(1)

df1.loc[df1.TrnsCount.isna() | df1.NumberEmployees.isna() | df1.AvgTrnsValue.isna()].head()

df1.TrnsCount.fillna(value = 0, inplace = True)
df1.AvgTrnsValue.fillna(value = 0, inplace = True)

df1.NumberEmployees.loc['TSX:RNW'] = 291

DroppedTickers = Transactions.merge(df1, on = 'Ticker', how = 'outer').index.drop_duplicates(keep = 'first')
DroppedTickers = pd.Series(DroppedTickers)

with open('Dropped_Tickers.txt', 'w') as file:
    file.write(DroppedTickers.to_string())


df1.MarketCapitalization.plot.hist(bins = 50)

df1.corr()

plot1 = df1.plot.scatter('MarketCapitalization', 'TotalAssets')


plot2 = df1.plot.scatter('MarketCapitalization', 'TrnsCount')



df1['MktCapSize']=pd.cut(df1.MarketCapitalization,3, labels=['small', 'Medium', 'High'])
df1['TtlAsstSize']=pd.cut(df1.TotalAssets,3, labels=['small', 'Medium', 'High'])
df1.head()

df1.loc[df1.MktCapSize == 'medium'].loc[df1.TtlAsstSize == 'small']

heatmap_data = df1.drop(columns= ['NumberEmployees', 'TrnsCount', 'TotalAssets', 'MarketCapitalization']).groupby(['MktCapSize','TtlAsstSize']).mean()
#heatmap_data = heatmap_data.fillna(0)
heatmap_data

heatmap_data = heatmap_data.unstack('TtlAsstSize')
heatmap_data

heatmap = sns.heatmap(heatmap_data)

