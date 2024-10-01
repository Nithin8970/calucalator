import tkinter as tk
window = tk.Tk()
window.title("Calculator")
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('%', 5, 0), ('^', 5, 1), ('%', 5, 0), ('^', 5, 1), 
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, padx=30, pady=30, command=button_equal)
    else:
        button = tk.Button(window, text=text, padx=30, pady=30, command=lambda txt=text: button_click(txt))
    button.grid(row=row, column=col)

clear_button = tk.Button(window, text="Clear", padx=89, pady=30, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2)

exit_button = tk.Button(window, text="Exit", padx=89, pady=30, command=window.quit)
exit_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
