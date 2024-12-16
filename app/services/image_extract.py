from PIL import Image

def extract_text(image_path):
    image = Image.open(image_path)

    pixels = image.load()
    bin_secret_text = ''
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            bin_secret_text += str(r & 1)
            bin_secret_text += str(g & 1)
            bin_secret_text += str(b & 1)
    
    secret_text = ''
    for i in range(0, len(bin_secret_text), 8):
        char = chr(int(bin_secret_text[i:i+8], 2))
        if char == '#' and secret_text.endswith('END'):
            return secret_text[:-4]
        secret_text += char
    
    return 'No hidden message found'