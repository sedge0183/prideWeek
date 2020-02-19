import os
import time

# Global variable to hold all the colorus for the rainbow
#           Red         Orange?     Yellow      Green       Blue        Violet  
colours = ["\033[91m", "\033[33m", "\033[93m", "\033[32m", "\033[34m", "\033[35m"]


def flag():
    global colours # Use the global variable colours
    line = 50 * "\u2588" # Unicode for the "█" character, multiplied by 50

    for colour in colours:
        coloured_line = colour + line
        
        print(coloured_line)
        print(coloured_line)


def rainbowWords(string, i=0):
    global colours # Use the global variable colours

    for char in string:
        # Add the colour and he character, end="" is to keep it on the same line
        print(colours[i] + char, end="")

        # Increase index "i" to go to next colour, the modulus is to loop the index back to the beginning colour
        i = (i + 1) % len(colours)
    
    print() # Need to move to the next line at the end of the string


def changingWords(string, speed=0, i=0):
    global colours

    # Formula for speed. Varialbe "speed"  should range from 0 - 100, 100 being fastest
    stop_time = 1.1 - (speed / 100)

    # To kill a process, use "Ctrl + C"
    while True:
        os.system("clear") # Clears the screen, preps for "next frame"
        rainbowWords(string, i) # Use the funciton above
        
        # Tell program to stop for a period of time
        time.sleep(stop_time)
        # Increase "i" for next colour, modulus to loop back to the beginning of colours
        i = (i + 1) % len(colours)


if __name__ == "__main__":
    changingWords("Use \"Ctrl\" + C to kill a process", 100) # This string is here so I don't forget while presenting