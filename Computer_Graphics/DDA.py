
#_____________________step-1: Start___________________________________

# Python program for DDA line generation
from matplotlib import pyplot as plt 

def DDA():

    # _____________________step-2: input__________________________________

    (x0 , y0) = (0,0) 
    (xn , yn) = (4, 8)

    #______________________step-3: find absolute differences of dx and dy and Both slope__________________

    dx = abs(x0 - xn) 
    dy = abs(y0 - yn) 
    m = dy/dx

    #______________________step-4: check slope condition m>1:true or false and repeat a till xi <= xn and yi <= yn in a table show_____________

    steps = max(dx, dy) + 1
    # start with 1st point 
    x = float(x0) 
    y = float(y0)

    # DDA Function for line generation 
    x_coordinates = [] 
    y_coordinates = [] 

    # calculate the increment in x and y 
    xinc = x0
    yinc = y0
    if m < 1:
        print('xi', ' ', 'Yi', '  ', 'Xi+1', '', 'Yi+1', '     ', '(x,y)')
        for i in range(steps): 
            # append the x,y coordinates in respective list 
            x_coordinates.append(x) 
            y_coordinates.append(y) 
            print(x, "  ", y, end=" ")
            # increment the values 
            x += xinc + 1
            y += yinc + m
            print("  ",x, " ", y, "   ", "(",x, ",", y,")")
        
    else:
        print('xi', ' ', 'Yi', '  ', 'Xi+1', '', 'Yi+1', '     ', '(x,y)')
        for i in range(steps): 
            # append the x,y coordinates in respective list 
            x_coordinates.append(x) 
            y_coordinates.append(y) 
            print(x, "", y, end=" ")
            # increment the values 
            x += xinc + (1/m) 
            y += yinc + 1
            print("  ",x, " ", y, "   ", "(",x, ",", y,")")

    #___________________________step-5: drow graph________________________________________

    # plot the line with coordinates list 
    plt.plot(x_coordinates, y_coordinates, marker="o", markersize=5, markerfacecolor="b") 
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("DDA line generation")
    plt.grid(True)
    plt.show() 

DDA()