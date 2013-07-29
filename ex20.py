# makes it so you can pull variables from the command like
from sys import argv
# defines what is pulled from the command line.
# in this case it is the name of thr file and a variable called input_file
script, input_file = argv
# a function that outputs the entire file
def print_all(f):
	print f.read()
# function that brings the file marker back to the beginning
def rewind(f):
	f.seek(0)
# functiokn that reads one line at a time
def print_a_line(line_count, f):
	print line_count, f.readline()
# opens the file and sets it to a variable
current_file = open(input_file)

print "First let's print the whole file:\n"
# outputs thr entire file using a function
print_all(current_file)

print "Now let's rewind, like a tape."
# brings file marker back
rewind(current_file)

print "Let's print three lines:"
# prints a line, appends line count and prints untik 3 linea are printed
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
