# Import necessary libraries
import cv2
import os
from datetime import datetime

import keyboard

from face_rec import face_comparison


def save_face():
    i = 1
    wait = 0
    video = cv2.VideoCapture(0)

    while True:
        ret, img = video.read()

        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, str(datetime.now()), (20, 40),
                    font, 2, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Сканирование лица', img)
        key = cv2.waitKey(100)
        wait = wait + 100

        if key == ord('q'):
            break
        if wait == 1000:
            filename = 'frame/Frame_' + str(i) + '.jpg'

            cv2.imwrite(filename, img)
            i = i + 1
            wait = 0
        if keyboard.is_pressed("p"):
            break

    video.release()
    cv2.destroyAllWindows()





