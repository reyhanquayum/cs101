"""
This script plays a song  by calculating the number of samples per given note where each note is given in a list
along with the duration of each note for a song.

Submitted by Reyhan Quayum, rrq2003
"""

import lib.WAV_utilities_v2 as utilities
import songs as songs
import math

filename = "rrq2003_song.wav"
sound_file = open(filename, 'wb')

total_duration = 0
time_elapsed = 0
sample_number = 0
channels = 1
samples_per_s = 8000  # 44100 is CD quality, 6600 ~ old phone landlines
time_between_samples = 1 / samples_per_s
for i in songs.Frere_Jacques_durations:  # calculate duration of song
    duration = i
    total_duration = total_duration + duration
total_samples = 8000*total_duration
# Header with information about the size of the file and its format.
sound_binary = utilities.header(total_duration, samples_per_s, channels)
print()

for note in songs.Frere_Jacques_notes:
    freq = note
    note_duration = songs.Frere_Jacques_durations[songs.Frere_Jacques_notes.index(note)]
    samples_per_note = samples_per_s / note_duration
    while sample_number < samples_per_note:
        sample = int(utilities.max_amplitude / 10 * math.sin(2 * math.pi * freq * time_elapsed))
        encoded_sample = utilities.bytes_pack_signed(sample, utilities.sample_depth // 8)
        sound_binary += encoded_sample
        sample_number += 1
        time_elapsed += time_between_samples
        if sample_number == samples_per_note or sample_number > samples_per_note:
            sample_number = 0  # reset sample number to 0 when note has been completed
            break


print(f"File Size is {len(sound_binary)}")
sound_file.write(sound_binary)
sound_file.close()
print(f"{filename} WAV file was generated...")