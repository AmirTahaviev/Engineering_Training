import pwm_dac as pw
import signal_generator_tr as sg
import time
t = 0
amplitude = 5
signal_frequency = 20
sampling_frequency = 100

try:
    pwm = pw.PWM_DAC(12, 500, 5, True)

    while True:
        a = sg.get_tr_amplitude(signal_frequency, t)
        voltage = a * amplitude
        pwm.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t = t + 1.0 / sampling_frequency 
finally:
    pwm.deinit()