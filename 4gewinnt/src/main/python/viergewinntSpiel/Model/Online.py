from viergewinntSpiel.Model import Abstract
import requests


class OnlineService(Abstract.AbstractClass):

    def send(self, fields, col):
        print('Selected col:'+str(col))
        newField = self.insert(fields, col)

        print('Fields '+newField)

        param = {"fields": newField}
        resp = requests.get('http://localhost:8080/viergewinnt', params=param)

        if resp.status_code != 200:
            raise ValueError(self.output.format(resp.status_code))

        output = resp.text
        print('OUTPUT: '+output)
        print(len(output))
        return output

    def insert(self, fields, col):
        liste = list(fields)

        if liste[col+12] == ' ':
            liste[col+12] = 'b'
        elif liste[col+8] == ' ':
            liste[col + 8] = 'b'
        elif liste[col + 4] == ' ':
            liste[col + 4] = 'b'
        elif liste[col] == ' ':
            liste[col] = 'b'
        else:
            pass

        return "".join(liste)

