# Copyright 2019, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from machine import Pin, PWM
import time

# Pin D0 (AD0/DIO0)
START_BUTTON = "D0"
# Pin P0 (RSSI PWM/DIO10)
PWM_CHANNEL = "P0"

DUTY_CYCLE_MAX = 1023
DUTY_CYCLE_MIN = 0
DUTY_CYCLE_STEP = 25


print(" +----------------------------------------+")
print(" | XBee MicroPython PWM Duty Cycle Sample |")
print(" +----------------------------------------+\n")

current_duty_cycle = DUTY_CYCLE_MIN

# Set up the 'start button' object to check the input value. Configure the
# pin as input and enable the internal pull-up.
start_button = Pin(START_BUTTON, Pin.IN, Pin.PULL_UP)
# Instantiate the PWM object from the corresponding pin. Configure the
# initial duty cycle to the minimum value.
pwm_channel = PWM(PWM_CHANNEL, duty=current_duty_cycle)

while True:
    # Check if the start button is pressed. If so, start the duty cycle
    # sequence.
    if start_button.value() == 0:
        # Increase the duty cycle to the maximum value.
        while current_duty_cycle < DUTY_CYCLE_MAX:
            current_duty_cycle = current_duty_cycle + DUTY_CYCLE_STEP
            if current_duty_cycle > DUTY_CYCLE_MAX:
                current_duty_cycle = DUTY_CYCLE_MAX
            pwm_channel.duty(current_duty_cycle)
            time.sleep(0.1)

        # Keep at maximum 2 seconds.
        time.sleep(2)

        # Decrease the duty cycle to the minimum value.
        while current_duty_cycle > DUTY_CYCLE_MIN:
            current_duty_cycle = current_duty_cycle - DUTY_CYCLE_STEP
            if current_duty_cycle < DUTY_CYCLE_MIN:
                current_duty_cycle = DUTY_CYCLE_MIN
            pwm_channel.duty(current_duty_cycle)
            time.sleep(0.1)
    else:
        time.sleep(0.1)
