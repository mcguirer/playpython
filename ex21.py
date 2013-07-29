def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def devide(a, b):
	print "DEVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just function!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, devide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"

w1 = devide(iq, 2)
w2 = multiply(weight, w1)
w3 = subtract(height, w2)
w4 = add(age, w3)

print "I think I figured it out!  The answer is %d" % w4

calc1 = 24 + 16 / 45 * 19 * 2

calc = add(24, devide(16, (multiply(45, (multiply(19, 2))))))

print "So, this: %d should equal that: %d" % (calc1, calc1)
