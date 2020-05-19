from multiprocessing import Process
from time import sleep


def writer():
    print("Hallo Welt")


if __name__ == '__main__':
    process_list = []
    for i in range(20):
        sleep(1)
        p = Process(target=writer, args=())
        process_list.append(p)
        p.start()

    for p in process_list:
        p.join()
