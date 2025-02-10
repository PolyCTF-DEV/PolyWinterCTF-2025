from Crypto.Util.strxor import strxor
import string

def check_validity(data):
    allowed_chars = set(string.ascii_letters + string.digits + string.punctuation)
    return all(ch in allowed_chars or ch.isspace() for ch in data)

with open("output.txt", "r") as file:
    encoded_text = file.readline().strip()

decoded_bytes = bytes.fromhex(encoded_text)
length_decoded = len(decoded_bytes)

for possible_key_length in range(12, 44):
    if length_decoded % possible_key_length == 0:
        mapping = {}

        segment_length = length_decoded // possible_key_length
        for index in range(length_decoded):
            if index % possible_key_length == 0:
                mapping[index % segment_length] = decoded_bytes[index]

        if segment_length == len(mapping):
            sorted_values = (dict(sorted(mapping.items()))).values()
            extracted_data = b''.join(bytes([val]) for val in sorted_values)

            for key_candidate in range(256):
                decrypted_text = strxor(extracted_data, bytes([key_candidate]) * segment_length)

                try:
                    decoded_string = decrypted_text.decode('utf-8')
                except UnicodeDecodeError:
                    continue

                for segment in decoded_string.split():
                    if check_validity(segment):
                        print(segment, possible_key_length)
