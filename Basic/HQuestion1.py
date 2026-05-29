import math

r = 23.5
an = 34.5

d = 2 * r
cic = 2 * math.pi * r
s = (an / 360) * math.pi * r * r
ar = (an / 360) * cic

print("Radius:", r)
print("Diameter:", d)
print("Circumference:", cic)
print("Sector Area for", an, "degrees:", s)
print("Arc Length for", an, "degrees:", ar)
