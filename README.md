# webproject

This is a basic web app to illustrate deployment on Microsoft IIS or Apache + mod_wsgi

# Prep

1. Install the necessary libraries

2. Update `webproject/webproject/settings.py` (e.g. add ALLOWED_HOSTS and STATIC_ROOT)

#  Microsoft IIS

## References:

- [Configure Python web apps for IIS](https://docs.microsoft.com/en-us/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2019)

- [WFastCGI](https://pypi.org/project/wfastcgi/)

For Microsoft IIS please use the webproject/web-config-template and the webproject/static/web.config files. Update them as needed.

# Apache and mod_wsgi

## References:

- [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/modwsgi/)

For Apache 2.4 and mod_wsgi use the httpd.conf.template