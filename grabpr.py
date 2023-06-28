import requests
import re
import json
import time
import csv


with open('auth.json') as file:
    json_file = json.load(file)
    login = json_file['auth']["login"]
    password = json_file['auth']["password"]
    agent = json_file['useragent']['useragent']
    initialURL = json_file['urls']['initialURL']
    loginURL = json_file['urls']['loginURL']
    projectsURL = json_file['urls']['projectsURL']
headers = {
    'User-Agent': agent
}
session = requests.Session()
session.headers.update(headers)
response = session.get(loginURL)
p = re.compile('_csrf_token.*value=.([\w-]*)', re.DOTALL)
m = p.search(response.text)
csrf_token = m.groups()[0]
print ("CSRF Token:", csrf_token)
data = {
    'username': login,
    'password': password,
    '_csrf_token': csrf_token
}
response = session.post(initialURL, data=data)
print ("Status code: ", response.status_code)
time.sleep(5)
response = session.get(projectsURL)
time.sleep(3)
print ("------------------------------------")
print (response.text)
print ("------------------------------------")
p = re.compile('<a href="(/projects/[\w-]*\?ref=https.*)">')
link_list = p.findall(response.text)
print ("Number of projects: ", len(link_list))
project_data = [['Project name', 'Project service name', 'Project ID', 'Origin', 'CDN']]
iter = 0
for link in link_list:
    response = session.get(initialURL + link)
    time.sleep(3)
    detail1 = response.text
    p = re.compile('<label.*?>Имя проекта</label>.*?<input.*?value=\"([\w.]*)\"', re.DOTALL)
    m = p.search(detail1)
    project_name = (m.groups()[0]).strip()
    print ("Имя проекта: ", project_name)
    p = re.compile('<label.*?>Служебное имя проекта</label>.*?<div.*?>([\w\s]*)</div>', re.DOTALL)
    m = p.search(detail1)
    project_ser_name = (m.groups()[0]).strip()
    print ("Служебное имя проекта: ", project_ser_name)
    p = re.compile('<input.*?id=\"edit_form_project_origins0edit_name\".*?value=\"([\w.]*)\"', re.DOTALL)
    m = p.search(detail1)
    origin = (m.groups()[0]).strip()
    print ("Origin: ", origin)
    p = re.compile('/projects/([\w-]*)\?', re.DOTALL)
    m = p.search(link)
    project_id = (m.groups()[0]).strip()
    print ("Project ID: ", project_id)
    detail2_link = re.sub('\?ref', '/ssl?ref', link)
    response = session.get(initialURL + detail2_link)
    time.sleep(3)
    detail2 = response.text
    p = re.compile('<input.*?id=\"edit_form_server_name\".*?value=\"([\w\s.]*)\"', re.DOTALL)
    m = p.search(detail2)
    cdn = (m.groups()[0]).strip()
    print ("CDN: ", cdn)
    project_data.append([project_name, project_ser_name, project_id, origin, cdn])
    iter += 1
    if iter > 3:
         break

with open("projects.csv", "w", newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=";")
        for line in project_data:
            csvwriter.writerow(line)
