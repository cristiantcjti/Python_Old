from src.leilao.excecoes import LanceInvalido
from src.leilao.dominio import Usuario, Leilao
import pytest

@pytest.fixture # executa a chamada do method e transforma o resultado em uma 'variável' que podemos passar por parâmetro.
def cris():
    return Usuario('cris', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_esse_propor_um_lance(cris, leilao):
    cris.propoe_lance(leilao, 50.0)
    
    assert cris.carteira == 50.0 

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(cris, leilao):
    cris.propoe_lance(leilao, 1.0)

    assert cris.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(cris, leilao):
    cris.propoe_lance(leilao, 100.0)

    assert cris.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(cris, leilao):
    with pytest.raises(LanceInvalido):

        cris.propoe_lance(leilao, 200.0)
