import numpy as np
import soundfile as sf
import pyaudio
import threading

# === Audio lesen ===
filename = 'test.ogg'  # oder z. B. 'test.wav'
data, samplerate = sf.read(filename)

# === Nur Mono verwenden ===
if data.ndim > 1:
    data = data[:, 0]

# === Audio speichern als MP3 ===
sf.write('new.mp3', data, samplerate)

# === Audio abspielen in eigenem Thread ===
def play_audio(data, samplerate):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=samplerate,
                    output=True)
    
    # Konvertiere zu 32-Bit Float und spiele ab
    stream.write(data.astype(np.float32).tobytes())
    
    stream.stop_stream()
    stream.close()
    p.terminate()

# === Starte Wiedergabe in eigenem Thread ===
t = threading.Thread(target=play_audio, args=(data, samplerate))
t.start()

# Weiterer Code kann hier ausgeführt werden, während Audio spielt
print("Audio wird abgespielt...")

# Warten bis Audio zu Ende ist (optional)
t.join()
print("Abspielen abgeschlossen.")
