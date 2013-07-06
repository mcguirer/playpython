# using the system modules, import the argv module.  argv uses command line arguments to pass data to the program
from sys import argv
# argv imports the script name followed by any arguments and sets them to variables in the program
script, filename = argv
# opents a file (named by variable filename called in argv) and sets the contents of that file to a FILE OBJECT named txt.  It's like a temp copy of that file that we can play with.
txt = open(filename)
# puts some words on the screen and displays the name of the file we're going to output to the screen
print "Here's your file %r" % filename
# performs the read command on the file object txt.  This basically reads the files content and outputs it to the screen.
print txt.read()
# Closes the file
txt.close()
# Prints some words
print "Type the filename again."
# Asks the user for some input and stores the value to a variable
file_again = raw_input("> ")
# opents a file that the user specified in the last step and creates a file object
txt_again = open(file_again)
# Prints the contents of that file using the read  command using the file object
print txt_again.read()
# Closes the file 
txt.close()
