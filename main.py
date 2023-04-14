import os
import gc
import sys
import subprocess
import matplotlib
from matplotlib import pyplot as plt
from math import log

matplotlib.use('TkAgg')
dictionary = {
    2: "Binary", 3: "Ternary", 4: "Quaternary", 5: "Quinary", 6: "Senary", 7: "Septenary", 8: "Octal", 9: "Nonary",
    10: "Decimal", 11: "Undecimal", 12: "Duodecimal", 13: "Tridecimal", 14: "Tetradecimal", 15: "Pentadecimal",
    16: "Hexadecimal", 17: "Heptadecimal", 18: "Octodecimal", 19: "Nonadecimal", 20: "Vigesimal"
}

averages = []
approximation = []
x_values = []
i = 0

while True:
    primary_base = input("Primary Base: ")
    secondary_base = input("Secondary Base: ")
    length = input("Maximum Integer Size: ")
    if not length:
        length = "9999000000000"

    if int(primary_base) >= 2 and int(secondary_base) >= 2 and int(length) > 0:
        break
    else:
        print("Please provide bases larger than two and a maximum integer size larger than zero")

argument_list = ["./radix", primary_base, secondary_base, length]
radix = subprocess.run(argument_list, capture_output=True)
if radix.returncode == 0:
    print("Radix Succeeded")
else:
    print("Radix Failed")
    print(radix.stdout)
    sys.exit()

a = int(primary_base)
b = int(secondary_base)

if 2 <= a <= 20:
    primary_base = dictionary[a]
    primary_marker = primary_base[0]
else:
    primary_base = "Base " + str(a)
    primary_marker = str(a)
if 2 <= b <= 20:
    secondary_base = dictionary[b]
    secondary_marker = secondary_base[0]
else:
    secondary_base = "Base " + str(b)
    secondary_marker = str(b)

radix_average = open("radix_average.txt", 'r')

for line in radix_average:
    values = line.strip().split(',')
    averages.append(float(values[0]))
    x_values.append(int(values[1]))
plt.plot(x_values, averages, label="Actual")
del averages
gc.collect()

for x in x_values:
    approximation.append((a * log(x, a) + a) / (b * log(x, b) + b))
plt.plot(x_values, approximation, label="Approximation")
del approximation

limit = a * log(b) / (b * log(a))
plt.plot([1, x_values[-1]], [limit, limit], label="Limit")
del limit
gc.collect()

print("Plot Data Finished")

matplotlib.pyplot.xscale("log")
plt.axhline(y=1, color=(0, 0, 0), linestyle="--")
plt.title(f"Relative Radix Economy of {primary_base} and {secondary_base}")
plt.xlabel("Maximum Represented Integer")
plt.ylabel(f"Relative Average Economy ({primary_marker}/{secondary_marker})")
plt.legend()

print("Plot Definition Finished")

if not os.path.isdir("Images"):
    os.makedirs("Images")

plt.savefig(f"Images/Relative Radix Economy of {primary_base} and {secondary_base}.png", bbox_inches="tight")
plt.savefig(f"Images/Relative Radix Economy of {primary_base} and {secondary_base}.pdf", bbox_inches="tight")
plt.show()

