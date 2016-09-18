#!/usr/bin/env python

import pandas

df_accel = pandas.DataFrame.from_csv(DATASET + '-accel.csv')
df_baro = pandas.DataFrame.from_csv(DATASET + '-baro.csv')

print 'df_accel'
print df_accel.describe()

print 'df_baro'
print df_baro.describe()
