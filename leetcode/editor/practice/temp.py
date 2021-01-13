class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)


def josephus(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        # print("开始数数人：", simqueue)
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        outer = simqueue.dequeue()
        print("出局人：", outer)

    return simqueue.dequeue()


if __name__ == '__main__':
    print("胜利者：", josephus(["Bill", "David", "Kent", "Jane", "Susan", "Brad"], 3))
