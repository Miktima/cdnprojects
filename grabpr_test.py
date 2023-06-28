import requests
import re
import time
import csv


with open('detail2.html', encoding="utf-8") as file:
        file_data = file.read()
p = re.compile('<input.*?id=\"edit_form_server_name\".*?value=\"([\w\s.]*)\"', re.DOTALL)
m = p.search(file_data)
print ("mmmm: ", m)
CDN = (m.groups()[0]).strip()
print ("CDN: ", CDN)


