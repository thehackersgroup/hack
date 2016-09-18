#!/usr/bin/env python
a=df_baro.to_dict(orient='records')
b=df_accel.to_dict(orient='records')

history={}

for rec in a: 
	if rec['alt_steps']==1.0:
		history[rec['date']]   = {'height': abs(rec['alt_steps_height']),'dir': 'up'}
	elif rec['alt_steps']==-1.0:
		history[rec['date']] =  {'height': abs(rec['alt_steps_height']) ,'dir': 'down'}

start_state=None
start_date=None
for rec in b:
	if start_state!=rec['is_activity']:
		start_state=rec['is_activity']
		
		if not rec['date'] in history:
			history[rec['date']]={'active':rec['is_activity']}
		if start_state and start_date:
			history[rec['date']]['duration']=(rec['date']- start_date).seconds
		else:
			history[rec['date']]['duration']=0
		start_date=rec['date']




for p in sorted(history):
	if 'dir' not in history[p] and history[p]['active']==True and history[p]['duration']>1:
		print p, ': Ms X is started moving'
	elif 'dir' not in history[p] and history[p]['active']==False :
		print p, ': Ms X sits'
	elif 'dir' in history[p] :
		print p, ': Ms X using the elevator to go ', history[p]['dir']