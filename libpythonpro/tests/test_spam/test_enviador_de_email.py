import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario', ['foo.bar@gmail.com', 'marcospaulo.silvaviana@gmail.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    # destinatario = ['foo.bar@gmail.com','marcospaulo.silvaviana@gmail.com']
    resultado = enviador.enviar(
        destinatario,
        'samaralivia.tomesousa@gmail.com',
        'teste do curso python pro',
        'to indo em frente'
    )
    assert destinatario in resultado


@pytest.mark.parametrize('destinatario', ['', 'marcospaulo'])
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'samaralivia.tomesousa@gmail.com',
            'teste do curso python pro',
            'to indo em frente'
        )
