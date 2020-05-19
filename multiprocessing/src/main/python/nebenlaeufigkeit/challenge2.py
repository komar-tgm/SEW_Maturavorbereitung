from multiprocessing import Process, Event, Value


class Calculator(Process):
    def __init__(self, event, value):
        Process.__init__(self)
        self.event = event
        self.value = value

    def run(self):
        self.event.wait()
        summe = 0

        for i in range(self.value.value + 1):
            summe += i

        self.value.value = summe


if __name__ == '__main__':
    event = Event()
    value = Value("i", 0)
    calculator = Calculator(event, value)
    calculator.start()
    input = int(input("Eingabe"))

    event.set()
    value.value = input
    calculator.join()
    print(str(value.value))
