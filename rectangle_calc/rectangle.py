import calculate

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate.area(length, width)
parameter = calculate.parameter(length, width)

print(f"The area of the rectangle is: {area}.")
print(f"The parameter of the rectangle is: {parameter}.")