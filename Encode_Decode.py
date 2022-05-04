def encode(char, is_code=False):
    special_character = [',', ':', '!', '?', '*', '&', '%', '$', '#', '@', '(', ')']
    code = ' '
    char_to_morse_code = {'A': '.-', 'B': '-...',
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

    # ---------------------------ENCODE----------------------------------
    if is_code == False:
        for i in char:
            if i in special_character:
                pass
            else:
                code += f'{char_to_morse_code[i.upper()]}'
        return code.strip()  # Strip REMOVE leading whitespace

    # ---------------------------DECODE----------------------------------
    if is_code == True:
        char_split = char.split()  # Split making a long string into indexes of string in a LIST.
        # Ex: "HELLO" after
        # SPLIT would be ['H' 'E' 'L' 'L' 'O'].
        for i in range(len(char_split)):  # Use range(len()) to avoid LIST is not STRING TypeError.
            for key, value in char_to_morse_code.items():
                if char_split[i] == value:
                    code += key
        return ''.join(code).strip()  # STRIP concatenate the separate index into a long string OPPOSITE TO SPLIT

#     Ex: ['H' 'E' 'L' 'L' 'O']
#     After join method would become "HELLO"


char = input("Enter the text to convert to Morse Code if is_code is False or enter Morse Code to convert to text if is_code is True: ")
print(encode(char, is_code=True))


from tkinter import *
from functools import partial
import tkinter.messagebox as tmessage

win = Tk()
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


# MorseCode To Text
def sssum(label, x2):
    n2 = (x2.get())
    word = n2
    word += ' '
    decipher = ''
    citext = ''

    for letter in word:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(codes.keys())[list(codes.values()).index(citext)]
                citext = ''
    label.config(text=decipher)
    return decipher

# Text to MorseCode Converter Function
def sum(label, x1):
    n1 = (x1.get())
    code = n1
    word = code.upper()
    enc = ""
    for i in word:
        if (i != " "):
            enc += codes[i] + " "
        else:
            enc += " "
    label.config(text=enc)
    return enc


# GUI Building

win.title("Exercise_9 Morsecode converter")
win.configure(background="Blue")
win.geometry("750x250")

l0 = Label(win, text="Welcome to the MorseCode Converter", fg="BLue", bg="Violet")
l1 = Label(win, text="Enter the text to be encrypted:  ", fg="BLue", bg="Violet")
l2 = Label(win, text="Enter the MorseCode to be decyphyered:  ", fg="BLue", bg="Violet")
label = Label(win, text="Output: ", fg="Blue", bg="Violet")
x1 = StringVar()
x2 = StringVar()
e1 = Entry(win, textvariable=x1)
e2 = Entry(win, textvariable=x2)




# Button Is Decleared
button = Button(win, text="Encrypt", command=sum, fg="BLue", bg="Violet")
sum = partial(sum, label, x1)
button2 = Button(win, text="Decrypt", command=sssum, fg="BLue", bg="Violet")
sssum = partial(sssum, label, x2)

l0.grid(row=2, column=2)
l1.grid(row=3, column=0)
l2.grid(row=5, column=0)
e1.grid(row=3, column=2)
e2.grid(row=5, column=2)
button.grid(row=3, column=3)
button2.grid(row=5, column=3)

mymenu = Menu(win)
m1 = Menu(mymenu, tearoff=0)
win.config(menu=mymenu)
mymenu.add_cascade(label="File", menu=m1)


win.mainloop()
