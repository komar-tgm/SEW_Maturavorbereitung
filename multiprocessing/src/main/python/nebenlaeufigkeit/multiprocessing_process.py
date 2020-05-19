from multiprocessing import Process
from time import sleep


def hampt_dampti():
    # Eine Liste an 1000 Prozessen erstellen und starten
    process_list = []
    for i in range(1000):
        p = Process(target=concurrent_output, args=("hallo", i))
        p.start()
        process_list.append(p)

        for p in process_list:
            p.join()
        # Warten bis alle 1000 Prozesse abgearbeitet wurden


def concurrent_output(message, id):
    # Wartet eine Sekunde bis die Message ausgegeben wird
    sleep(1)
    print("Process " + str(id) + ":" + message)


if __name__ == '__main__':
    hampt_dampti()
