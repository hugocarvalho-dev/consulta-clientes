from PyQt5 import QtWidgets
import pyperclip as pc

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração básica
        self.setWindowTitle("Localize")
        self.setFixedSize(820, 380)

        # Campo de busca
        self.input = QtWidgets.QLineEdit(self)
        self.input.setPlaceholderText("Digite o telefone...")
        self.input.setGeometry(260, 40, 200, 35)

        # Botão de consulta (ilustrativo)
        self.btn = QtWidgets.QPushButton("Consultar", self)
        self.btn.setGeometry(470, 40, 90, 35)
        self.btn.clicked.connect(self.search)

        # Área que exibirá os dados consultados
        self.info_name = self._make_copy_label(40, 120)
        self.info_cnpj = self._make_copy_label(40, 160)
        self.info_cnae = self._make_copy_label(40, 200)
        self.info_address = self._make_copy_label(40, 240)

    def _make_copy_label(self, x, y):
        """Cria um QLabel clicável que copia o conteúdo ao clicar."""
        label = QtWidgets.QLabel("", self)
        label.setGeometry(x, y, 700, 25)
        label.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        label.mousePressEvent = lambda event, l=label: pc.copy(l.text())
        return label

    def search(self):
        """
        Lógica fictícia apenas para demonstrar funcionalidade.
        Aqui, no app real, você consulta o banco .accdb.
        """
        telefone = self.input.text()

        # Exemplo de preenchimento (dados mock)
        self.info_name.setText("Nome da Empresa Exemplo")
        self.info_cnpj.setText("00.000.000/0000-00")
        self.info_cnae.setText("6204-0/00 - Consultoria em TI")
        self.info_address.setText("Rua Exemplo, 123 - Centro")

if __name__ == "__main__":
    import sys
    from PyQt5 import QtCore

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
