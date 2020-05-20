import cv2
import time
import matplotlib.pyplot as plt
from nist_suite import FullNistTest as fnt

class Capture(object):

    def __init__(self, number):
        self.number = number
        self.cap = cv2.VideoCapture(0)
        self.__coordinate_file_path = f'light_coordinates/coordinates_{number}.txt'

    def make_coordinates(self):
        start_time = time.time()
        print(f"MAKING COORDINATES №{self.number} WAIT FOR 2 MINUTES")
        f = open(self.__coordinate_file_path, "w")
        while (True):
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            thres = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY)[1]
            for x in range(200, 300):
                for y in range(1, 640):
                    if str(thres[x, y]) == "255":
                        f.write(str(x) + ",")
            cv2.imshow('frame', thres)
            if (time.time() - start_time) >= 120:
                print(f"STOP MAKING COORDINATES №{self.number}")
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        f.close()
        return self.__coordinate_file_path


class Hist(object):
    def __init__(self, coordinates_file_path, number):
        self.coordinates_file_path = coordinates_file_path
        self.hist_file_path = None
        self.number = number
        self.coordinates = []

    def make_hist(self):
        self.hist_file_path = f"hists/hist_{self.number}.png"
        with open(self.coordinates_file_path, "r") as f:
            str = f.read()
            str_coordinates = str.split(",")
            str_coordinates = str_coordinates[:-1]
            print(str_coordinates)
        for str_coordinate in str_coordinates:
            self.coordinates.append(int(str_coordinate))
        plt.hist(self.coordinates, 10, facecolor='blue', alpha=0.5)
        plt.savefig(self.hist_file_path, dpi=72)
        plt.cla()
        plt.clf()
        #plt.close()
        return self.hist_file_path


def execute():
    for i in range(1,11):
        cp = Capture(i)
        file_path = cp.make_coordinates()
        hs = Hist(coordinates_file_path=file_path, number=i)
        hs.make_hist()


def make_light_tests():
    for i in range(1, 11):
        binary_data = []
        with open(f"light_coordinates/coordinates_{i}.txt", "r") as f:
            str = f.read()
            str_coordinates = str.split(",")
            str_coordinates = str_coordinates[:-1]
            for str_coordinate in str_coordinates:
                if int(str_coordinate) > 250:
                    binary_data.append('1')
                else:
                    binary_data.append('0')
            str_to_test = "".join(binary_data)
            nt = fnt(i, str_to_test)
            nt.execute()
make_light_tests()