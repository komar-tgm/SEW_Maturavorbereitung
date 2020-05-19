from multiprocessing import Process, Event, Value

"""
Eine Klasse die von 1 bis zu einer bestimmten Zahl alle Zahlen aufaddiert
"""


class Calculator(Process):
    def __init__(self, value, event):
        Process.__init__(self)
        self.value = value
        self.event = event

    def run(self):
        self.event.wait()  # Auf ein Event warten
        summe = 0
        for i in range(self.value.value + 1):
            summe += i  # Additionsvorgang

        self.value.value = summe


if __name__ == '__main__':
    event = Event()  # Neues Event
    value = Value('i', 0)  # Value ist ein shared Objekt
    calculator = Calculator(value, event)
    calculator.start()  # Starten des Prozesses
    n = int(input("Input: "))  # Zahl wird eingegeben
    value.value = n
    event.set()  # Signal wird gegeben, wenn die Eingabe erfolgt
    calculator.join()
    print("ERGEBNIS: " + str(value.value))  # Ausgabe
