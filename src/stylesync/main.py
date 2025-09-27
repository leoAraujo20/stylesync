from wsgiref.simple_server import make_server

def aplicacao(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    html = '''
            <html>
            <header>Olá Mundo</header>
            </html>
    '''
    return [html.encode('utf-8')]


make_server('', 8000, aplicacao).serve_forever()    