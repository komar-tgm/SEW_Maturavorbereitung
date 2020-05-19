from multiprocessing import Process, Condition


class WriteFile(Process):
    # TODO übergabe von Lock-Objekt und Filename
    def __init__(self, condition, filename):
        Process.__init__(self)
        self.condition = condition
        self.filename = filename

    def run(self):
        # TODO kritischen Bereich mit einem Lock definieren
        with self.condition:
            # TODO File öffnen und Status hineinschreiben
            self.condition.wait()
            with open(self.filename, 'a') as file:
                file.write("PID"+str(self.pid)+" Name: "+self.filename+"\n")
                file.close()
            self.condition.notify()


if __name__ == '__main__':
    process_list = []
    # TODO initialisiere Lock-Objekt
    condition = Condition()
    # TODO 10 Prozesse, die ihren Status in ein File schreiben
    for i in range(10):
        p = WriteFile(condition, "test.txt")
        process_list.append(p)
        p.start()
        with condition:
            condition.notify()

    # TODO abwarten und Tee trinken
    for x in process_list:
        x.join()


