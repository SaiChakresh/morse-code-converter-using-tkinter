import tkinter as tk

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': ' '
}

def convert_to_morse_code(text):
    text = text.upper()
    morse = []
    for char in text:
        morse.append(MORSE_CODE_DICT.get(char, ''))  # skip unknown characters
    return ' '.join(morse)

def on_convert():
    input_text = input_entry.get("1.0", tk.END).strip()
    morse_result = convert_to_morse_code(input_text)
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, morse_result)
    output_text.config(state='disabled')

# Setup GUI
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("600x400")
root.resizable(False, False)

# Input Label
tk.Label(root, text="Enter Text:", font=("Helvetica", 14)).pack(pady=10)

# Input Box
input_entry = tk.Text(root, height=5, width=60, font=("Helvetica", 12))
input_entry.pack()

# Convert Button
convert_button = tk.Button(root, text="Convert to Morse", font=("Helvetica", 12), command=on_convert)
convert_button.pack(pady=15)

# Output Label
tk.Label(root, text="Morse Code Output:", font=("Helvetica", 14)).pack()

# Output Box (Read-only)
output_text = tk.Text(root, height=5, width=60, font=("Courier", 12), bg="#f0f0f0")
output_text.pack()
output_text.config(state='disabled')

root.mainloop()
