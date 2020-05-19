from multiprocessing import Process, Queue

"""
def func(queue):
    queue.put("Hallo")
    queue.put(9)


if __name__ == '__main__':
    q = Queue()
    p = Process(target=func, args=(q,))
    p.start()
    print(q.get())
    p.join()
"""

"""
Klasse die eine Queue erzeugt und Daten einfügt
"""


class QueueErz(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.queue = queue

    def run(self):
        self.queue.put("HALLO QUEUE")  # In die Queue einfügen
        self.queue.put("2TE QUEUE")


"""
Klasse die aus der Queue empfängt
"""


class QueueEmpf(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():  # Wenn die Queue nicht leer ist
            print(self.queue.get())  # dann soll ausgelesen werden


if __name__ == '__main__':
    queue = Queue()  # Queue erzeugen
    erzeuger = QueueErz(queue)
    erzeuger.start()  # Erzeuger Prozess starten
    empf = QueueEmpf(queue)
    empf.start()  # Empfänger Prozess starten
    erzeuger.join()
    empf.join()
