import cv2
import pyzbar.pyzbar as pyzbar

def qr():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        decode_QR = pyzbar.decode(frame)
        for qrcode in decode_QR:
            (x, y, w, h) = qrcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 0, 255), 2)
            if len(qrcode.data) > 1:
                cap.release()
                cv2.destroyAllWindows()
                return qrcode.data
                break
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()