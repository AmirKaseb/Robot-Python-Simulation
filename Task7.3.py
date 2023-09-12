"""
This file contains the code for a robot controller.

The robot controller calculates the angular velocities of the two motors
and sets the PWM of the motors. It also updates the PID controller.
"""

import math
import time

from motor import Motor
from pid import PID


def get_angular_velocities(vx, vy, omega):
  """Returns the angular velocities of the two motors.

  Args:
    vx: The x-component of the robot's velocity.
    vy: The y-component of the robot's velocity.
    omega: The angular velocity of the robot.

  Returns:
    A tuple of the angular velocities of the two motors.
  """

  R = 20  # Wheel radius
  L = 100  # Distance between wheels

  w1 = (vx + vy) / R
  w2 = (vx - vy) / R

  return w1, w2


def drive_motor(motor, pwm):
  """Drives the motor at the given PWM.

  Args:
    motor: The motor to drive.
    pwm: The PWM to set.
  """

  motor.set_pwm(pwm)


def create_pid_controller(kp, ki, kd):
  """Creates a PID controller.

  Args:
    kp: The proportional gain.
    ki: The integral gain.
    kd: The derivative gain.

  Returns:
    A PID controller.
  """

  return PID(kp, ki, kd)


def main():
  # Create the motors.
  motor_1 = Motor(1)
  motor_2 = Motor(2)

  # Create the PID controller.
  pid_controller = create_pid_controller(1, 0, 0)

  # Set the target position.
  target_position = [100, 100]

  # Start the loop.
  while True:
    # Calculate the robot's velocity and angular velocity.
    vx, vy, omega = get_angular_velocities(target_position[0] - motor_1.position,
                                          target_position[1] - motor_2.position, 0)

    # Calculate the angular velocities of the two motors.
    w1, w2 = get_angular_velocities(vx, vy, omega)

    # Set the PWM of the motors.
    motor_1.set_pwm(w1)
    motor_2.set_pwm(w2)

    # Update the PID controller.
    pid_controller.update(motor_1.position, target_position[0])

    # Calculate the error.
    error = target_position[0] - motor_1.position

    # Print the error.
    print("Error = %f" % error)

    # Sleep for a second.
    time.sleep(1)
