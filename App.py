
from Calculator import Calculator


class App:

    def __init__(self, master):

        self.master = master
        Calculator(self.master, 0, 0)