def checkInput():
    print("We will display a spiral.") 
    check_size = input("Please enter an integer value for the length/width of the spiral grid: ")
    try:
        int(check_size)
    except ValueError:
        print("Please enter a valid integer.")
        return checkInput()
    else:
        return int(check_size)
size = checkInput()

#for a square grid of length "size" we will record the tuples of coordinates 
#at which our symbols making up our spiral should appear
i = 0
j = 0
k = 0
coords = []
coords.append([0,0])
def calculate_coordinates(spiral_length, x, y, turns, coordinates):
    #going right
    if(spiral_length == 0):
        return coordinates
    while(x<spiral_length+(turns*2)):
        x = x + 1
        coordinates.append([y, x])
    spiral_length = spiral_length - 1
    #going down
    if(spiral_length == 0):
        return coordinates
    while(y<spiral_length+(turns*2)):
        y = y + 1
        coordinates.append([y, x])
    spiral_length = spiral_length - 1
    #going left
    turns = turns + 1
    if(spiral_length == 0):
        return coordinates
    while(x>(turns*2)):
        x = x - 1
        coordinates.append([y, x])
    spiral_length = spiral_length - 1
    #going up
    if(spiral_length == 0):
        return coordinates
    while(y>(turns*2)):
        y = y - 1
        coordinates.append([y, x])
    spiral_length = spiral_length - 1
    
    return calculate_coordinates(spiral_length, x, y, turns, coordinates)

coordinates = calculate_coordinates(size-1, i, j, k, coords)
coordinates.sort()


#printing our spiral, using our coordinates list to determine if a spiral symbol should appear
element = 0
for y in range(size):
    print('[', end = '')
    for x in range(size):
        if tuple([y, x]) == tuple(coordinates[element]):
            print('*', end = '')
            if(element < len(coordinates)-1):
                element = element + 1
        else:
            print(' ', end = '')
        if x < size-1:
            print(' ', end='')
    print(']')
