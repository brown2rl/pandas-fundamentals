# -*- coding: utf-8 -*-
import pandas as pd
import os

# Let's load the data for the first time
df = pd.read_pickle(os.path.join('..', 'data_frame.pickle'))

# count number of unique artists
artists = df['artist']
pd.unique(artists)
len(pd.unique(artists))

# count number of works by an artist
s = df['artist'] == 'Bacon, Francis' # return bool
s.value_counts()
 
    # Other way
artist_counts = df['artist'].value_counts()
artist_counts['Bacon, Francis']

# indexing
df.loc[1035, 'artist'] # using labels in the index object [row indexer, col]
df.iloc[0, 0] # indexing by position
df.iloc[0, :] # first row, all columns
df.iloc[0:2, 0:2] # row range, col range

## Find largest artwork
# df['height'] * df['width'] - error b/c of missing & string values
df['width'].sort_values().head() # inspecting
df['width'].sort_values().tail()

# Try to convert values to numbers
# pd.to_numeric(df['width']) - error converting strings to numbers

# Force NaNs 
pd.to_numeric(df['width'], errors='coerce') # force width column values to NaN on error
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce') # replacing old width col with new

pd.to_numeric(df['height'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'],
                                    errors='coerce')

df['height'] * df['width'] # works w/ new col
df['units'].value_counts() # shows all units

# create new column 'area' with sizes
area = df['height'] * df['width']
df = df.assign(area=area)

df['area'].max() # just max val
df['area'].idxmax() # returns index w/ max vals
df.loc[df['area'].idxmax(), :] # returns information
