import wave
import numpy as np

def hide_message(audio_path, secret_message, output_path):
    print(f"Audio path: {audio_path}")
    print(f"Secret message: {secret_message}")

    secret_message += '#END#'

    audio = wave.open(audio_path, 'rb')

    frames = audio.readframes(audio.getnframes())
    frame_array = np.frombuffer(frames, dtype=np.uint8)

    bin_secret_message = ''.join(format(ord(c), '08b') for c in secret_message)

    if len(bin_secret_message) > len(frame_array):
        raise ValueError('Insufficient audio file capacity to hide the secret message')
    
    frame_array = frame_array.astype(np.int32)
    
    index = 0
    for i in range(len(frame_array)):
        if index < len(bin_secret_message):
            frame_array[i] = (frame_array[i] & 0xFE) | int(bin_secret_message[index])
            index += 1

    frame_array = np.clip(frame_array, 0, 255).astype(np.uint8)
    
    modified_audio = wave.open(output_path, 'wb')
    modified_audio.setparams(audio.getparams())
    modified_audio.writeframes(frame_array.astype(np.uint8).tobytes())
    modified_audio.close()

    audio.close()
    
    return output_path