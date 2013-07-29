print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with login so firmly planted
cannot discern \n the needs of love
nor comprehend passion from inuition
and require an explaniation
\n\twhere there is none.
"""

print "=============="
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	poop = started * 500
	cans = poop / 1000
	toilets = cans / 100
	return poop, cans, toilets

start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (jelly_beans, jars, crates)
 
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)