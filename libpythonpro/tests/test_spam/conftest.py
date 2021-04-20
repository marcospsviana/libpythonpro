import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


@pytest.fixture(scope='module')
def conexao():
    conexao_fixture = Conexao()
    yield conexao_fixture
    conexao_fixture.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_fixture = conexao.gerar_sessao()
    yield sessao_fixture
    sessao_fixture.roll_back()
    sessao_fixture.fechar()

# @pytest.fixture
# def usuario():
#     usuario_fixture = usuario.enviar_emails()
#     usuario_fixture.enviar()