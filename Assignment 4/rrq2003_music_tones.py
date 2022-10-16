"""
This module takes the notes of a given song and shifts each note by
multiplying by 2 ^ 1/2 for each frequency

Submitted by Reyhan Quayum, rrq2003
"""

def transposer(song):
    transposed_tones = list()
    semitones = list(input("Give a list of the notes of the song")
    for note in semitones:
        shifted_note = note * (2 ** 0.5)
        transposed_tones.append(shifted_note)
    return transposed_tones
