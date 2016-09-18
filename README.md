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
__getting_in_and_out__

1. Getting in
2. Riding the elevator up
3. Getting out
4. Getting in
5. Riding the elevator down
6. Getting out
7. Getting in
8. Riding the elevator down
9. Getting out

__walk_and_ride__

1. Sitting
2. Walking
3. Riding the elevator down
4. Walking

### Sequence 2

__elevator_up_and_stairs_down__

1. Walking to the elevator
2. Taking the elevator
3. Walking stairs down
4. Walking back

__riding_the_elevator_is_fun__

1. Walking to the elevator
2. Entering/exiting/riding the elevator many times
3. Walking back to the seat
4. Sitting

### Sequence 3

__stairway_workout__

1. Walking up the stairs
2. 2-stepping up the stairwell
3. Walking towards elevators and waiting
4. Riding the elevator down
5. Walking back to seat

__escalator_fun__

1. Riding up escalator
2. Walking
3. Riding down escalator

## Authors
* David Gugelmann
* Maria Apostolaki
* Edith Schmid
* Veronika Siska
