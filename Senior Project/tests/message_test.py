from PIL import Image

def verify_hidden_text(image_path, original_message):
    image = Image.open(image_path)
    pixels = image.load()

    secret_text = original_message + '#END#'
    bin_secret_text = ''.join(format(ord(char), '08b') for char in secret_text)

    extracted_bits = []
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            extracted_bits.append(r & 1)
            extracted_bits.append(g & 1)
            extracted_bits.append(b & 1)

            if len(extracted_bits) >= len(bin_secret_text):
                break
        if len(extracted_bits) >= len(bin_secret_text):
            break

    extracted_bin_text = ''.join(str(bit) for bit in extracted_bits)

    return extracted_bin_text == bin_secret_text

original_image = "tests/parrots.bmp"
modified_image = "tests/new.bmp"
secret_message = "parrots"

if verify_hidden_text(modified_image, secret_message):
    print("Message successfully hidden!")
else:
    print("Message embedding failed.")
