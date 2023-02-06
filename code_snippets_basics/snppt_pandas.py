#%%
"""### Pandas"""

# Pandas: Create a TimeDelta from a string
import pandas as pd

pd.Timedelta('2 days 2 hours 15 minutes 30 seconds')



#%%
# Pandas: Replace NaN values in a Column
import numpy as np
import pandas as pd
df = pd.DataFrame({
  'dogs': [5, 10, np.nan, 7],
})

df['dogs'].replace(np.nan, 0, regex=True)



#%%
# Pandas: Describe Timestamp values in a column
import pandas as pd
df = pd.DataFrame({
  'time': ['2022-09-14 00:52:00-07:00', '2022-09-14 00:52:30-07:00', 
           '2022-09-14 01:52:30-07:00'],
  'letter': ['A', 'B', 'C'],
})
df['time'] = pd.to_datetime(df.time)

df['time'].describe(datetime_is_numeric=True)


#%%
# Pandas: Create a TimeDelta using `unit`
import pandas as pd

pd.to_timedelta(1, unit='h')



#%%
# Pandas: Create a TimeDelta using available kwargs
import pandas as pd

pd.Timedelta(days=2)



#%%
"""### Pandas Timestamp"""

# Pandas Timestamp: Convert string to Timestamp
import pandas as pd

pd.Timestamp('9/27/22 06:59').tz_localize('US/Pacific')



#%%
# Pandas Timestamp: Convert string to Timestamp, using date only
import pandas as pd

pd.Timestamp('9/27/22').tz_localize('US/Pacific')



#%%
"""### Pandas DataFrame"""

# Pandas DataFrame: Intersect Indexes
import pandas as pd
terminator_df = pd.DataFrame({
  'first_name': ['Sarah', 'John', 'Kyle'],
  'last_name': ['Connor', 'Connor', 'Reese'],
})
terminator_df.set_index('first_name', inplace=True)

buckaroo_df = pd.DataFrame({
  'first_name': ['John', 'John', 'Buckaroo'],
  'last_name': ['Parker', 'Whorfin', 'Banzai'],
})
buckaroo_df.set_index('first_name', inplace=True)

terminator_df.index.intersection(buckaroo_df.index).shape



#%%
# Pandas DataFrame: Rename multiple Columns
import pandas as pd
df = pd.DataFrame({
    'Year': [2016, 2015, 2014, 2013, 2012],
    'Top Animal': ['Giant panda', 'Chicken', 'Pig', 'Turkey', 'Dog']
})

df.rename(columns={
    'Year': 'Calendar Year', 
    'Top Animal': 'Favorite Animal', 
}, inplace=True)
df



#%%
# Pandas DataFrame: Ignore one Column
import pandas as pd
df = pd.DataFrame({
  'first_name': ['Sarah', 'John', 'Kyle', 'Joe'],
  'last_name': ['Connor', 'Connor', 'Reese', 'Bonnot'],
})

df.loc[:, df.columns!='last_name']



#%%
# Pandas DataFrame: Drop duplicate rows
import pandas as pd
df = pd.DataFrame({
  'first_name': ['Sarah', 'John', 'Kyle', 'Joe'],
  'last_name': ['Connor', 'Connor', 'Reese', 'Bonnot'],
})
df.set_index('last_name', inplace=True)
df.loc[~df.index.duplicated(), :]



#%%
# Pandas DataFrame: Create from lists of values
import pandas as pd

last_names = ['Connor', 'Connor', 'Reese']
first_names = ['Sarah', 'John', 'Kyle']
df = pd.DataFrame({
  'first_name': first_names,
  'last_name': last_names,
})
df



#%%
# Pandas DataFrame: Query by variable value
import pandas as pd
df = pd.DataFrame({
  'first_name': ['Sarah', 'John', 'Kyle'],
  'last_name': ['Connor', 'Connor', 'Reese'],
})

foo = 'Connor'
df.query('last_name == @foo')



#%%
# Pandas DataFrame: Query by regexp (regular expression)
import pandas as pd
df = pd.DataFrame({
  'first_name': ['Sarah', 'John', 'Kyle', 'Joe'],
  'last_name': ['Connor', 'Connor', 'Reese', 'Bonnot'],
})

df[df.last_name.str.match('.*onno.*')]



#%%
# Pandas DataFrame: Query by Timestamp above a value
import pandas as pd
df = pd.DataFrame({
  'time': ['2022-09-14 00:52:00-07:00', '2022-09-14 00:52:30-07:00', 
           '2022-09-14 01:52:30-07:00'],
  'letter': ['A', 'B', 'C'],
})
df['time'] = pd.to_datetime(df.time)

df.query('time >= "2022-09-14 00:52:30-07:00"')



#%%
# Pandas DataFrame: Sort the count of rows grouped on columns
import pandas as pd
df = pd.DataFrame({
  'first_name': ['Sarah', 'John', 'Kyle'],
  'last_name': ['Connor', 'Connor', 'Reese'],
})

df.groupby(['last_name']).size().sort_values(ascending=False)



#%%
# Pandas DataFrame: Select all rows from A that are not in B, using the index
import pandas as pd
terminator_df = pd.DataFrame({
  'first_name': ['Sarah', 'John', 'Kyle'],
  'last_name': ['Connor', 'Connor', 'Reese'],
})
terminator_df.set_index('first_name', inplace=True)

