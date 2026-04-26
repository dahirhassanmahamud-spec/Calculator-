# Calculator-
My first calculator program of python build using tkinter
# Calculator Application

This is a functional desktop calculator built using Python and the Tkinter library. It features a modern, dark-themed interface inspired by common mobile calculator designs and supports basic arithmetic operations along with advanced functions like square root and percentage.

---

## Features

* **Basic Arithmetic:** Addition, subtraction, multiplication, and division.
* **Advanced Functions:** Square root calculation and percentage conversion.
* **Sign Toggle:** Quickly switch between positive and negative values.
* **Clear Function:** Reset the calculator using the AC (All Clear) button.
* **Responsive Layout:** A grid-based UI that maintains its structure.
* **Error Handling:** Displays an Error message in the event of invalid operations, such as dividing by zero or taking the square root of a negative number.

---

## Prerequisites

To run this application, you must have Python installed on your system. Tkinter is included with most standard Python installations.

* Python 3.x

---

## How to Run

1.  Save the code provided in a file named `calculator.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory containing the file.
4.  Run the application using the following command:

    ```bash
    python calculator.py
    ```

---

## Technical Overview

### Components

* **Tkinter:** Used for the Graphical User Interface (GUI).
* **Math Module:** Utilized for precise square root calculations.
* **Eval Function:** Processes the string expressions into mathematical results after sanitizing operator symbols.

### UI Styling

| Element | Color Hex |
| :--- | :--- |
| Background | #1c1c1c |
| Operators | #f0a500 |
| Function Keys | #a0a0a0 |
| Number Keys | #505050 |
| Text | White |

---

## Logic Flow

1.  **Input:** The `_on_click` method captures button presses and appends them to the `expression` string.
2.  **Sanitization:** Before evaluation, visual symbols like "÷" and "×" are converted to Python-readable "/" and "*".
3.  **Calculation:** The `eval()` function processes the math, and the result is updated in the `display_var`.
4.  **Display:** The UI updates dynamically via the `tk.StringVar` linked to the top label.
5.  ## Developer Information
6.  Name:Mohamud Dahir Hassan
7.  Reg.No 25/BCC/BU/R/0014
