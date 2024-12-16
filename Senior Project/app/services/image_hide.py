from PIL import Image
import os

def hide_text(image_path, secret_text, output_path):
    image = Image.open(image_path)

    secret_text += '#END#'

    bin_secret_text = ''.join(format(ord(char), '08b') for char in secret_text)

    image_cap = image.width * image.height * 3

    if len(bin_secret_text) > image_cap:
        raise ValueError('Insufficient image capacity to hide the secret text.')
    
    pixels = image.load()
    index = 0
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            
            if index < len(bin_secret_text):
                r = (r & 0xFE) | int(bin_secret_text[index])
                index += 1
            if index < len(bin_secret_text):
                g = (g & 0xFE) | int(bin_secret_text[index])
                index += 1
            if index < len(bin_secret_text):
                b = (b & 0xFE) | int(bin_secret_text[index])
                index += 1
            
            pixels[i, j] = (r, g, b)
        if index >= len(bin_secret_text):
            break
    
    image.save(output_path)

    return output_path