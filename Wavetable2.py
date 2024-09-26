import numpy as np
import matplotlib.pyplot as plot
import sounddevice as sd
import time
from scipy.signal import sawtooth

sample_rate = 96000
frequency = 2000 #Hz
duration = 0.3 # Seconds
wavetable_length = sample_rate
toggle = True

def sawtooth1(frequency):
	wavetable1 = np.arange(0, duration, 1/ wavetable_length)
	#Print List
	print(f'These are the wavetable time divisions: {wavetable1}')

	#create random phase variable
	random_phase = np.random.uniform(0, 2 * np.pi)

	#sample the sine wave
	# wave_discreet = np.sin(2 * np.pi * frequency* wavetable + random_phase)
	wave_discreet = sawtooth(2 * np.pi * frequency* wavetable1 + random_phase)

	#scake the sine wave
	wave_discreet_scaled = wave_discreet * 32767

	#convert to integer values
	wave_discreet_int = np.round(wave_discreet_scaled).astype(np.int16)
	#Print List
	print(f'\nThese are the integer values of sine function that are placed into the array of time divisions: {wave_discreet_int}')

	# plot.figure(figsize=(19, 4)) # set size of figures
	# plot.plot(wavetable, wave_discreet_scaled, 'o', markersize=2, label='Sample Points')
	# plot.plot(wavetable, wave_discreet_int) # used to show points
	# plot.title('Sine Wave Plot') #self explanatory
	# plot.xlabel('Seconds') # self explanatory
	# plot.ylabel('Amplitude') #self explanatory
	# plot.ylim(-67000, 67000) # axis limits
	# plot.axhline(0, color="black", linewidth=0.5, linestyle="--")
	# plot.grid(True) # shows a grid
	# plot.show() # displays the plot
	# plot.legend()

	sd.play(wave_discreet_int, samplerate=sample_rate)
	sd.wait()
	
while True:
	sawtooth1(frequency)
	frequency -= 100

	if frequency < 15:
		frequency = 2000
	
