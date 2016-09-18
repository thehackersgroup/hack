from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.palettes import Viridis3, Viridis256
from bokeh.plotting import figure
from bokeh.models import Range1d

# adapted from doc examples

output_file("1.html")

ax = [t.seconds for t in (df_accel.index - df_accel.index[0])]
ay0 = df_accel['x']
ay1 = df_accel['y']
ay2 = df_accel['z']
ay3 = df_accel['is_activity']

ap1 = figure(width=1200, plot_height=250, title='x')
ap1.line(ax, ay0, color=Viridis256[200])
ap1.set(x_range=Range1d(min(ax), max(ax)))

ap2 = figure(width=1200, height=250, title='y')
ap2.line(ax, ay1, color=Viridis3[1])
ap2.set(x_range=Range1d(min(ax), max(ax)))

ap3 = figure(width=1200, height=250, title='z')
ap3.line(ax, ay2, color=Viridis3[2])
ap3.set(x_range=Range1d(min(ax), max(ax)))

ap4 = figure(width=1200, height=250, title='Physical acctivity (running, walking, ...)')
ap4.circle(ax, [_y if _y == 1 else NaN for _y in ay3], color=Viridis256[2], size=30)
ap4.set(x_range=Range1d(min(ax), max(ax)))

grid = gridplot([[ap1], [ap2], [ap3], [ap4]])
show(grid)



output_file("2.html")

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





output_file("3.html")

sap4 = figure(width=1200, height=250, title='Physical acctivity (running, walking, ...)')
sap4.circle(ax, [_y if _y == 1 else NaN for _y in ay3], color=Viridis3[0], size=30)
sap4.set(x_range=Range1d(min(ax), max(ax)))

sp2 = figure(width=1200, height=250, title='Vertical movement patterns')
sp2.circle(x, [_y2 if _y2 != 0 else NaN for _y2 in y2], color=Viridis3[1], size=30)
sp2.set(x_range=Range1d(min(x), max(x)))

sp3 = figure(width=1200, height=250, title='Approximated number of changed floors')
sp3.line(x, y1, color=Viridis256[200])
sp3.set(x_range=Range1d(min(x), max(x)))


grid = gridplot([[sap4], [sp2], [sp3]])
show(grid)
