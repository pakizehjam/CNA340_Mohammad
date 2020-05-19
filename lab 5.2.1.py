import math

# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wallHeight = float(input('Enter wall height (feet):\n'))
wallWidth = float(input('Enter wall width (feet):\n'))
wallArea = float(wallHeight * wallWidth)
#print('Wall area: %f square feet' %(wallArea))
print('Wall area:', int(wallArea), 'square feet')

# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall: a gallon of paint covers 350 sq ft
area_per_gallon = float(1 / 350)
amt_paint = wallArea * area_per_gallon
# print(area_per_gallon)
#print('Paint needed: %f gallons' % (amt_paint))
print('Paint needed:',format(amt_paint,'.2f'), 'gallons')


# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
paintCans = math.ceil(amt_paint)
print('Cans needed: %d can(s)' % (paintCans))

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
userColor = input('\nChoose a color to paint the wall:\n')
if userColor in paintColors:
  price = paintColors[userColor]
  totalPrice = int(price) * paintCans
  print('Cost of purchasing %s paint: $%d' % (userColor, totalPrice))
else:
  print('Invalid Color Choice!')
