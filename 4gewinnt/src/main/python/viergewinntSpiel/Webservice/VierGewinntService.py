import random
import web

# TODO: Library einbinden, um Webservice zu starten

# TODO: Web Application mit URL erstellen
urls = ('/viergewinnt', 'VierGewinnt')
app = web.application(urls, globals())


# Beispiel-Aufruf mit 1 besetztem Feld:
# http://127.0.0.1:8080/viergewinnt?fields=%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20b

class VierGewinnt:
    # TODO: auf GET reagieren und GET-Parameter "fields" auslesen
    # TODO (EK): "fields" auf Gültigkeit pruefen
    # TODO: next_move mit "fields" aufrufen und Ergebnis als Text zurückliefern
    pass

    def GET(self):
        fields1 = web.input().fields
        print("WEBSERVICE: "+fields1)
        return next_move(fields1)


def next_move(field: str):
    """
    Versucht, mit einem Zug eine Gewinnbedingung zu erreichen
    :param field: Das aktuelle 4x4-Spielfeld
    :return: Das neue 4x4-Spielfeld (inkl. gesetztem Feld)
    """
    i = 0
    # Alle vier Spalten durchgehen
    for i in range(4):
        j = -1
        # Bis zum letzten freien Feld dieser Spalte navigieren
        while (j + 1) * 4 + i < 16 and field[(j + 1) * 4 + i] == ' ':
            j += 1
        # Es ist noch etwas frei
        if j >= 0:
            # Stein in diesem Feld einsetzen und probieren, ob gewonnen wird
            index = (j) * 4 + i
            trywin = field[:index] + 'r' + field[index + 1:]
            if checkwin(trywin) == 'r':
                return trywin

    # Es kann nicht mit 1 Zug gewonnen werden: Zufaellige freie Spalte waehlen
    if field[:15].count(' ') > 0:
        j = -1
        num = -1
        while j < 0:
            num = random.randint(0, 4)
            while (j + 1) * 4 + num < 16 and field[(j + 1) * 4 + num] == ' ':
                j += 1
        index = (j) * 4 + num
        fields = field[:index] + 'r' + field[index + 1:]
    return fields


def checkwin(fields):
    """
    Prueft, ob im uebergebenen Spielfeld jemand gewonnen hat (r oder b).
    :param fields: das zu ueberpruefende Spielfeld
    :return: der Gewinner (r, b oder ' ')
    """
    win = ' '
    # Alle Gewinnbedingungen pruefen
    if fields[0] == fields[1] == fields[2] == fields[3]:
        win = fields[0]
    elif fields[4] == fields[5] == fields[6] == fields[7]:
        win = fields[4]
    elif fields[8] == fields[9] == fields[10] == fields[11]:
        win = fields[8]
    elif fields[12] == fields[13] == fields[14] == fields[15]:
        win = fields[12]
    elif fields[0] == fields[4] == fields[8] == fields[12]:
        win = fields[0]
    elif fields[1] == fields[5] == fields[9] == fields[13]:
        win = fields[1]
    elif fields[2] == fields[6] == fields[10] == fields[14]:
        win = fields[2]
    elif fields[3] == fields[7] == fields[11] == fields[15]:
        win = fields[3]
    elif fields[0] == fields[5] == fields[10] == fields[15]:
        win = fields[0]
    elif fields[3] == fields[6] == fields[9] == fields[12]:
        win = fields[3]
    return win


if __name__ == "__main__":
    # TODO: Webservice starten
    app.run()
