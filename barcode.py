import cv2
import keyboard
from pyzbar import pyzbar


list_code = []

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        list_code.append(barcode_text)
        print(barcode_text)

        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame

def main_bar():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    check_list = []
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow("Отсканируйте товары", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        if keyboard.is_pressed("p"):
            camera.release()
            cv2.destroyAllWindows()
            break
    return list(set(list_code))

if __name__ == '__main__':
    main_bar()
