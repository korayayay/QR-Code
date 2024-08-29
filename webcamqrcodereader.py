import cv2
from pyzbar import pyzbar
import webbrowser

def decode_qr_code_from_webcam():
    # Webcam'i başlat
    cap = cv2.VideoCapture(0)

    last_qr_code = None  # Son okunan QR kodunu saklamak için değişken

    while True:
        # Kameradan bir kare oku
        ret, frame = cap.read()

        if not ret:
            break

        # QR kodlarını çözümle
        qr_codes = pyzbar.decode(frame)

        # Bulunan QR kodlarını işle
        for qr_code in qr_codes:
            qr_code_data = qr_code.data.decode("utf-8")

            # Eğer QR kodu daha önce okunmamışsa işle
            if qr_code_data != last_qr_code:
                last_qr_code = qr_code_data  # Son okunan QR kodunu güncelle

                print(f"QR Kod Verisi: {qr_code_data}")

                # Eğer QR kodu bir URL ise, tarayıcıda aç
                if qr_code_data.startswith("http"):
                    webbrowser.open(qr_code_data)

                # QR kodunu işaretlemek için dikdörtgen çiz
                x, y, w, h = qr_code.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, qr_code_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # İşaretlenmiş kareyi göster
        cv2.imshow("QR Kodu Okuyucu", frame)

        # 'q' tuşuna basarak döngüyü kır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera ve pencereleri serbest bırak
    cap.release()
    cv2.destroyAllWindows()

# Kullanım
decode_qr_code_from_webcam()
