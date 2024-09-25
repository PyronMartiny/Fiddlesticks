import numpy as np
import scipy.io.wavfile as wav
import os
import sounddevice as sd

index = 0.0
index_increment = None
wave_table = None
wavetable_length = 1000


def interpolate_linearly(wave_table, index):
	truncated_index = int(np.floor(index))
	next_index = (truncated_index + 1) % wave_table.shape[0]

	next_index_weight = index - truncated_index
	truncated_index_weight = 1 - next_index_weight

	return truncated_index_weight * wave_table[truncated_index] + next_index_weight * wave_table[next_index]

def audio_callback(outdata, frames, time, status):
	if status:
		print(status)

	global index
	for i in range(frames):
		outdata[i] = interpolate_linearly(wave_table, index)
		index += index_increment[i]
		index %= wavetable_length

def main():
	global index, index_increment, wave_table
	sample_rate = 44100
	start_frequency = 300
	end_frequency = 3000

	t = 3
	waveform = np.sin
	wave_table = np.zeros((wavetable_length,))
	for n in range(wavetable_length,):
		wave_table[n] = waveform(2 * np.pi * n/ wavetable_length)

	index = 0.0
	
	frequencies = np.linspace(start_frequency, end_frequency, int(sample_rate * t))
	index_increment = (frequencies * wavetable_length / sample_rate)

	for n in range(wavetable_length):
	
		wave_table[n] = waveform(2 * np.pi * n / wavetable_length)
	

	with sd.OutputStream(samplerate=sample_rate, channels=1, callback=audio_callback):
		print('Uhnts!')
		sd.sleep(int(t * 1000))

if __name__ == '__main__':
	main()