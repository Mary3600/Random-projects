'''
import math

print("Good day, \nToday we'll be calcuating the root means square and peak values of current of any electrical device.")
print("First we need to know the power wattage and RMS voltage of your device.")

power_rating = float(input("What is the power rating of the device?(In kiloWatts[kW]\n"))
unit = input("Is power in watts or kilowatts? (Input 'W'or 'kW')\n")
if unit == 'kW' or 'kw' or 'KW' or 'Kw':
    p = power_rating * 1000
elif unit == 'w' or 'W':
    p = power_rating 
else:
    print("Invalid input. Kindly choose kw for kilowatts or w for watts")

voltage = float(input("What is the RMS voltage of the device?(in volts[v])\n"))

#current rms
current_rms = p/voltage
print("The root mean square value of current is " + str(current_rms) + "A")

#peak current
peak_current = math.sqrt(2) * current_rms
print("The peak current vaue is " + str(peak_current) + "A")
'''

import tkinter as tk
from tkinter import messagebox
import math

def calculate_currents():
    """
    Calculates the RMS and peak current values based on user input
    and displays them in the GUI.
    """
    try:
        power_rating_str = power_entry.get()
        unit = unit_entry.get().strip().lower()
        voltage_str = voltage_entry.get()

        # Validate input for power rating
        if not power_rating_str:
            messagebox.showerror("Input Error", "Please enter the power rating.")
            return
        power_rating = float(power_rating_str)

        # Determine power in watts based on unit
        if unit == 'kw':
            p = power_rating * 1000
        elif unit == 'w':
            p = power_rating
        else:
            messagebox.showerror("Input Error", "Invalid unit. Please enter 'kW' or 'W'.")
            return

        # Validate input for voltage
        if not voltage_str:
            messagebox.showerror("Input Error", "Please enter the RMS voltage.")
            return
        voltage = float(voltage_str)

        if voltage == 0:
            messagebox.showerror("Calculation Error", "Voltage cannot be zero.")
            return

        # Calculate current RMS
        current_rms = p / voltage
        rms_result_label.config(text=f"The root mean square value of current is {current_rms:.2f} A")

        # Calculate peak current
        peak_current = math.sqrt(2) * current_rms
        peak_result_label.config(text=f"The peak current value is {peak_current:.2f} A")

    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter numeric values for power and voltage.")
    except Exception as e:
        messagebox.showerror("An Error Occurred", f"An unexpected error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("Electrical Current Calculator")
root.geometry("400x350") # Set a fixed window size
root.resizable(False, False) # Make the window not resizable

# Add some padding around the widgets
padding_x = 20
padding_y = 10

# Title Label
title_label = tk.Label(root, text="Electrical Device Current Calculator", font=("Arial", 14, "bold"))
title_label.pack(pady=(20, 10))

# Frame for inputs to organize them better
input_frame = tk.Frame(root)
input_frame.pack(pady=padding_y)

# Power Rating Input
power_label = tk.Label(input_frame, text="Power Rating (e.g., 1.5):")
power_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
power_entry = tk.Entry(input_frame, width=20)
power_entry.grid(row=0, column=1, padx=5, pady=5)

# Unit Input (kW/W)
unit_label = tk.Label(input_frame, text="Power unit (kW or W):")
unit_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
unit_entry = tk.Entry(input_frame, width=20)
unit_entry.grid(row=1, column=1, padx=5, pady=5)
unit_entry.insert(0, "kW") # Default value

# RMS Voltage Input
voltage_label = tk.Label(input_frame, text="RMS Voltage (V):")
voltage_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
voltage_entry = tk.Entry(input_frame, width=20)
voltage_entry.grid(row=2, column=1, padx=5, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Currents", command=calculate_currents,
                             font=("Arial", 12), bg="#4CAF50", fg="white",
                             activebackground="#45a049", activeforeground="white")
calculate_button.pack(pady=20)

# Result Labels
rms_result_label = tk.Label(root, text="The root mean square value of current is: ", font=("Arial", 10))
rms_result_label.pack(pady=5)

peak_result_label = tk.Label(root, text="The peak current value is: ", font=("Arial", 10))
peak_result_label.pack(pady=5)

root.mainloop()