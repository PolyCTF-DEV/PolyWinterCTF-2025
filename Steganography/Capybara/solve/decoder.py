from PIL import Image

def extract_text_from_transparent_pixels(image_path):
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size

    binary_text = ""
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a % 2 == 0:  
                binary_text += str(r & 1)  
                binary_text += str(g & 1)  
                binary_text += str(b & 1)  
    secret_text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i + 8]
        secret_text += chr(int(byte, 2))

    return secret_text

secret_message = extract_text_from_transparent_pixels("task.png")
print("Извлечённое сообщение:", secret_message)
