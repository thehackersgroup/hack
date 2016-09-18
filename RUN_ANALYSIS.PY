#!/usr/bin/env python

import glob
from collections import OrderedDict
execfile('helpers.py')

OUT_DIR = '.'

DATA = OrderedDict()
DATA['sensor-reading'] = {'detect_step_width': 10, 'plot_gt': False, 'rolling_std_width': 50, 'ignore_gap_width': 20, 'percentile': 60, 'accel_smoothing_window_size': 25, 'accel_smoothing_poly_order' : 3}

for DATASET in DATA:

    print '### %s ###' % DATASET
    
    execfile('convert_to_csv.py')
    convert(DATASET + '.json', DATASET)

    execfile('analyze_load.py')
    
    execfile('analyze_baro.py')

    execfile('visualise.py')

    execfile('plot.py')