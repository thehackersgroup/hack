# Motion analytics in the wild

## Challenge
Extract and classify distinct motion patterns from inertial data in order to track activity


## Method
Classify short and simple patterns in measured data into primitives, then use them to identify complex sequences of activities

### Measured data
* Three axes of acceleration
* Barometric pressure
* Three axes of rotation [not included in deliverable]
* Three axes of magnetic field [not included in deliverable]
* Heart rate  [not included in deliverable]

### Primitives
* Resting
* Movement
  * Walking
  * Running
* Elevator
  * Change in elevation
  * Starting
  * Stopping

### Algorithms used
* Detecting of elevator rides by step function detection on barometric pressure and measuring vertical distance travelled by measuring height in the step function.
* Detecting presence of activity by filtering for high variance in the total magnitude of acceleration.

### General pipeline
All constants are set and submodules are executed from RUN_ANALYSIS.PY (self-collected data) or RUN_CHALLENGE_ANALYSIS.PY (set challenges).

1. Load data from selected case (analyze_load.py / convert_to_csv.py, depending on format)
2. Execute analysis module(s) (analyze_baro.py for barometer, analyze_acc.py for acceleration)

### Machine learning  pipeline
We also have a machine learning pipeline set up for the classification of primitives: activity/no activity (activity_sklearn.py); elevator start/stop/neither (elevator_sklearn.py), generating input data for classifiers. However, we did not end up using it in lack of sufficient data to train these models and due the primitives being easily identifiable using simpler and more robust methods.

##Results
Please find the complete analysis pipeline in the dashboard as well as the solutions to the challenges


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

## Business_case
__Future classifiers__
*Posture: Lying, sitting, standing
*Vigor: Resting, light, middle, strong, extreme
*Motion type: Linear, rhythmic, rotational, erratic, stop-and-go
*3D pattern: Stationary, occasional jumps, constantly climbing, small or large height amplitudes (e.g. aided vs. unaided)
*Shocks: None, occasional, frequent (e.g. collisions between players, ball received, tennis stroke, soccer kick)

__B2C__
Integrate (pre-)classified motion patterns into a tech wearable, e.g. for
*healthcare (predictive and preventive care)
*sports and fitness (motion analysis, avoidable injuries)
*insurance (incentivized behavior)

__B2C__
Offer solutions for businesses, e.g.
*crowd management (e.g. transit flow, advertising spaces)
*smart cities / buildings

## Authors
* David Gugelmann dg2 [at] Gugelmann [dot] com 
* Maria Apostolaki apostolaki [dot] a [dot] maria [at] gmail [dot] com
* Edith Schmid edith [at] e [dot] chmid@gmail [dot] com
* Veronika Siska vs389 [at] cam [dot] ac [dot] uk
