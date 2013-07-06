days = "Mon Tue Wed Thur Fri Sat Sun"
# /n makes a new line and needs no space padding
months = "Jan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6. %s
""" % days
