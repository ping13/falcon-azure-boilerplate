"""
This script runs the application using a development server.
"""

import falcon

import functions.hello


app = falcon.API()

hello = functions.hello.Resource()

app.add_route('/', hello)

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
