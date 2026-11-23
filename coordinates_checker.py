x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Point is at the Origin.")

elif y == 0:
    print("Point lies on the X-axis.")

elif x == 0:
    print("Point lies on the Y-axis.")

elif x > 0 and y > 0:
    print("Point lies in Quadrant 1")

elif x < 0 and y > 0:
    print("Point lies in Quadrant 2")

elif x < 0 and y < 0:
    print("Point lies in Quadrant 3")

else:
    print("Point lies in Quadrant 4")