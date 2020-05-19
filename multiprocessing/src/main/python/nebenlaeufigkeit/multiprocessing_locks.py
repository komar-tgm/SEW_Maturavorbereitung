from multiprocessing import Process, Lock


class WriteFile(Process):
    # TODO übergabe von Lock-Objekt und Filename
    def __init__(self, lock, filename):
        Process.__init__(self)
        self.lock = lock
        self.filename = filename

    def run(self):
        # TODO kritischen Bereich mit einem Lock definieren
        with self.lock:
            # TODO File öffnen und Status hineinschreiben
            with open(self.filename, 'a') as file:
                file.write("PID"+str(self.pid)+" Name: "+self.filename+"\n")
                file.close()


if __name__ == '__main__':
    process_list = []
    # TODO initialisiere Lock-Objekt
    lock = Lock()
    # TODO 10 Prozesse, die ihren Status in ein File schreiben
    for i in range(10):
        p = WriteFile(lock, "test.txt")
        process_list.append(p)
        p.start()

    # TODO abwarten und Tee trinken
    for x in process_list:
        x.join()
