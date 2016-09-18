import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d

#def regularise_time(ts, xs):
#    t1 = np.arange(ts[0], ts[len(ts) - 1], 0.1)
#    x1 = np.interp(t1, ts, xs)
#
#    return(x1, t1)



t = df_accel.index - df_accel.index[0]
t = [_t.seconds+float(_t.microseconds)/1000000 for _t in t]
x = df_accel['x']
y = df_accel['y']
z = df_accel['z']

#(x, t) = regularise_time(t0, x0)
#(y, t) = regularise_time(t0, y0)
#(z, t) = regularise_time(t0, z0)

abs_val = []
for i in range(len(df_accel.index)):
    abs_val.append(x[i]*x[i] + y[i]*y[i] + z[i]*z[i])
    
df_accel['abs_val'] = abs_val

# some sample data
ts = pd.Series(abs_val, index=t)

#plot the time series
plt.figure(figsize=[20,10])
plt.subplot(2,1,1)
ts.plot(style='k--')

# calculate a 60 day rolling mean and plot
plt.subplot(2,1,2)
ts.rolling(DATA[DATASET]['rolling_std_width']).mean().plot(style='k')

# add the 20 day rolling variance:
rollingVar = ts.rolling(DATA[DATASET]['rolling_std_width']).std().fillna(method='backfill')
percentile_result = np.nanpercentile(rollingVar, DATA[DATASET]['percentile'])

itp = interp1d(rollingVar.index, rollingVar.values, kind='linear')
rollingVar_sg = savgol_filter(itp(rollingVar.index), DATA[DATASET]['accel_smoothing_window_size'], DATA[DATASET]['accel_smoothing_poly_order'])
is_above = rollingVar_sg > percentile_result
df_accel['is_activity'] = is_above

plt.figure(figsize=[23.5,10])
rollingVar.plot(style='b')
plt.plot(rollingVar.index, is_above, color = 'y')
plt.plot(rollingVar.index, rollingVar_sg, color = 'k')
plt.axhline(y=percentile_result, color = 'r')

df_accel[['is_activity']].plot(figsize=[24,10], grid=True)
ylim([0,1.1])
