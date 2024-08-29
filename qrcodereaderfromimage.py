import cv2
from pyzbar import pyzbar

def decode_qr_code():
    image = cv2.imread('qrkod.png')

    qr_codes = pyzbar.decode(image)

    for qr_code in qr_codes:
        x, y, w, h = qr_code.rect
        qr_code_data = qr_code.data.decode("utf-8")
        qr_code_type = qr_code.type

        print(f"QR Kod Tipi: {qr_code_type}")
        print(f"QR Kod Verisi: {qr_code_data}")

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("QR Kodu Görüntüsü", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

decode_qr_code()
