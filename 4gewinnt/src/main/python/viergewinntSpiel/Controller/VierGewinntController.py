import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from viergewinntSpiel.view import VierGewinntView as MyView
from viergewinntSpiel.Model import Online, Offline


# TODO: Model-File erstellen, Model-Klasse implementieren und hier importieren

# TODO: View designen und generieren

# TODO: Klasse und Methoden Kommentieren

class MyController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.myForm = MyView.Ui_VierGewinnt()
        self.myForm.setupUi(self)
        self.besetzen = self.myForm.feldBesetzen.clicked.connect(self.besetzeFeld)
        self.spinner = self.myForm.spinBox
        self.beendenButton = self.myForm.beenden.clicked.connect(self.beenden)
        self.serviceBox = self.myForm.webserviceBox.clicked.connect(self.check)
        self.textField = self.myForm.textBrowser
        self.neu = self.myForm.neueSpiel.clicked.connect(self.neuesspiel)
        self.strategy = Online.OnlineService()
        self.fields = ' ' * 16
        self.display()
        # TODO: Model-Objekt erstellen und Button-Event Handler hinzufuegen

    def display(self):

        output = '------\n|'
        output += self.fields[0] + self.fields[1] + self.fields[2] + self.fields[3] + "|\n|"
        output += self.fields[4] + self.fields[5] + self.fields[6] + self.fields[7] + "|\n|"
        output += self.fields[8] + self.fields[9] + self.fields[10] + self.fields[11] + "|\n|"
        output += self.fields[12] + self.fields[13] + self.fields[14] + self.fields[15] + "|\n"
        output += '------'
        # TODO: Gewinn-Nachricht anzeigen, falls jemand gewonnen hat
        if self.strategy.check(self.fields) != ' ':
            output += "\n Der Gewinner ist: "+self.strategy.check(self.fields)
        # TODO: in Textfeld anzeigen
        self.textField.setText(output)

    # TODO: bei Buttonklick Feld besetzen, Model aufrufen (Webservice abfragen) und Ergebnis anzeigen
    def besetzeFeld(self):
        print('BESETZEN ' + str(self.spinner.value()))
        self.fields = self.strategy.send(self.fields, self.spinner.value())
        self.display()

    def beenden(self):
        sys.exit()

    def neuesspiel(self):
        print('Neues Spiel')
        self.fields = ' ' * 16
        self.display()

    def checkWin(self):
        self.textField.append('<p>Hallo</p>')
        out = self.strategy.check(self.fields)
        print("CONTROLLER CHECK "+out)

        if out == 'b':
            self.textField.append("Winner is: "+out)
        elif out == 'r':
            self.textField.append("Winner is: " + out)
        else:
            pass

    # TODO (EK): Error Handling einbauen

    # TODO (EK): bei Checkbox-Klick Strategie aendern
    def check(self, checked):
        if checked:
            self.strategy = Online.OnlineService()
            print('ONLINE')
        else:
            self.strategy = Offline.OfflineService()
            print('OFFLINE')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
