import tkinter as tk

# Global variables to store calculation state
first_num = None
operation = None

# Function to update output when number is pressed
def on_number_click(num):
    current = output["text"]
    output.config(text=current + str(num))

# Function to clear output
def clear_output():
    global first_num, operation
    first_num = None
    operation = None
    output.config(text="")

# Function when operator is pressed
def on_operator_click(op):
    global first_num, operation
    current = output["text"]
    if current != "":
        first_num = current
        operation = op
        output.config(text=current + op)  # keep first number, add operator

# Function to calculate result
def calculate_result():
    global first_num, operation
    if first_num is not None and operation is not None:
        try:
            expression = output["text"].replace("×", "*").replace("÷", "/")
            result = str(eval(expression))  # use eval for simplicity
            output.config(text=result)
            # Reset so result can be used as next input
            first_num = None
            operation = None
        except Exception:
            output.config(text="Error")
            first_num = None
            operation = None

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Create a non-editable output display (Label widget)
output = tk.Label(root, text="", font=("Arial", 20), bg="white", anchor="e", relief="ridge", height=2)
output.pack(pady=10, padx=10, fill="x")

# Create a frame to hold the operator buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=5, fill="x")

# Define operator buttons with functionality
btn_add = tk.Button(button_frame, text="+", font=("Arial", 16), command=lambda: on_operator_click("+"))
btn_sub = tk.Button(button_frame, text="-", font=("Arial", 16), command=lambda: on_operator_click("-"))
btn_mul = tk.Button(button_frame, text="×", font=("Arial", 16), command=lambda: on_operator_click("×"))
btn_div = tk.Button(button_frame, text="÷", font=("Arial", 16), command=lambda: on_operator_click("÷"))

# Place them in a single row and stretch equally
btn_add.pack(side="left", expand=True, fill="both")
btn_sub.pack(side="left", expand=True, fill="both")
btn_mul.pack(side="left", expand=True, fill="both")
btn_div.pack(side="left", expand=True, fill="both")

# Frame for number buttons, AC, and Equal
num_frame = tk.Frame(root)
num_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Create number buttons with functionality
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
    ("0", 3, 0), ("AC", 3, 1), ("=", 3, 2)
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]

    if text.isdigit():  # Number buttons
        tk.Button(num_frame, text=text, font=("Arial", 16),
                  command=lambda t=text: on_number_click(t))\
            .grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    elif text == "AC":  # Clear button
        tk.Button(num_frame, text=text, font=("Arial", 16),
                  command=clear_output)\
            .grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    else:  # "=" button
        tk.Button(num_frame, text=text, font=("Arial", 16),
                  command=calculate_result)\
            .grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Make grid cells expand equally
for i in range(3):
    num_frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    num_frame.grid_rowconfigure(i, weight=1)

# Run the window loop
root.mainloop()