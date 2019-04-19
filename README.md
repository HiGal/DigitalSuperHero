# Marketplace for contractors and customers of the power grid company

The system **allows customers to** make an application for power supply and **allows contractors to** compete for customer's applications.
### Contributors:
* [Farit Galeev](mailto:f.galeev@innopolis.ru "Send mail")
* [Lenar Gumerov](mailto:l.gumerov@innopolis.ru "Send mail")
* [Ruslan Shakirov](mailto:r.shakirov@innopolis.ru "Send mail")
* [Anastasiya Gromovoa](mailto:a.gromova@innopolis.ru "Send mail")
------
## Getting Started
### Starting server
#### Execute commands:

*Unix Bash (Linux, Mac, etc.)*:
```
$ export FLASK_APP=app.py
$ flask run -h 0.0.0.0
```
*Windows CMD*:
```
> set FLASK_APP=app.py
> flask run -h 0.0.0.0
```
*Windows PowerShell*:
```
> $env:FLASK_APP = "app.py"
> flask run -h 0.0.0.0
```
### Testing service
After starting the server link to site is host's IPv4 in network and port ```5000```

__Example:__
```
10.240.17.219:5000
```
If you are trying to access to the site on the same machine as the server is running, do not use ```localhost``` or ```127.0.0.1```, because it will break URLs in QR-codes. Use your network address or ip instead.
