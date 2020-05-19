from multiprocessing import Process, Lock


def writer(lock):
    with lock:
        with open("writer.txt", "a") as file:
            for i in range(3):
                file.write("Hallo David\n")


if __name__ == '__main__':
    lock = Lock()
    process_list = []
    for i in range(12):
        p = Process(target=writer, args=(lock,))
        process_list.append(p)
        p.start()

    for p in process_list:
        p.join()
