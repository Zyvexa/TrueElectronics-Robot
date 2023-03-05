class Buffer():  # кольцевой буфер
    def __init__(self, buffer_size=10):
        self.buff_size = buffer_size  # размер буфера
        self.buffer = []  # данные в буфере

    def add(self, data):  # добаление элемента, если места нет, то перезаписываеться самый старый
        if len(self.buffer) > self.buff_size:
            self.buffer.pop(-1)
        self.buffer.insert(0, data)
        # print(self.buffer)

    @property
    def get(self):  # получение самого старого значения из буфера
        if not self.is_empty:
            return self.buffer.pop(-1)
        else:
            return []

    @property
    def is_empty(self):  # поустой ли буфер?
        return len(self.buffer) == 0


