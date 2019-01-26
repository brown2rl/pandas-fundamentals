#types:
 ##raw data
np.array
np.ndarray
 ##row labels (custom list indicies).. pretty print .index object
pd.Series
 ##column labels
pd.DataFrame

#data sources:

text - csv (delimeter agnostic), json, html tables
binary - data interchange b/w excel, SAS, etc
relational DBs - sql, etc

#useful methods:

pd.DataFrame.from_*
df.loc[]
df.iloc[]
