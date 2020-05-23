from viergewinntSpiel.Model import Abstract


class OfflineService(Abstract.AbstractClass):
    def send(self, fields, col):
        print('OFFLINE')
        return 'SKIA' * 4
