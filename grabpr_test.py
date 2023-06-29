import requests
import re
import time
import csv


with open('test.html', encoding="utf-8") as file:
        file_data = file.read()
p = re.compile('<a href="(/projects/[\w-]*\?ref=https.*)">(?!orig.video.ria.ru)')
link_list = p.findall(file_data)
print ("Number of projects: ", len(link_list))
for link in link_list:
        print (link)

