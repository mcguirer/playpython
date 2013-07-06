from sys import argv
from os.path import exists

script, from_file, to_file = argv



# indata = open(from_file).read()

print "Does the output file exist? %r" % exists(to_file)

print "Ready to copy %s to %s, %d bytes long. RETURN to continue, CTRL-C to abort." % (
	from_file, to_file, len(open(from_file).read())
	)
raw_input()

open(to_file, 'w').write(open(from_file).read())

print "Alright, all done."