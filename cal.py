import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("300x400")

        # Define la fuente y el tamaño de letra
        font = ("Arial", 18)

        # Crea el campo de entrada
        self.entry = tk.Entry(master, width=20, font=font, justify="right", bd=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Crea los botones
        button_1 = tk.Button(master, text="1", padx=20, pady=10, font=font, command=lambda: self.button_click(1))
        button_2 = tk.Button(master, text="2", padx=20, pady=10, font=font, command=lambda: self.button_click(2))
        button_3 = tk.Button(master, text="3", padx=20, pady=10, font=font, command=lambda: self.button_click(3))
        button_4 = tk.Button(master, text="4", padx=20, pady=10, font=font, command=lambda: self.button_click(4))
        button_5 = tk.Button(master, text="5", padx=20, pady=10, font=font, command=lambda: self.button_click(5))
        button_6 = tk.Button(master, text="6", padx=20, pady=10, font=font, command=lambda: self.button_click(6))
        button_7 = tk.Button(master, text="7", padx=20, pady=10, font=font, command=lambda: self.button_click(7))
        button_8 = tk.Button(master, text="8", padx=20, pady=10, font=font, command=lambda: self.button_click(8))
        button_9 = tk.Button(master, text="9", padx=20, pady=10, font=font, command=lambda: self.button_click(9))
        button_0 = tk.Button(master, text="0", padx=20, pady=10, font=font, command=lambda: self.button_click(0))

        button_add = tk.Button(master, text="+", padx=20, pady=10, font=font, bg="#4CAF50", fg="white", command=self.button_add)
        button_subtract = tk.Button(master, text="-", padx=20, pady=10, font=font, bg="#4CAF50", fg="white", command=self.button_subtract)
        button_multiply = tk.Button(master, text="*", padx=20, pady=10, font=font, bg="#4CAF50", fg="white", command=self.button_multiply)
        button_divide = tk.Button(master, text="/", padx=20, pady=10, font=font, bg="#4CAF50", fg="white", command=self.button_divide)

        button_clear = tk.Button(master, text="C", padx=20, pady=10, font=font, bg="#F44336", fg="white", command=self.button_clear)
        button_equal = tk.Button(master, text="=", padx=20, pady=10, font=font, bg="#2196F3", fg="white", command=self.button_equal)

        # Coloca los botones en la interfaz gráfica
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)

        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)

        button_0.grid(row=4, column=0)

        button_add.grid(row=1, column=3)
        button_subtract.grid(row=2, column=3)
        button_multiply.grid(row=3, column=3)
        button_divide.grid(row=4, column=3)

        button_clear.grid(row=4, column=1)
        button_equal.grid(row=4, column=2)

    # Define las funciones de los botones
    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(current) + str(number))

    def button_clear(self):
        self.entry.delete(0, tk.END)

    def button_add(self):
        first_number = self.entry.get()
        self.entry.delete(0, tk.END)
        self.first_number = int(first_number)
        self.operation = "+"

    def button_subtract(self):
        first_number = self.entry.get()
        self.entry.delete(0, tk.END)
        self.first_number = int(first_number)
        self.operation = "-"

    def button_multiply(self):
        first_number = self.entry.get()
        self.entry.delete(0, tk.END)
        self.first_number = int(first_number)
        self.operation = "*"

    def button_divide(self):
        first_number = self.entry.get()
        self.entry.delete(0, tk.END)
        self.first_number = int(first_number)
        self.operation = "/"

    def button_equal(self):
        second_number = self.entry.get()
        self.entry.delete(0, tk.END)

        if self.operation == "+":
            self.entry.insert(0, self.first_number + int(second_number))
        elif self.operation == "-":
            self.entry.insert(0, self.first_number - int(second_number))
        elif self.operation == "*":
            self.entry.insert(0, self.first_number * int(second_number))
        elif self.operation == "/":
            self.entry.insert(0, self.first_number / int(second_number))

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()