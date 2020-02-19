
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


if __name__ == "__main__":
    flag()