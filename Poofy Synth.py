import numpy as np
import pyaudio
import tkinter as tk
from threading import Thread, Lock
from time import sleep

# Global variables
wave_type = 'sine'
playing = False
stream = None
p = None
waveform_buffer = None
buffer_lock = Lock()
frequency_range = [440, 455]  # Default frequency range

def on_closing(root):
    if playing:
        toggle_playback()
    root.destroy()

# Generate different types of waveforms
def generate_waveform(wave_type, freq, duration, sample_rate=44100, amplitude=32767):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    if wave_type == 'sine':
        wave = amplitude * np.sin(2.0 * np.pi * freq * t)
    elif wave_type == 'square':
        wave = amplitude * np.sign(np.sin(2.0 * np.pi * freq * t))
    elif wave_type == 'sawtooth':
        wave = amplitude * (2.0 * (t * freq - np.floor(t * freq + 0.5)))
    else:
        raise ValueError("Unsupported wave type")
    return wave.astype(np.int16)

# Audio playback function
def play_audio():
    global playing, stream, waveform_buffer, frequency_range
    duration = 10.0  # Duration of each waveform segment in seconds
    sample_rate = 44100

    while playing:
        freq_min, freq_max = frequency_range
        freq = np.linspace(freq_min, freq_max, int(sample_rate * duration))  # Create a linearly changing frequency
        for f in freq:
            with buffer_lock:
                waveform_buffer = generate_waveform(wave_type, f, duration, sample_rate)
                if waveform_buffer is not None:
                    stream.write(waveform_buffer.tobytes())
            sleep(duration)  # Sleep to match the duration of the waveform segment

# Toggle playback
def toggle_playback():
    global playing, stream, p, waveform_buffer
    if playing:
        playing = False
        if stream:
            stream.stop_stream()
            stream.close()
        if p:
            p.terminate()
    else:
        global wave_type, frequency_range
        wave_type = wave_type_var.get()
        freq_min = float(freq_min_entry.get())
        freq_max = float(freq_max_entry.get())
        frequency_range = [freq_min, freq_max]
        
        duration = 0.1
        sample_rate = 44100
        
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, output=True)
        
        playing = True
        playback_thread = Thread(target=play_audio)
        playback_thread.start()

# GUI setup
def setup_gui():
    global wave_type_var, freq_min_entry, freq_max_entry
    
    root = tk.Tk()
    root.title("Audio Playback Application")
    
    tk.Label(root, text="Frequency Min (Hz):").pack()
    freq_min_entry = tk.Entry(root)
    freq_min_entry.pack()
    freq_min_entry.insert(0, "440")
    
    tk.Label(root, text="Frequency Max (Hz):").pack()
    freq_max_entry = tk.Entry(root)
    freq_max_entry.pack()
    freq_max_entry.insert(0, "455")
    
    tk.Label(root, text="Wave Type:").pack()
    wave_type_var = tk.StringVar(value='sine')
    tk.Radiobutton(root, text="Sine", variable=wave_type_var, value='sine').pack()
    tk.Radiobutton(root, text="Square", variable=wave_type_var, value='square').pack()
    tk.Radiobutton(root, text="Sawtooth", variable=wave_type_var, value='sawtooth').pack()
    
    play_button = tk.Button(root, text="Play/Pause", command=toggle_playback)
    play_button.pack()

    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    
    root.mainloop()

if __name__ == "__main__":
    setup_gui()
