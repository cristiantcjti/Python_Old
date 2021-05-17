from src.leilao.excecoes import LanceInvalido
from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao


# method setUp // chamado antes de cada função
# method tearDown // chamado logo após execução do teste
# method setUpClass // chamado no momento da criação da classe
# method tearDownClass // chamado após o último teste da classe ser executado

#Classe de equivalencia, quando os testes são parecidos, apenas criamos situacoes diferentes
class TestLeilao(TestCase):
    # CRIAÇÃO DE CENÁRIO DE TESTES, QUANDO ALGO É REPETIDO EM TODOS OS PONTOS DE TESTE.  
    def setUp(self): 
        self.paulo = Usuario('paulo', 500.0)  
        self.lance_do_paulo = Lance(self.paulo, 150.0)    
        self.leilao = Leilao('Celular')          


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        cris = Usuario('cris', 500.0)
        lance_do_cris = Lance(cris, 100.0)

        self.leilao.propoe(lance_do_cris)
        self.leilao.propoe(self.lance_do_paulo)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        
        with self.assertRaises(LanceInvalido):
            cris = Usuario('cris', 500.0)
            lance_do_cris = Lance(cris, 100.0)
            
            self.leilao.propoe(self.lance_do_paulo)
            self.leilao.propoe(lance_do_cris)

    def test_deve_retornar_o_mesmo_valor_para_o_mairo_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_paulo)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_mairo_e_menor_lance_quando_leilao_tiver_tres_lances(self):
        cris = Usuario('cris', 500.0)
        marcos = Usuario('marcos', 500.0)
        
        lance_do_cris = Lance(cris, 100.0)
        lance_do_marcos = Lance(marcos, 200.0)

        self.leilao.propoe(lance_do_cris)
        self.leilao.propoe(self.lance_do_paulo)
        self.leilao.propoe(lance_do_marcos)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance) 

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_paulo)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        joao = Usuario('joan', 500.0)

        lance_do_joao = Lance(joao, 200.0)

        self.leilao.propoe(self.lance_do_paulo)
        self.leilao.propoe(lance_do_joao)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebidos)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_paulo200 = Lance(self.paulo, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_paulo)
            self.leilao.propoe(lance_do_paulo200)
            quantidade_de_lances_recebidos = len(self.leilao.lances)
            self.assertEqual(1, quantidade_de_lances_recebidos) 


