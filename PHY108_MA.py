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