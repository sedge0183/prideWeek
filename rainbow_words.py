
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


if __name__ == "__main__":
    rainbowWords("OMG It's actually working!!! This is amazing!!", 3)