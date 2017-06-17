#!/usr/bin/python

import urllib
from bs4 import BeautifulSoup

site= "http://192.168.1.11/wp/wp-admin/install.php?language=en_US"
filename=raw_input("Enter Filename For Password list ? ")
print ("Wait Im Make 100 Password D:")
for item in range(0,100):
        res = urllib.urlopen(site)
        soup = BeautifulSoup(res.read(), 'html.parser')
        file = open(str(filename), "a+")
        for link in soup.find_all('input'):
                if((link.get('data-pw'))==None):
                        continue
                else:
                        passwords = link.get('data-pw')
                        print str(item)+")"+str(passwords)
                        file.write(str(passwords)+"\n")







