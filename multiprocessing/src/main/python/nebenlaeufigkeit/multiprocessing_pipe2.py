from multiprocessing import Process, Pipe


class Sender(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        self.pipe.send("HALLO COCO")


class Receiver(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        print(self.pipe.recv())


if __name__ == '__main__':
    child, parent = Pipe()
    receiver = Receiver(child)
    receiver.start()
    sender = Sender(parent)
    sender.start()
    receiver.join()
    sender.join()
