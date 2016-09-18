fig = matplotlib.pyplot.figure(figsize=[24,24])
fig.add_subplot(2,1,1)

df_baro[['alt_steps', 'alt', 'alt_steps_height']].plot(ax=gca()) # alt_steps_height

plot(df_baro.index, -10 * ones(len(df_baro.index)), 'x', label='measurements')

if DATA[DATASET]['plot_gt']:
    gt = pd.read_json(glob.glob("%s/*.json" % DATASET)[0])
    plot(gt[['start_time']], -12 * ones(len(gt.index)), 'x', label='start of events')
    plot(gt[['end_time']], -12 * ones(len(gt.index)), 'o', label='end of events')
legend()

fig.add_subplot(2,1,2)
df_accel[['x', 'y', 'z', 'is_activity']].plot(ax=gca())

plt.show()
