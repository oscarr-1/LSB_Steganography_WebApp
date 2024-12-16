import wave
import numpy as np

def extract_message(audio_path):
    audio = wave.open(audio_path, 'rb')

    frames = audio.readframes(audio.getnframes())
    frame_array = np.frombuffer(frames, dtype=np.uint8)

    bin_secret_message = ''
    for i in range(len(frame_array)):
        bin_secret_message += str(frame_array[i] & 1)
    
    secret_message = ''
    for i in range(0, len(bin_secret_message), 8):
        char = chr(int(bin_secret_message[i:i+8], 2))
        if char == '#' and secret_message.endswith('END'):
            return secret_message[:-4]
        secret_message += char
    
    return 'No hidden message found'