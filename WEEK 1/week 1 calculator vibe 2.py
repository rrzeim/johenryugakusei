import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")

# Configure grid for equal button resizing
for i in range(8):  # 1 row for output + 7 rows for buttons
    root.rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    root.columnconfigure(j, weight=1)

# Output textbox (readonly Entry)
output_var = tk.StringVar()
output = tk.Entry(
    root,
    textvariable=output_var,
    font=("Arial", 24),
    justify="right",
    bd=10,
    state="readonly"
)
output.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# --- Functions ---
def on_button_click(value):
    """Append button value to display"""
    current = output_var.get()
    output_var.set(current + value)

def clear_output():
    """Clear the display"""
    output_var.set("")

def evaluate_expression():
    """Evaluate the math expression"""
    expr = output_var.get()

    # Replace alternative grouping symbols with ()
    expr = expr.replace("[", "(").replace("]", ")")
    expr = expr.replace("{", "(").replace("}", ")")
    expr = expr.replace("<", "(").replace(">", ")")

    try:
        result = str(eval(expr))
        output_var.set(result)
    except Exception:
        output_var.set("Error")

# Button layout
buttons = [
    # Row 1: parentheses and brackets
    ("(", 1, 0), (")", 1, 1), ("[", 1, 2), ("]", 1, 3),
    # Row 2: curly braces and angle brackets
    ("{", 2, 0), ("}", 2, 1), ("<", 2, 2), (">", 2, 3),
    # Row 3: numbers 7–9 and AC
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("AC", 3, 3),
    # Row 4: numbers 4–6 and =
    ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("=", 4, 3),
    # Row 5: numbers 1–3 and +
    ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("+", 5, 3),
    # Row 6: 0, decimal, - and *
    ("0", 6, 0), (".", 6, 1), ("-", 6, 2), ("*", 6, 3),
    # Row 7: division
    ("/", 7, 0)
]

# Place buttons in grid
for (text, row, col) in buttons:
    if text == "AC":
        action = clear_output
    elif text == "=":
        action = evaluate_expression
    else:
        action = lambda t=text: on_button_click(t)

    button = tk.Button(root, text=text, font=("Arial", 18), command=action)
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Run the application
root.mainloop()