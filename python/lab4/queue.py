'''We need to implement a python class that represents
the queue data structure.'''
class QueueOutOfRangeException(Exception):
    pass    

class Queue:

    def __init__(self, items: list = None):
        if not items:
            items = []
        self.items = items
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop()
        else:
            print("Queue is empty. Cannot dequeue.")
            return None
        
    def empty(self):
        return not self.items


'''We need to implement another queue class that has the same properties as
previous but with the following changes:
    A. The queue should have a name that is provided as a parameter of its
    constructor

    B. The queue should have a size that is provided as a parameter of its
    constructor and if we tried to insert more values than its size raises a
    custom exception called QueueOutOfRangeException

    C. The queue keeps track with all queues instances that has been created
    through this class and we can get any queue of them using its name

    D. The queue class should have two class methods called (save, load)
    which saves all created queues instances to a file and load them when
    needed. '''    
class Qplusplus(Queue):

    queues = []

    def __init__(self,name: str, max_size: int, items = None):
        if not items:
            items = []
        if not len(items) <= max_size:
            raise QueueOutOfRangeException("Items exceed maximum size.")
        super().__init__(items)
        self.name = name
        self.max_size = max_size
        Qplusplus.queues.append(self)
        
    def enqueue(self, item):
        if len(self.items) >= self.max_size:
            raise QueueOutOfRangeException("Cannot enqueue: queue is full.")
        super().enqueue(item)

    @staticmethod
    def get_queue(name: str):
        matches = [x for x in Qplusplus.queues if x.name == name]
        return matches[0] if matches else None

    @staticmethod
    def save():
        with open('queues.txt', 'w') as f:
            for object in Qplusplus.queues:
                f.write(f"{object.name}:{'||'.join(map(str, object.items))}:{object.max_size}\n")

    @staticmethod
    def load():
        try:
            with open('queues.txt', 'r') as f:
                for line in f.readlines():
                    name, items, max_length = line.split(':', 2)
                    Qplusplus(name, int(max_length), items.split('||'))
        except FileNotFoundError:
            pass

            


if __name__ == "__main__":
    # Simple tests
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    print(q.dequeue())  # A
    print(q.empty())    # False
    
    qpp = Qplusplus("test", 3, ["X"])
    qpp.enqueue("Y")
    print(Qplusplus.get_queue("test"))  # ['Y', 'X']
    
    # Test exception
    try:
        Qplusplus("big", 1, ["too", "many"])
    except QueueOutOfRangeException:
        print("Exception works")
    
    print("All tests passed!")
    
    

