# code to calculate area

print('Calculate the area of a rectangle')
#
# get height and width
height = input('Type height of reactangle: ')
width = input('Type height of reactangle: ')
# convert from string to numeric values
height = float(height)
width = float(width)
# do are calculation
rect_area = width * height

print('The area of a rectangle', width, 'by', height, 'is', rect_area)


print('\n\nCalculate the area of a triangle')
#
# get height and base width
height = input('Type height of triangle: ')
base = input('Type width of base of triangle: ')
# convert from string to numeric values
height = float(height)
base = float(base)
# do are calculation
triangle_area = (1/2) * base * height

print('\nThe area of a triangle', width, 'high with base', base, 'is', triangle_area)



