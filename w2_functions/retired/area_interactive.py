from area_functions import area_rectangle, area_triangle

# import area_functions

print('Calculate the area of a rectangle')
# input height and width
height = float(input('Type height of reactangle: '))
width = float(input('Type height of reactangle: '))
# get area
area_r = area_rectangle(height, width)
# print the result
print('The area of a rectangle', width, 'by', height, 'is', area_r)



print('\n\nCalculate the area of a triangle')
#
# get height and base width
height = float(input('Type height of triangle: '))
base = float(input('Type width of base of triangle: '))
# get area
area_t = area_triangle(base, height)
#print the result
print('\nThe area of a triangle', width, 'high with base', base, 'is', area_t)



