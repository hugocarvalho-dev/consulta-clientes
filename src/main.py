"""
Localize – Consulta de clientes em banco Access com interface PyQt5
Versão simplificada para portfólio
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui, QtCore
import pyodbc
import threading
import sys

DATABASE_PATH = "Localize.accdb"   # Exemplo ilustrativo

class Localizador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()                     # Interface carregada via .ui
        self.btn_consultar.clicked.connect(self.iniciar_consulta)

    def setup_ui(self):
        """
        Aqui você carregaria o arquivo .ui gerado pelo Qt Designer.
        Mantido vazio na versão de portfólio para focar na lógica.
        """
        pass

    def iniciar_consulta(self):
        numero = self.campo_telefone.text().strip()
        if not numero:
            self.exibir_mensagem("Digite um número válido.")
            return

        # Thread evita travar a interface
        threading.Thread(target=self.consultar_base, args=(numero,), daemon=True).start()

    def consultar_base(self, numero):
        try:
            conn = pyodbc.connect(
                r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                f"DBQ={DATABASE_PATH};"
            )
            cursor = conn.cursor()

            consulta = f"""
                SELECT * 
                FROM Base 
                WHERE Telefone_1 LIKE '%{numero}%'
                   OR Telefone_2 LIKE '%{numero}%'
                   OR Telefone_3 LIKE '%{numero}%'
            """

            resultado = cursor.execute(consulta).fetchone()

            if resultado:
                self.exibir_resultado(resultado)
            else:
                self.exibir_mensagem("Nenhum registro encontrado.")

        except Exception:
            self.exibir_mensagem("Erro ao consultar o banco de dados.")

    def exibir_resultado(self, dados):
        """
        Exibe os dados na interface (campos removidos para simplificação).
        """
        print("Resultado encontrado:", dados)

    def exibir_mensagem(self, texto):
        QMessageBox.information(self, "Localize", texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Localizador()
    janela.show()
    sys.exit(app.exec_())
