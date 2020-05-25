from waitress import serve

from webproject.wsgi import application
# documentation: https://docs.pylonsproject.org/projects/waitress/en/stable/api.html

if __name__ == '__main__':
    serve(application, host = '0.0.0.0', port='8080')
