tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

special_cat = "I'm a \n\\\tcat"

fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "Presenting: Special Cat! \n%s THE BEST CAT IN DA WORLD\a\a\a\a" % special_cat

print "%r" % fat_cat



while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,

