
def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Input
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))
mode = input("Choose mode (encrypt/decrypt): ").lower()

# Output
output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")
