from string import ascii_lowercase


def encryption(string, key):
    alphabet = ascii_lowercase
    result = ''
    for char in string:
        if char not in alphabet:
            if char.lower() not in alphabet:
                result += char
            else:
                new_key = (alphabet.index(char.lower()) + key) % len(alphabet)
                result += alphabet[new_key].upper()

        else:
            new_key = (alphabet.index(char) + key) % len(alphabet)
            result += alphabet[new_key]
    return result

string = input('insert text for encryption : ')
key = int(input('insert encryption key : '))
print(encryption(string,key))
