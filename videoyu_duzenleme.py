import cv2

# Kamera cihazını yakala
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()

    # Eğer bir kare başarıyla okunduysa,
    if ret:
        frame =cv2.resize(frame , None ,fx =1/2,fy=1/2 , interpolation=cv2.INTER_AREA)
        # Okunan kareyi "Frame" isimli bir pencerede göster
        cv2.imshow("Frame", frame)

        # Her 25 ms'de bir klavye girdisini kontrol et
        # Eğer 'q' tuşuna basıldıysa döngüyü kır
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Döngüden çıktıktan sonra kaynakları serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()