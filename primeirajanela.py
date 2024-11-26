# A biblioteca sys(sistema) nos ajuda a gerenciar a janela no sistema operacional. Biblioteca nativa do python.
import sys
# importar as bibliotecas do pyqt para criar a janela e os elementos gráficos, tais como: label, caixas de textos, botões e outros.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
#import no começo seria para importar tuudo. já o from eu irei ditar oque será importado.

# Para construir a nossa janela, iremos montar uma classe que terá todos os itens da janela. Esta classe será chamada para executar a janela e exibi-la em tela.
class Janela(QWidget):
   
    # Função __init__ faz  o star da janela, ou seja faz a janela executar/ inicia.
    # O parâmetro self, faz referência a própria janela.
    def __init__(self):
       
        # O comoando super faz referência ao QWidget que foi chamando na construção da janela e inicia uma cópia para classe janela.
        super().__init__()

        # Definindo a posição em x e y e também o tamanho da janela.
        # O comando setGeometry pede os seguintes valores: x = posição horizontal da abertura da janela,
        # y = posição vertical da abertura da janela,
        # w = largura da janela,
        # h =  altura da janela.
        self.setGeometry(50,100,600,500) # Set = manda os dados, Get = pega os dados.
        self.setFixedSize(600,500)
        
        # Vamos fazer a chamada do layout vertical para adicionar os controles: label, editline e button.
        self.v_layout = QVBoxLayout()
        # Vamos criar uma label para o nome cliente
        # ------------ nome cliente--------------------------------
        self.label_name = QLabel("Nome completo:")
        self.label_name.setStyleSheet("QLabel{font-size:20pt;color:#004fff}")
        self.edit_name = QLineEdit()
        self.edit_name.setStyleSheet("QLineEdit{padding:4px}")

        #--------------------Email Cliente-----------------------------
        self.label_email = QLabel("Número do cartão de credito:")
        self.label_email.setStyleSheet("QLabel{font-size:20pt;color:#004fff}")
        self.edit_email = QLineEdit()
        self.edit_email.setStyleSheet("QLineEdit{padding:4px}")

        #------------- CPF do cliente-------------
        self.label_cpf = QLabel("CPF:")
        self.label_cpf.setStyleSheet("QLabel{font-size:20pt;color:#004fff}")
        self.edit_cpf = QLineEdit()
        self.edit_cpf.setStyleSheet("QLineEdit{padding:4px}")

        #------------- Telefone --------------
        self.label_fone = QLabel("Código de segurança (CCV):")
        self.label_fone.setStyleSheet("QLabel{font-size:20pt;color:#004fff}")
        self.edit_fone = QLineEdit()
        self.edit_fone.setStyleSheet("QLineEdit{padding:4px}")

        #------------- Idade do cliente ------------
        self.label_idade = QLabel("Data de Vencimento:")
        self.label_idade.setStyleSheet("QLabel{font-size:20pt;color:#004fff}")
        self.edit_idade = QLineEdit()
        self.edit_idade.setStyleSheet("QLineEdit{padding:4px}")

        # -------------Adicionar o botão cadastrar ------------
        self.button_cadastrar = QPushButton("Verificar")
        self.button_cadastrar.setStyleSheet("QPushButton{width:200px}")


        #-------------- Componentes do layout --------
        # Adicionar a label nome no layout
        self.v_layout.addWidget(self.label_name)
        # Adicionar a edit nome no layout
        self.v_layout.addWidget(self.edit_name)
        # Adicionar a edit email
        self.v_layout.addWidget(self.label_email)
        self.v_layout.addWidget(self.edit_email)
        # Adicionar a edit cpf
        self.v_layout.addWidget(self.label_cpf)
        self.v_layout.addWidget(self.edit_cpf)
        # Adicionar a edit telefone
        self.v_layout.addWidget(self.label_fone)
        self.v_layout.addWidget(self.edit_fone)
        # Adicionar a edit idade
        self.v_layout.addWidget(self.label_idade)
        self.v_layout.addWidget(self.edit_idade)
        # Adicinar botão na tela
        self.v_layout.addWidget(self.button_cadastrar)
        

        # Adicionar o layout na tela
        self.setLayout(self.v_layout)
app = QApplication(sys.argv) # Argv = Disco, Memória e Video.
jan = Janela()
jan.show() #(.show) mostra ela na tela. Caso ao contrario ficará em segundo plano.
app.exec_()