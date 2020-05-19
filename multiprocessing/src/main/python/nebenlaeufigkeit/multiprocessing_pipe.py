from multiprocessing import Process, Pipe

"""
Prozess wird als Methode aufgerufen, nicht über eine Klasse
    def func(conn):
        conn.send("hallo")
        conn.close()

    if __name__ == '__main__':
        child, parent = Pipe()
        p = Process(target=func, args=(child,))
        p.start()
        print(parent.recv())
        p.join()
"""

"""
Klasse die mithilfe von Pipes senden soll
"""
class KlasseSender(Process):
    def __init__(self, pipe):
        Process.__init__(self)  #Von Process erben
        self.pipe = pipe        #Pipe

    def run(self):
        self.pipe.send('HALLO PIPE') #Hier wird in die Pipe gesendet

"""
Klasse die mithilfe von Pipes empfangen soll
"""
class KlasseEmpf(Process):
    def __init__(self, pipe):
        Process.__init__(self)  #Von Process erben
        self.pipe = pipe        #Pipe

    def run(self):
        print(self.pipe.recv()) #Aus der Pipe empfangen und ausgeben


if __name__ == '__main__':
    child, parent = Pipe()      #Pipe-Duplex: 2 Seiten einer Pipe
    receiver = KlasseEmpf(parent)   #Receiver Objekt, als Parameter die eine Seite der Pipe angeben
    receiver.start()                #Receiver Prozess starten
    sender = KlasseSender(child)    #Sender Objekt, als Parameter die andere Seite der Pipe angeben
    sender.start()                  #Sender Prozess starten
    receiver.join()
    sender.join()
