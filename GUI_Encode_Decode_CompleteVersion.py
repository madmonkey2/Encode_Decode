from tkinter import *
from functools import partial

navy = '#203354'
black = '#000000'
green = '#00FF00'
orange = '#FFA500'

special_character = [',', ':', '!', '?', '*', '&', '%', '$', '#', '@', '(', ')']
codes = {'A': '.-', 'B': '-...',
         'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-',
         'L': '.-..', 'M': '--', 'N': '-.',
         'O': '---', 'P': '.--.', 'Q': '--.-',
         'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--',
         'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.',
         '0': '-----', ' ': '/'}


# ---------------------------- Encode text to Morse ------------------------------- #

def encode(char, x1):
    code = (x1.get())
    word = code.upper()
    enc = ""
    for i in word:
        if (i in special_character):
            pass
        else:
            enc += codes[i] + " "
    char.config(text=enc)
    return enc


# ---------------------------- Decode Morse to text ------------------------------- #

def decode(char, x2):
    word = (x2.get())
    word += " "

    key_list = list(codes.keys())
    val_list = list(codes.values())

    # To store morse code in a temp variable
    morse_code = ""
    plain_text = ""
    for letters in word:
        if letters != " ":
            morse_code += letters
            space_found = 0
        else:
            space_found += 1
            if space_found == 2:
                plain_text += " "
            else:

                # Accessing the index of the value i.e, morsecode and then from that index finding the key at that index
                plain_text += key_list[val_list.index(morse_code)]

                # Again making morse_code empty so that it can store next morse in it
                morse_code = ""
    char.config(text=plain_text)
    return f" {plain_text}"


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Exercise9 - Encode/Decode Morse_Code")
root.config(padx=50, pady=25, bg=navy)

title = Label(text="Welcome to the MorseCode Converter!!!", fg=green, bg=black, font=("Times New Roman", 15))
text_to_morse = Label(text="Enter the text to be encrypted:  ", fg=green, bg=black)
morse_to_text = Label(text="Enter the MorseCode to be decyphyered:  ", fg=green, bg=black)
rst = Label(text="Result of the converter: ", fg=green, bg=black)
output = Label(root, fg=green, bg=black, font=("Times New Roman", 18, 'bold'))

x1 = StringVar()
x2 = StringVar()

e1 = Entry(textvariable=x1)
e2 = Entry(textvariable=x2)

title.grid(row=2, column=2)
text_to_morse.grid(row=3, column=0, sticky="W")
morse_to_text.grid(row=5, column=0, sticky="W")
rst.grid(row=6, column=0, sticky="W")
output.grid(row=6, column=2)
e1.grid(row=3, column=2)
e2.grid(row=5, column=2)

encode = partial(encode, output, x1)
decode = partial(decode, output, x2)

button = Button(root, text="Encrypt", command=encode, fg=green, bg=black)
button2 = Button(root, text="Decrypt", command=decode, fg=green, bg=black)

button.grid(row=3, column=3)
button2.grid(row=5, column=3)

root.mainloop()
