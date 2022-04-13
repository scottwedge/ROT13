#!/usr/bin/env python3

# ROT13 (add 13 to encrypt; subtract 13 to decrypt)
# so should convert between
# Cryptography is fun
# Pelcgbtencul vf sha

# Tests

def test_encode():
    assert encode("Cryptography is fun", up, low) == "Pelcgbtencul vf sha"

def test_decode():
    assert decode("Pelcgbtencul vf sha", up, low) == "Cryptography is fun"

# Functions:

def encode(text, up, low):
    result = ""
    for j in text:
        print("DEBUG____j=", j)
        if j in up:
            indx = up.index(j)  # find index for letter
            indx += 13  # Offset it
            indx = indx % len(up)  # Wrap around end of alphabet if needed
            result = result + up[indx]  # Add character
        elif j in low:
            indx = low.index(j)  # find index for letter
            indx += 13  # Offset it
            indx = indx % len(low)  # Wrap around end of alphabet if needed
            result = result + low[indx]  # Add character
        else:
            result = result + j  # Non alphabet character remains as is
    return result

def main():
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    text = "Cryptography is fun"
    res = encode(text, upper_alphabet, lower_alphabet)
    print(res)

if __name__ == "__main__":
    main()
