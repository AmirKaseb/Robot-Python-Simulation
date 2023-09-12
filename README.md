# Robot Controller

This file contains the code for a robot controller. The robot controller calculates the angular velocities of the two motors and sets the PWM of the motors. It also updates the PID controller.

## Functions

* `get_angular_velocities()`: Returns the angular velocities of the two motors.
  * Arguments:
    * `vx`: The x-component of the robot's velocity.
    * `vy`: The y-component of the robot's velocity.
    * `omega`: The angular velocity of the robot.
  * Returns:
    * A tuple of the angular velocities of the two motors.
* `drive_motor()`: Drives the motor at the given PWM.
  * Arguments:
    * `motor`: The motor to drive.
    * `pwm`: The PWM to set which will be equal to RPM
* `create_pid_controller()`: Creates a PID controller.
  * Arguments:
    * `kp`: The proportional gain.
    * `ki`: The integral gain.
    * `kd`: The derivative gain.
  * Returns:
    * A PID controller.
* `main()`: The main function of the program.
  * Creates the motors and the PID controller.
  * Sets the target position.
  * Starts the loop, which calculates the angular velocities of the motors, sets the PWM of the motors, updates the PID controller, and prints the error.

## Usage

To use the robot controller, first create the motors and the PID controller. Then, set the target position. Finally, start the loop.

