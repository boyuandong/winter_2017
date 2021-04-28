# CMPUT 175 Winter 2013 Lab 2 Exercise 2
# This program is used to calculate the worth of an automobile.

class Automobile:
    
    # Constructor:
    def __init__(self, length, horsepower, color):
        self.__length = length
        self.__horsepower = horsepower
        self.__color = color
        
    # Returns the length:
    def get_length(self):
        return self.__length
    
    # Returns the horsepower:
    def get_horsepower(self):
        return self.__horsepower
        # TODO: You must implement this method!
    
    # Returns the color:
    def get_color(self):
        return self.__color
        # TODO: You must implement this method!
    
    #Returns the worth:
    def get_worth(self):
        if self.__color =='red':
            color_factor=3
        elif self.__color =='yellow' or self.__color=='blue':
            color_factor=2
        else:
            color_factor=1
        worth=int(self.__horsepower)*int(self.__length)*int(color_factor)*10
        return worth
        # TODO: You must implement this method!
    
# Main function, which asks the user for the length, horsepower, and color of
# an automobile, and will then print out the worth of that automobile:
def main():
    print('Example interaction with the program:')
    length=input("Enter automobile's length in meters: ")
    housepower=input("Enter automobile's horsepower: ")
    color=input("Enter automobile's color: ")
    automobile=Automobile(length,housepower,color)
    print("This automobile is worth $"+str(automobile.get_worth())+".")
    # TODO: You must implement this function!

main()