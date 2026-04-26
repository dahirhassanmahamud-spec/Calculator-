import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self):
        # Display
        display = tk.Label(
            self.root,
            textvariable=self.display_var,
            anchor="e",
            bg="#1c1c1c",
            fg="white",
            font=("Helvetica", 40, "bold"),
            padx=10,
            pady=20,
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout
        buttons = [
            ["AC", "+/-", "%", "÷"],
            ["7",  "8",   "9", "×"],
            ["4",  "5",   "6", "-"],
            ["1",  "2",   "3", "+"],
            ["0",  ".",   "√", "="],
        ]

        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                self._make_button(label, r + 1, c)

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1, minsize=80)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1, minsize=70)

    def _make_button(self, label, row, col):
        if label in ("÷", "×", "-", "+", "="):
            bg, fg = "#f0a500", "white"
        elif label in ("AC", "+/-", "%"):
            bg, fg = "#a0a0a0", "white"
        else:
            bg, fg = "#505050", "white"

        btn = tk.Button(
            self.root,
            text=label,
            font=("Helvetica", 22, "bold"),
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            borderwidth=1,
            relief="flat",
            command=lambda l=label: self._on_click(l),
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

    def _on_click(self, label):
        current = self.display_var.get()

        if label == "AC":
            self.expression = ""
            self.display_var.set("0")

        elif label == "+/-":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.display_var.set(self.expression)

        elif label == "%":
            try:
                val = str(float(self.expression) / 100)
                self.expression = val
                self.display_var.set(val)
            except:
                self.display_var.set("Error")
                self.expression = ""

        elif label == "√":
            try:
                val = str(math.sqrt(float(self.expression)))
                self.expression = val
                self.display_var.set(val)
            except:
                self.display_var.set("Error")
                self.expression = ""

        elif label == "=":
            try:
                expr = self.expression.replace("÷", "/").replace("×", "*")
                result = str(eval(expr))
                self.display_var.set(result)
                self.expression = result
            except:
                self.display_var.set("Error")
                self.expression = ""

        else:
            if current == "0" and label not in (".", "÷", "×", "-", "+"):
                self.expression = label
            else:
                self.expression += label
            self.display_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
