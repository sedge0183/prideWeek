'''
Rainbows with escape codes

What are they?
Used to control elements within the terminal (OS based rather than python based)

What are we going to do with them?
We will be using them to change the colour of the text within our terminal
It tells the terminal to output in a different colour until told otherwise 
(won't switch back to white another colour until specified to)


"\033" is the escape key for python. Used in a string before the parameters
Colours involve a "[" with a number afterward. This number determines which colour is used
An "m" is needed to finish off the full code


"\033[31m" is an example code for red

\033 is the escape code
31 is the number that gives red
"[" and "m" are also needed
 
'''

def colour():
    print("\033[31mRed")
    print("This will also be in Red")
    print("\033[93mYellow")
    print("\033[36mCyan")


if __name__ == "__main__":
    colour()