buckaroo_df = pd.DataFrame({
  'first_name': ['John', 'John', 'Buckaroo'],
  'last_name': ['Parker', 'Whorfin', 'Banzai'],
})
buckaroo_df.set_index('first_name', inplace=True)

terminator_df[~terminator_df.index.isin(buckaroo_df.index)]



#%%
# Pandas DataFrame: Filter by Timestamp in DatetimeIndex using `.loc[]`
import pandas as pd
df = pd.DataFrame({
  'time': ['2022-09-14 00:52:00-07:00', '2022-09-14 00:52:30-07:00', 
           '2022-09-14 01:52:30-07:00'],
  'letter': ['A', 'B', 'C'],
})
df['time'] = pd.to_datetime(df.time)
df.set_index('time', inplace=True)

df.loc['2022-09-14':'2022-09-14 00:53']



#%%
# Pandas DataFrame: Query for Timestamp between two values
import pandas as pd
df = pd.DataFrame({
  'time': ['2022-09-14 00:52:00-07:00', '2022-09-14 00:52:30-07:00', 
           '2022-09-14 01:52:30-07:00'],
  'letter': ['A', 'B', 'C'],
})
df['time'] = pd.to_datetime(df.time)

begin_ts = '2022-09-14 00:52:00-07:00'
end_ts = '2022-09-14 00:54:00-07:00'

df.query('@begin_ts <= time < @end_ts')



#%%
# Pandas DataFrame: Extract values using regexp (regular expression)
import pandas as pd
df = pd.DataFrame({
  'request': ['GET /index.html?baz=3', 'GET /foo.html?bar=1'],
})

df['request'].str.extract('GET /([^?]+)\?', expand=True)



#%%
# Pandas DataFrame: Filter by Timestamp using TimeDelta string
import pandas as pd
df = pd.DataFrame({
  'time': ['2022-09-14 00:52:00-07:00', '2022-09-14 00:52:30-07:00', 
           '2022-09-14 01:52:30-07:00'],
  'letter': ['A', 'B', 'C'],
})
df['time'] = pd.to_datetime(df.time)

def rows_in_time_range(df, time_column, start_ts_str, timedelta_str):
  # Return rows from df, where start_ts < time_column <= start_ts + delta.
  # start_ts_str can be a date '2022-09-01' or a time '2022-09-14 00:52:00-07:00'
  # timedelta_str examples: '2 minutes'  '2 days 2 hours 15 minutes 30 seconds'
  start_ts = pd.Timestamp(start_ts_str).tz_localize('US/Pacific')
  end_ts = start_ts + pd.to_timedelta(timedelta_str)
  return df.query("@start_ts <= {0} < @end_ts".format(time_column))

rows_in_time_range(df, 'time', '2022-09-14 00:00', '52 minutes 31 seconds')



#%%
# Pandas DataFrame: Select rows by an attribute of a column value
import pandas as pd
df = pd.DataFrame({
  'first_name': ['Sarah', 'John', 'Kyle'],
  'last_name': ['Connor', 'Connor', 'Reese'],
})

df[df['last_name'].map(len) == 5]



#%%
# Pandas: DataFrames: Group Timeseries by Frequency
import pandas as pd
df = pd.DataFrame({
  'time': ['2022-09-01 00:00:01-07:00', '2022-09-01 00:00:02-07:00', 
           '2022-09-01 00:01:00-07:00', '2022-09-01 00:02:00-07:00',
           '2022-09-01 00:03:00-07:00', '2022-09-01 00:04:00-07:00',
           '2022-09-01 00:05:00-07:00', '2022-09-01 00:07:00-07:00'], 
  'requests': [1, 1, 1, 1, 1, 1, 1, 1],
})
df['time'] = pd.to_datetime(df.time)

df.groupby(pd.Grouper(key='time', freq='2min')).sum()



#%%
# Pandas DataFrame: Query using variable value as a column name
import pandas as pd
df = pd.DataFrame(data={
  'first_name': ['Sarah', 'John', 'Kyle'],
  'last_name': ['Connor', 'Connor', 'Reese'],
})

column_name = 'first_name'
df.query(f"`{column_name}` == 'John'")



#%%
# Pandas DataFrame: Explode a column containing dictionary values into multiple columns
import pandas as pd
df = pd.DataFrame({
  'date': ['2022-09-14', '2022-09-15', '2022-09-16'],
  'letter': ['A', 'B', 'C'],
  'dict' : [{ 'fruit': 'apple', 'weather': 'aces'},
            { 'fruit': 'banana', 'weather': 'bad'},
            { 'fruit': 'cantaloupe', 'weather': 'cloudy'}],
})

pd.concat([df.drop(['dict'], axis=1), df['dict'].apply(pd.Series)], axis=1)



#%%
# Pandas DataFrame: Reshape to have 1 row per value in a list column
import pandas as pd
df = pd.DataFrame({
  'date': ['9/1/22', '9/2/22', '9/3/22'],
  'action': ['Add', 'Update', 'Delete'],
  'msg_ids': [[1, 2, 3], [], [2, 3]],
})
df.set_index('date', inplace=True)
  
  
temp_series = df['msg_ids'].apply(pd.Series, 1).stack()
temp_series.index = temp_series.index.droplevel(-1)
temp_series.name = 'msg_id'
new_df = temp_series.to_frame()
new_df.set_index('msg_id', inplace=True)
new_df.loc[~new_df.index.duplicated(), :] # Drop duplicates.