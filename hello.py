def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = "OKKKKK"
    for each in environ['QUERY_STRING']:
        if each == '&':
            body += "\n"
        else:
            body += each

    start_response(status, headers)
    return body
