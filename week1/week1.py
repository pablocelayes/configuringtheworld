import pandas as pd
import numpy as np

df=pd.read_excel('CtW 1 Size, wealth and poverty.xlsx')
df.index = df['Country ']

# Some comparisons
df.loc[['Argentina','Netherlands']]
df.loc[['Argentina','Finland']]
df.loc[['Argentina','Chile']]
df.loc[['Argentina','Cuba']]
df.loc[['Argentina','Mexico']]

# TODO: apply renames to other columns
df['HDI2012'] = df['Human Development Index (HDI) value 2012']

hdis = df.HDI2012
hdis[hdis == 'n/a'] = None
df.HDI2012 = hdis
df.sort(('HDI2012'))

hdis = hdis.copy()
hdis.sort(ascending=False)

# This is the part of the ranking that includes South America
hdis[:40]
