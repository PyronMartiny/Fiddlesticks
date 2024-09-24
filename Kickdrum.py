import pygame as pg
import numpy as np

# Initialize Pygame
pg.init()
pg.mixer.init()

# Parameters
sampling_rate = 44100
duration = 0.02  # Duration of each note in seconds
bpm = 50  # Beats per minute
steps = 16  # Number of steps
step_duration = 60 / bpm / 4  # Duration of each step in seconds

# Function to generate a sine wave buffer
def generate_sine_wave_buffer(frequency, buffer_size):
    t = np.linspace(0, buffer_size / sampling_rate, buffer_size, endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sound = np.asarray([32767 * wave, 32767 * wave]).T.astype(np.int16)
    return sound.copy(order='C')

# Initialize variables
running = True
frequency = 440.0  # A4
sequence = [0] * steps  # 16 steps (0 = off, 1 = on)
current_step = 0
last_tick = pg.time.get_ticks()

# Set up the display
width, height = 400, 300
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Step Sequencer")

# Create a sound object for the sine wave
sound_buffer = generate_sine_wave_buffer(frequency, int(step_duration * sampling_rate))
sound = pg.sndarray.make_sound(sound_buffer)

# Add a flag to track sound state
is_playing = False

while running:
    current_time = pg.time.get_ticks()

    # Check if the current step is active and play sound if not already playing
    if sequence[current_step] == 1 and not is_playing:
        sound.play()
        is_playing = True
    elif sequence[current_step] == 0:
        is_playing = False  # Reset when the step is off

    # Move to the next step
    if current_time - last_tick >= step_duration * 1000:
        current_step = (current_step + 1) % steps
        last_tick = current_time

    # Rest of the drawing and event handling code...


    screen.fill((255, 255, 255))  # Clear the screen

    # Draw the sequencer
    for i in range(steps):
        color = (0, 150, 0) if sequence[i] == 1 else (200, 200, 200)
        pg.draw.rect(screen, color, (50 + i * 20, height // 2 - 10, 15, 15))

    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                x, y = event.pos
                if y in range(height // 2 - 10, height // 2 + 10):
                    step_index = (x - 50) // 20
                    if 0 <= step_index < steps:
                        sequence[step_index] = 1 - sequence[step_index]  # Toggle step

    pg.display.flip()  # Update the display

# Clean up
pg.quit()
