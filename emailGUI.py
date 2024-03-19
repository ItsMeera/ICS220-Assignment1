import tkinter as tk
from tkinter import messagebox

class MyCalc:
    """Class to represent calculator layout"""

    # Constructor
    def __init__(self):
        # Create the window
        self.main_window = tk.Tk()
        self.main_window.title("My Calculator")  # Change title
        self.main_window.resizable(False, False)  # Disallow resizing

        # Create two frames inside the window
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Entry in the top frame
        self.entry = tk.Entry(self.top_frame, width=25, justify="right", state="disabled")  # Deactivate entry
        self.entry.grid(row=0, columnspan=4, sticky="W")

        # Buttons in the bottom frame and in grid layout
        self.cls = tk.Button(self.bottom_frame, text="C", width=4, command=self.clear)  # Use one button as Clear button
        self.cls.grid(row=1, column=0)
        self.bck = tk.Button(self.bottom_frame, text="←", width=4)
        self.bck.grid(row=1, column=1)
        self.lbl = tk.Button(self.bottom_frame, width=4)
        self.lbl.grid(row=1, column=2)
        self.clo = tk.Button(self.bottom_frame, text="Close", command=self.close)
        self.clo.grid(row=1, column=3)
        self.sev = tk.Button(self.bottom_frame, text="7", width=4, command=lambda: self.append_to_display("7"))
        self.sev.grid(row=2, column=0)
        self.eig = tk.Button(self.bottom_frame, text="8", width=4, command=lambda: self.append_to_display("8"))
        self.eig.grid(row=2, column=1)
        self.nin = tk.Button(self.bottom_frame, text="9", width=4, command=lambda: self.append_to_display("9"))
        self.nin.grid(row=2, column=2)
        self.div = tk.Button(self.bottom_frame, text="/", width=4, command=lambda: self.append_to_display("/"))
        self.div.grid(row=2, column=3)

        self.fou = tk.Button(self.bottom_frame, text="4", width=4, command=lambda: self.append_to_display("4"))
        self.fou.grid(row=3, column=0)
        self.fiv = tk.Button(self.bottom_frame, text="5", width=4, command=lambda: self.append_to_display("5"))
        self.fiv.grid(row=3, column=1)
        self.six = tk.Button(self.bottom_frame, text="6", width=4, command=lambda: self.append_to_display("6"))
        self.six.grid(row=3, column=2)
        self.mul = tk.Button(self.bottom_frame, text="*", width=4, command=lambda: self.append_to_display("*"))
        self.mul.grid(row=3, column=3)

        self.one = tk.Button(self.bottom_frame, text="1", width=4, command=lambda: self.append_to_display("1"))
        self.one.grid(row=4, column=0)
        self.two = tk.Button(self.bottom_frame, text="2", width=4, command=lambda: self.append_to_display("2"))
        self.two.grid(row=4, column=1)
        self.thr = tk.Button(self.bottom_frame, text="3", width=4, command=lambda: self.append_to_display("3"))
        self.thr.grid(row=4, column=2)
        self.mns = tk.Button(self.bottom_frame, text="-", width=4, command=lambda: self.append_to_display("-"))
        self.mns.grid(row=4, column=3)

        self.zer = tk.Button(self.bottom_frame, text="0", width=4, command=lambda: self.append_to_display("0"))
        self.zer.grid(row=5, column=0)
        self.dot = tk.Button(self.bottom_frame, text=".", width=4, command=lambda: self.append_to_display("."))
        self.dot.grid(row=5, column=1)
        self.equ = tk.Button(self.bottom_frame, text="=", width=4, command=self.calculate)  # Bind calculate function to "="
        self.equ.grid(row=5, column=2)
        self.pls = tk.Button(self.bottom_frame, text="+", width=4, command=lambda: self.append_to_display("+"))
        self.pls.grid(row=5, column=3)

        # Pack both the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Display window and keep focus
        self.main_window.mainloop()

    # Function to append text to the display
    def append_to_display(self, value):
        current_text = self.entry.get()
        self.entry.config(state="normal")  # Activate entry for writing
        self.entry.delete(0, tk.END)  # Clear the current text
        self.entry.insert(0, current_text + value)  # Append the new value
        self.entry.config(state="disabled")  # Deactivate entry again

    # Function to clear the display
    def clear(self):
        self.entry.config(state="normal")  # Activate entry for writing
        self.entry.delete(0, tk.END)  # Clear the current text
        self.entry.config(state="disabled")  # Deactivate entry again

    # Function to calculate the result
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.config(state="normal")  # Activate entry for writing
            self.entry.delete(0, tk.END)  # Clear the current text
            self.entry.insert(0, str(result))  # Show the result
            self.entry.config(state="disabled")  # Deactivate entry again
        except:
            messagebox.showerror("Error", "Invalid expression!")

    # Function to close the calculator
    def close(self):
        self.main_window.destroy()

# Create an object of the calculator
mycal = MyCalc()
