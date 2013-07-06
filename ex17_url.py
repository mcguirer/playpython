import urllib

website = urllib.urlopen("http://www.google.com")

print website.read()