# webproject

This is a basic web app to illustrate deployment on Microsoft IIS or Apache + mod_wsgi


##  Microsoft IIS

### References:

- [Configure Python web apps for IIS](https://docs.microsoft.com/en-us/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2019)

- [WFastCGI](https://pypi.org/project/wfastcgi/)

For Microsoft IIS please use the webproject/web-config-template and the webproject/static/web.config files. Update them as needed.





## Apache and mod_wsgi

### References:

- [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/modwsgi/)

For Apache 2.4 and mod_wsgi use the httpd.conf.template


### Steps 

1. Download and install Apache 2.4 in `C:/Apache24`. Use [Apache Lounge](https://www.apachelounge.com/download/), or any flavor you prefer.

    - After copying files over to `C:/Apache24`, open a CMD terminal as Administrator. Navigate to `C:/Apache24` and run `bin\httpd.exe -k install` to install the Apache service. You can then navigate to `localhost` to view the test page.

    - You can start the service by running `httpd.exe -k start`

    - You can stop the services by running `httpd.exe -k stop` and restart it by `httpd.exe -k restart`

2. Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). You will need this before you run `pip install mod_wsgi`.

3. Install Python 3.7 in `C:/Python37` (you don't need to create a virtual environment)

4. Install `django`, `openpyxl`, `modwsgi` (see `install_requirements.bat`)

5. On a CMD terminal, run `mod_wsgi-express module-config`, then copy the contents and edit  `webproject/httpd.conf.template`. Edit paths to Python and your Django project.

6. On a CMD terminal, run `C:/Apache24/bin/httpd.exe -k start`, open a web browser and navigate to `localhost` (make sure `ALLOWED_HOSTS` has been updated).