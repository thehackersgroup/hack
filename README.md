# When Crowd Meets Elevators

## Challenge
Make use of sensor data from phones to infer activity patterns

## Method
Classify short and simple patterns in measured data into primitives, then use them to identify complex sequences of activities

### Data
* Three axes of acceleration
* Barometric pressure
* Three axes of rotation [not yet used]
* Three axes of magnetic field [not yet used]
* __Heart rate [not yet used]__

### Primitives
* Resting
* Movement
  * Walking
  * Running
* Elavator
  * Change in elavation
  * Starting
  * Stopping

### Machine learning  pipeline
We also have a machine learning pipeline set up for the classification of primitives: activity/no activity; elevator start/stop/neither. However, we did not end up using it in lack of data.

## Case sequences
### Sequence 1
getting_in_and_out
1. Getting in
2. Riding the elevator up
3. Getting out
4. Getting in
5. Riding the elevator down
6. Getting out
7. Getting in
8. Riding the elevator down
9. Getting out

walk_and_ride
1. Sitting
2. Walking
3. Riding the elevator down
4. Walking

### Sequence 2



## Authors
* David Gugelmann
* Maria Apostolaki
* Edith Schmid
* Veronika Siska
