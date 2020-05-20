import cv2
import time
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
my_file = open("coordinates.txt", "w")
counter = 0
dot_counter = 0
start_time = time.time()
x_coordinates = []
f1 = open("entropy_inputs/coordinates_not_ideal.txt", 'w')
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thres = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY)[1]
    color = (255, 255, 255)
    for x in range(200, 300):
        for y in range(1, 640):
            if str(thres[x, y]) == "255":
                dot_counter += 1
                x_coordinates.append(x)
                f1.write(str(x) + ",")
    counter += 1
    cv2.imshow('frame', thres)
    if (time.time() - start_time) >= 120:
        print(f"Количество точек -- {dot_counter}")
        print(f"Координаты точек -- {x_coordinates}")
        num_bins = 30
        DPI = 72
        f1.close()
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
