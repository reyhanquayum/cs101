"""Template script to make WAV files


This script creates a simple WAV file that produces MOVING tones
at predetermined frequencies. It runs for a user-defined number of
seconds and executes a while loop that concatenates to sound_binary until a
specified number of samples has been reached. Each sample has a calculated
intensity based on amplitude and frequency. Each sample also has a right
and left channel that is multiplied by a changing factor that
creates a 'moving' effect from the right channel to the left channel.

Prepared by
Mauricio Arias
Submitted by
Reyhan Quayum, NetID rrq2003
"""

import math
from lib.WAV_utilities import *  # this file is expected in the lib folder

filename = "alternating_tones.wav"
sound_file = open(filename, 'wb')

# Parameters for the sounds
freq1_in_Hz = A_freq * 2
freq2_in_Hz = A_freq
channels = 1
samples_per_s = 8000  # 44100 is CD quality, 6600 ~ old phone landlines
time_between_samples = 1 / samples_per_s

# TODO: ask the user for the duration. It should be between 1 and 20 seconds.
correctinput = False
while correctinput == False:
    duration = int(input("Enter a duration (should be between 1 and 20 seconds)."))
    if duration <= 20 or duration >= 1:
        duration_in_s = duration
        correctinput = True
    else:
        continue


# sample_depth is defined in WAV_utilities.

# Header with information about the size of the file and its format.
sound_binary = header(duration_in_s, samples_per_s, channels)
print()

# TODO: write the code to fill the data section in the space below.
# Sound information is generated as a function of time. Notice also
# that the sound is encoded as signed numbers using 
# bytes_pack_signed() from the library WAV_utilities.py.

time_elapsed = 0
sample_number = 0
total_samples = 8000*duration_in_s
while sample_number < total_samples:
    #  alternates frequency every .25 seconds
    freq = freq1_in_Hz if (time_elapsed // .25) % 2 == 0 else freq2_in_Hz 
    sample = int(max_amplitude / 10 * math.sin(2*math.pi*freq*time_elapsed))
    encoded_sample = bytes_pack_signed(sample, sample_depth // 8)
    sound_binary += encoded_sample
    sample_number += 1
    time_elapsed += time_between_samples












# Do not edit after this point
print(f"File Size is {len(sound_binary)}")
sound_file.write(sound_binary)
sound_file.close()
print(f"{filename} WAV file was generated...")
