# webproject

This is a basic web app to illustrate deployment on Microsoft IIS, Apache + mod_wsgi, or nginx

# Table of Contents

- [Microsoft IIS](#microsoft-iis)

- [Apache + mod_wsgi](#apache-and-mod_wsgi)

- [nginx + Waitress](#nginx-and-waitress)


##  Microsoft IIS

- Watch on YouTube: [Deploy Django on Windows using Microsoft IIS](https://youtu.be/APCQ15YqqQ0)

### Steps

1. Install IIS on your VM or machine, and enable CGI

    - [How to Install IIS on Windows 8 or Windows 10](https://www.howtogeek.com/112455/how-to-install-iis-8-on-windows-8/)

    - [CGI](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/cgi)

2. Copy `webproject` to `C:/inetpub/wwwroot/webproject`

3. Install Python 3.7 in `C:/Python37`, and install the necessary libraries `django`, `openpyxl`, `wfastcgi`; see `webproject/install_requirements.bat`

4. Navigate to `C:/`, right-click on `Python37`, and edit `Properties`. Under Security, add `IIS AppPool\DefaultAppPool`. `DefaultAppPool` is the default app pool.

5. Enable wfastcgi

    - Open a CMD terminal as Administrator, and run the command `wfastcgi-enable`. 
    
    - Copy the Python path, and replace the `scriptProcessor="<to be filled in>"` in web-config-template with the Python path returned by `wfastcgi-enable`.

6. Edit the remaining settings in `web-config-template` then save it as `web.config` in the `C:/inetpub/wwwroot/` directory. It should NOT sit inside `webproject/`. Other settings can be modified if `webproject` does NOT sit at `C:/inetpub/wwwroot/`

    - Edit project `PYTHONPATH` (path to your project)

    - Edit `WSGI_HANDLER` (located in your `wsgi.py`)

    - Edit `DJANGO_SETTINGS_MODULE` (your `settings.py` module)

7. Open Internet Information Services (IIS) Manager. Under connections select the server, then in the center pane under Management select Configuration Editor. Under Section select system.webServer/handlers. Under Section select Unlock Section. This is required because the `C:/inetpub/wwwroot/web.config` creates a [route handler](https://pypi.org/project/wfastcgi/#route-handlers) for our project.


8. Add Virtual Directory. In order to enable serving static files map a static alias to the static directory, `C:/inetpub/wwwroot/webproject/static/`

9. Refresh the server and navigate to `localhost`



## Apache and mod_wsgi

- Watch on YouTube: [Deploy Django with Apache and mod_wsgi on Windows Server 2019](https://www.youtube.com/watch?v=frEjX1DNSpc)

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



### References:

- [Configure Python web apps for IIS](https://docs.microsoft.com/en-us/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2019)

- [WFastCGI](https://pypi.org/project/wfastcgi/)

For Microsoft IIS please use the `webproject/web-config-template` and the `webproject/static/web.config` files. Update the `web-config-template` as needed. It will be used to create a `web.config` that sits on `C:/inetpub/wwwroot/web.config`; The directory will contain all project files: `C:/inetpub/wwwroot/web.config` along with `C:/inetpub/wwwroot/webproject`.



## nginx and Waitress

- Watch on YouTube: [Deploy Django with NGINX and Waitress on Windows Server 2019](https://youtu.be/BBKq6H9Rm5g)

### Steps

1. Download and copy nginx to `C:/`.

2. Install Python 3.7 in `C:/Python37` and install 

    - `django`, `openpyxl` and [`waitress`](https://docs.pylonsproject.org/projects/waitress/en/stable/)

3. Edit `ALLOWED_HOSTS` in `settings.py`. Waitress will be running the Django server at `http://localhost:8080`.

4. Collect static files by running `python manage.py collectstatic`

5. Edit `nginx_waitress/webproeject_nginx.conf`

    - Edit the `server_name`

    - Edit the path to `/static` (and `/media` if needed)
    
    - Edit `proxy_pass` to match the server running from Waitress (i.e. `runserver.py`). This will usually be `localhost` or your IP address

6. Create two directories inside of `C:/nginx/`

    - Create `sites-enabled` and `sites-available`

    - Copy `webproject_nginx.conf` to the two directories

6. Edit `C:/nginx/conf/nginx.conf`

    - Add `include <path to your sites-enabled/webproject_nginx.conf>;`

    - Change port `80` to a non-essential port like `10`. We will need to utilize `80` for our Django project

7. Open a terminal at `C:/nginx/` and run `nginx.exe -t` to check files, and if everything is successful run `nginx.exe` to start the server

8. Open a web browser and navigate to `http://localhost`
