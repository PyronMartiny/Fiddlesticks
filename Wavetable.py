import numpy as np
import matplotlib.pyplot as plot


sample_rate = 44100
frequency = 100 #Hz
duration = 1 # Seconds
wavetable_length = sample_rate


#create wavetable list

wavetable = np.arange(0, duration, 1/wavetable_length)
print(f'These are the wavetable time divisions: {wavetable}')

#sample the sine wave
wave_discreet = np.sin(2 * np.pi * frequency* wavetable)

#scake the sine wave
wave_discreet_scaled = wave_discreet * 127

#convert to integer values
wave_discreet_int = np.round(wave_discreet_scaled).astype(int)
print(f'\nThese are the integer values of sine function that are placed into the array of time divisions: {wave_discreet_int}')


plot.figure(figsize=(19, 4)) # set size of figures
plot.plot(wavetable, wave_discreet_scaled, 'o', markersize=2, label='Sample Points')
plot.plot(wavetable, wave_discreet_int) # used to show points
plot.title('Sine Wave Plot') #self explanatory
plot.xlabel('Seconds') # self explanatory
plot.ylabel('Amplitude') #self explanatory
plot.ylim(-130, 130) # axis limits
plot.axhline(0, color="black", linewidth=0.5, linestyle="--")
plot.grid(True) # shows a grid
plot.show() # displays the plot
plot.legend()
