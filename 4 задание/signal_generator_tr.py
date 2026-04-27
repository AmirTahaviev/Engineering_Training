import numpy as np
import time
def get_tr_amplitude(freq, time):
    value = (2/np.pi) * np.arcsin(np.sin(2*np.pi*freq*time))
    return (value + 1) / 2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1.0 / sampling_frequency)