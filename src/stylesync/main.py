from wsgiref.simple_server import make_server

def aplicacao(environ, start_response):
    produtos = [
        {'nome': 'Camiseta', 'preco': 29.90},
        {'nome': 'Caneca', 'preco': 15.90},
        {'nome': 'Mouse', 'preco': 79.90},
        {'nome': 'Impressora', 'preco': 299.90},
    ]
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    with open('src/stylesync/static/html/index.html', 'r') as arquivo:
        html = arquivo.read()
    
    html_produtos = ''
    for produto in produtos:
        html_produtos += f'<li>{produto["nome"]} - R$ {produto["preco"]}</li>\n'
    html = html.replace(r'{{ Produtos }}', html_produtos)
    return [html.encode('utf-8')]

make_server('', 8000, aplicacao).serve_forever()    