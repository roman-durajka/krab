STRING_TO_DECRYPT = "CECEKGIKCPG PKYJTPMP"


def inverse(key):
    new_key = 0
    for i in range(1, 27):
        if (i*key) % 27 == 1:
            new_key = i
            break

    return new_key


def main():
    for key1 in range(1, 27):
        for key2 in range(1, 27):
            inverted_key1 = inverse(key1)
            inverted_key2 = 27 - key2

            decrypted_string = ""
            for char in STRING_TO_DECRYPT:
                if char == " ":
                    numeric_char = 26
                else:
                    numeric_char = ord(char) - 65
                decrypted_char = (inverted_key1 * numeric_char + inverted_key2) % 27
                if decrypted_char == 26:
                    decrypted_string += " "
                else:
                    decrypted_string += chr(decrypted_char + 65)

            print(decrypted_string)


if __name__ == "__main__":
    main()
