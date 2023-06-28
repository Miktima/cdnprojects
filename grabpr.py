import requests
import re
import json


with open('auth.json') as file:
        json_file = json.load(file)
        login = json_file['auth']["login"]
        password = json_file['auth']["password"]
        agent = json_file['useragent']['useragent']
        initialURL = json_file['urls']['initialURL']
        projectsURL = json_file['urls']['projectsURL']
headers = {
    'User-Agent': agent
}
session = requests.Session()
session.headers.update(headers)
response = session.get(initialURL)
print (response.text)
p = re.compile('_csrf_token[\w\s]*>')
m = p.search(response.text)
print ("RE:", m.group())
data = {
    'username': login,
    'password': password,
    '_csrf_token': 'OS X Chrome v.89.0.4389.90 3a7a0'
}
