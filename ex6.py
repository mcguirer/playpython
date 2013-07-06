# Sets variable x to a string with 10 inserted where %d is
x = "There are %d types of people." % 10
# Sets a variable called binary with the string "binary"
binary = "binary"
# Sets the do_not variable to the string "don't"
do_not = "don't"
# Sets the y variable to contain a string which also contains two strings within
y = "Those who know %s and those who %s." % (binary, do_not)
# displays variable x ont he screen
print x
# Displays variable y on the screen
print y
# Displays a string with variable x contained inside
print "I said: %r." % x
# Displays a string with variable y contained inside
print "I also said: '%s'." % y
# Sets variable hilarious to false (booleen)
hilarious = False
# Sets joke_evaluation to a string that also contains another string.  This other string isn't defined here, it will be defined later!
joke_evaluation = "Isn't that joke so funny?! %r"
# Displays variable joke_evaluation but calls variable hilarious within.  This finishes the variable above!
print joke_evaluation % hilarious
# Sets a string to variable w
w = "This is the left side of..."
# Sets a string to variable e
e = "a string with a right side."

# Mashes together variables w and e, and puts them together in left to right order! Neat!
print w + e