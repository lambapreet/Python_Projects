import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start recording
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# Wait until the recording is finished
sd.wait()

# Save the recording using scipy
write("recording0.wav", freq, recording)

# Save the recording using wavio
# Note: wavio expects the data to be in the correct format (e.g., int16)
# Convert the recording to int16 format
recording_int16 = (recording * 32767).astype('int16')  # Scale to int16 range
wv.write("recording1.wav", recording_int16, freq, sampwidth=2)