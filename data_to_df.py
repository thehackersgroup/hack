import pandas as pd
import glob, os

_dfs=[]
for file in glob.glob("%s/*.Barometer" % DATASET):
    print file
    _dfs.append(pd.read_json(file))

df_baro = pd.concat(_dfs, axis=0)
df_baro.columns = [u'date', u'pressure', u'alt', u'type']
df_baro.index = df_baro['date']
df_baro.sort_index(inplace=True)

try:
    # filtering
    print 'before filtering'
    print 'df_baro: from:', df_baro.index[0]
    print 'df_baro: to:', df_baro.index[-1]
    df_baro = df_baro[df_baro.index >= DATA[DATASET]['start']]
    df_baro = df_baro[df_baro.index <= DATA[DATASET]['end']]
    print 'after filtering'
    print 'df_baro: from:', df_baro.index[0]
    print 'df_baro: to:', df_baro.index[-1]
except KeyError:
    pass


_dfs=[]
for file in glob.glob("%s/*.Accelerometer" % DATASET):
    print file
    _dfs.append(pd.read_json(file))

df_accel = pd.concat(_dfs, axis=0)
df_accel.index = df_accel['date']
df_accel.sort_index(inplace=True)

try:
    # filtering
    print 'before filtering'
    print 'df_accel: from:', df_accel.index[0]
    print 'df_accel: to:', df_accel.index[-1]
    df_accel = df_accel[df_accel.index >= DATA[DATASET]['start']]
    df_accel = df_accel[df_accel.index <= DATA[DATASET]['end']]
    print 'after filtering'
    print 'df_accel: from:', df_accel.index[0]
    print 'df_accel: to:', df_accel.index[-1]
except KeyError:
    pass





#df={}
#i=0
#for file in glob.glob("%s/*.Accelerometer" % DATASET):
	#print file
	#df[i] = pd.read_json(file)
	#i=i+1

#vertical_stack= df[0]

#for i in range(1, len(df)):
  #vertical_stack = pd.concat([vertical_stack,df[i]], axis=0)

#df_accel=vertical_stack.copy()
