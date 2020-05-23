from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def send(self, fields, col):
        pass

    def check(self, fields):
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
        print('CHECKWIN:' + win)
        return win

