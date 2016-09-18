from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.palettes import Viridis3, Viridis256
from bokeh.plotting import figure
from bokeh.models import Range1d, Label

# adapted from doc examples

output_file("dashboard/%s/1.html" % DATASET)

ax = [t.seconds for t in (df_accel.index - df_accel.index[0])]
ay0 = df_accel['x']
ay1 = df_accel['y']
ay2 = df_accel['z']
ay3 = df_accel['is_activity']

ap1 = figure(width=1200, plot_height=250, title='Acceleration - x')
ap1.line(ax, ay0, color=Viridis256[200])
ap1.set(x_range=Range1d(min(ax), max(ax)))

ap2 = figure(width=1200, height=250, title='Acceleration - y')
ap2.line(ax, ay1, color=Viridis3[1])
ap2.set(x_range=Range1d(min(ax), max(ax)))

ap3 = figure(width=1200, height=250, title='Acceleration - z')
ap3.line(ax, ay2, color=Viridis3[2])
ap3.set(x_range=Range1d(min(ax), max(ax)))

grid = gridplot([[ap1], [ap2], [ap3]])
show(grid)



output_file("dashboard/%s/2.html" % DATASET)

x = [t.seconds for t in (df_baro.index - df_baro.index[0])]
y0 = df_baro['alt']
y1 = [(1.0 *_y / 4) for _y in df_baro['alt_steps_height']]
y2 = df_baro['alt_steps']

p1 = figure(width=1200, plot_height=250, title='Relative altitude (from barometer)')
p1.line(x, y0, color=Viridis256[200])
p1.set(x_range=Range1d(min(x), max(x)))

p2 = figure(width=1200, height=250, title='Vertical movement patterns')
p2.circle(x, [_y2 if _y2 != 0 else NaN for _y2 in y2], color=Viridis256[2], size=30)
p2.set(x_range=Range1d(min(x), max(x)))

p3 = figure(width=1200, height=250, title='Approximated number of changed floors')
p3.line(x, y1, color=Viridis3[1])
p3.set(x_range=Range1d(min(x), max(x)))

grid = gridplot([[p1], [p2], [p3]])
show(grid)


output_file("dashboard/%s/summary.html" % DATASET)

sap4 = figure(width=1200, height=250, title='Identified physical acctivity (running, walking, ...)')
sap4.circle(ax, [_y if _y == 1 else NaN for _y in ay3], color=Viridis3[0], size=30)
sap4.set(x_range=Range1d(min(ax), max(ax)))

sp2 = figure(width=1200, height=250, title='Vertical movement patterns')
sp2.circle(x, [_y2 if _y2 != 0 else NaN for _y2 in y2], color=Viridis3[1], size=30)
sp2.set(x_range=Range1d(min(x), max(x)))

sp3 = figure(width=1200, height=250, title='Approximated number of changed floors')
sp3.line(x, y1, color=Viridis256[200])
sp3.set(x_range=Range1d(min(x), max(x)))

for i, p in enumerate(sorted(history)):
    if 'dir' not in history[p] and history[p]['active']==True and history[p]['duration']>1:
        txt = '%s Ms X started moving' % p
    elif 'dir' not in history[p] and history[p]['active']==False :
        txt = '%s Ms X sits' % p
    elif 'dir' in history[p] :
        txt = '%s Ms X is using the elevator to go %s' % (p, history[p]['dir'])
    print txt
    y = -30 -i * 30

    label = Label(x=30, y=y, x_units='screen', y_units='screen',
                 text=txt, render_mode='css', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0, angle=0)

    sp3.add_layout(label)

grid = gridplot([[sap4], [sp2], [sp3]])

show(grid)
