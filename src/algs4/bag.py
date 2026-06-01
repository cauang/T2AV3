class Bag(list):
    """
    Uma coleção não ordenada que permite duplicatas.
    Herda diretamente de 'list' para obter performance nativa em C no interpretador Python.
    """
    def add(self, item):
        self.append(item)

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0
