from unittest.mock import Mock

import pytest
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


# class EnviadorMock(Enviador):
#     def __init__(self):
#         super().__init__()
#         self.parametros_de_envio = None
#         self.quantidade_emails_enviados = 0
#
#     def enviar(self, remetente, destinatario, titulo, mensagem):
#         self.parametros_de_envio = (remetente, destinatario, titulo, mensagem)
#         self.quantidade_emails_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='marcosps', email='marcospsviana@gmail.com'),
            Usuario(nome='paulo', email='paulo.silva@gmail.com')
        ],
        [
            Usuario(nome='marcos', email='marcospaulo.silvaviana@gmail.com'),
        ]
    ]
)
def test_equantidade_de_spam(sessao, usuarios):
    enviador = Mock()
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'samaralivia.tomesousa@gmail.com',
        'teste do curso python pro',
        'to indo em frente'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='marcos', email='marcospaulo.silvaviana@gmail.com')
    enviador = Mock()
    sessao.salvar(usuario)
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'samaralivia.tomesousa@gmail.com',
        'teste do curso python pro',
        'to indo em frente'
    )
    enviador.assert_called_with(
        'samaralivia.tomesousa@gmail.com',
        'marcospaulo.silvaviana@gmail.com',
        'teste do curso python pro',
        'to indo em frente'
    )
