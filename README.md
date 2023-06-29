# cdnprojects
Tool to parse html pages from https://selfcare.cdnnow.ru, to collect data about CDN projects and to save data in the “project.csv” file

The structure of the configuration “auth.json” file:
```
{
  "auth": {
    "login": "",
    "password": ""
  },
  "useragent": {
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
  },
  "urls": {
    "initialURL": "https://selfcare.cdnnow.ru", 
    "loginURL": "https://selfcare.cdnnow.ru/login",
    "projectsURL": "https://selfcare.cdnnow.ru/clients/4-4/projects?page=1&items=100" 
  }
}
```
An example of the result “project.csv” file:
```
Project name;Project service name;Project ID;Origin;CDN
Site1;user11111;6fffff-fff-4fffe4a-8206-d4bb7f5fffffff4;img.site1.ru;cdn.img.site1.ru
```
Comments:
1. Useragent isn't use in the current version
2. The parcing data also printed in stdout
 

