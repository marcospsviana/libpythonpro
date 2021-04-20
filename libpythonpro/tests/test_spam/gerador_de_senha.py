import string


def gerar_senha(quantidade):
    _caracteres = string.printable.replace(' ','')
    senha_gerada = []
