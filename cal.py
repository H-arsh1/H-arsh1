import tkinter as tk

def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5/9
    celsius_label.config(text=f"{round(celsius, 2)}°C")

def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_label.config(text=f"{round(fahrenheit, 2)}°F")

window = tk.Tk()
window.title("Temperature Converter")

fahrenheit_label = tk.Label(text="Fahrenheit")
fahrenheit_label.grid(column=0, row=0)

fahrenheit_entry = tk.Entry(width=10)
fahrenheit_entry.grid(column=1, row=0)

celsius_label = tk.Label(text="Celsius")
celsius_label.grid(column=0, row=1)

celsius_entry = tk.Entry(width=10)
celsius_entry.grid(column=1, row=1)

fahrenheit_button = tk.Button(text="Convert to Celsius", command=fahrenheit_to_celsius)
fahrenheit_button.grid(column=2, row=0)

celsius_button = tk.Button(text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
celsius_button.grid(column=2, row=1)

window.mainloop()
