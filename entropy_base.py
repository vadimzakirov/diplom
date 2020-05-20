import pyfirmata
import time
import numpy as np


class Entropy(object):
    def __init__(self):
        self.end_array = []
        self.board = pyfirmata.Arduino('/dev/ttyUSB0')
        self.state = False
        self.list = []
        self.coordinates = []
    def start(self):
        counter = 0
        while True:
            for elem in self.list:
                if counter % 20 == 0:
                    pass
                if elem > 0:
                    self.send_1()
                else:
                    self.send_0()
                counter += 1

    def count(self):
        counter_1 = 0
        counter_0 = 0
        for elem in self.list:
            if elem == 1:
                self.end_array.append(1)
                counter_1 += 1
            if elem == 0:
                self.end_array.append(0)
                counter_0 += 1
        one_percent = int((counter_1 / len(self.end_array))*100)
        null_percent = int((counter_0 / len(self.end_array)) * 100)
        print(f"Процент единичек - {one_percent} \n Процент нулей - {null_percent}")


    def send_test(self):
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_0()
        self.send_1()
        self.send_0()
        self.send_0()
        self.send_0()

    def send_1(self):
        if self.state:
            time.sleep(0.05)
        if not self.state:
            self.__set_1(3)
            time.sleep(0.05)

    def send_0(self):
        if self.state:
            self.__set_0(3)
            time.sleep(0.05)
        if not self.state:
            time.sleep(0.05)


    def __set_1(self, pin):
        self.board.digital[pin].write(1)
        self.state = True


    def __set_0(self, pin):
        self.board.digital[pin].write(0)
        self.state = False

    def make_binary_file(self):
        str_array = [str(elem) for elem in self.end_array]
        binary_str = "".join(str_array)
        with open ("entropy_inputs/light_binary.txt", "w") as f:
            f.write(binary_str)




