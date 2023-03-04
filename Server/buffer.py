class Buffer():
    def __init__(self, buffer_size=100):
        self.buff_size = buffer_size
        self.buffer = []

    def add(self, data):
        if len(self.buffer) > self.buff_size:
            self.buffer.pop(-1)
        self.buffer.insert(0, data)
        print(self.buffer)

    @property
    def get(self):
        return self.buffer.pop(-1)

    @property
    def is_empty(self):
        return len(self.buffer) == 0


if __name__ == "__main__":
    buf = Buffer(buffer_size=5)
    buf.add(1)
    buf.add(2)
    buf.add(3)
    buf.add(4)
    buf.add(5)
    # print(buf.get)
    buf.add(6)
    buf.add(7)
    # buf.add('hello')
    print(buf.get)
    print(buf.buffer)
    buf.add(1)
    buf.add(2)
    buf.add(3)
    buf.add(4)
    buf.add(5)
    print(buf.buffer)
