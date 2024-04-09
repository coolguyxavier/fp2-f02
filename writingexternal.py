# - FP2-F02 - Writing to External Files - #
# - Xzavier Moosomin - #
# - 04/09/2024 - #

# - Developer Notes - #
# Not gonna lie, this is kind of lightwork.
# Dunno why I couldn't do it on my own

# - Imports - #

import time

# - Functions - #

def createfile(): # just to create file, i guess...?
    file1 = open('openedfile.txt', 'w')
    print("Creating file...")
    time.sleep(1)
    print("File Created.")
    time.sleep(1)
    print("Closing file.")
    
    file1.close()
    
def writefile():
    file1 = open('openedfile.txt', 'w')
    file1.write("Time to get funky.\n")
    file1.write("Perhaps we'll get some user input...?\n")
    
    print("Add something to the file yourself.")
    print("What do you want to write?\n")
    
    userinp = input(">")
    file1.write(userinp + "\n")
    
    file1.write("We did it!\n")
    
    file1.write("Now we're closing it.")
    print("File closed.")
    
    file1.close()
    
def appendfile():
    file1 = open('openedfile.txt', 'a')
    print("Opening file, again.")
    file1.write("\nNow we're opening it.")
    file1.write("\nAgain.")
    
    file1.write("\nHow are you?")
    
    file1.write("\nI'm bored now.")
    
    print("Now we're closing it, again.")
    file1.write("\nClosing file.")
    file1.close()

# - Main Code - #

createfile()
writefile()
appendfile()
