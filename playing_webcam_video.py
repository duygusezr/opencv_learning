# OpenCV kütüphanesini içe aktar
import cv2

# Video kaynağını belirle (0 varsayılan kamera cihazını temsil eder)
video_path = 0

# VideoCapture objesi ile kamera cihazından video yakala
cap = cv2.VideoCapture(video_path)

# Kamera başarıyla aktive edildiyse, bu döngüyü çalıştır
while cap.isOpened():
    # Kameradan bir kare oku
    ret, frame = cap.read()

    # Eğer bir kare başarıyla okunduysa,
    if ret:
        # Okunan kareyi 'Frame' isimli bir pencerede göster
        cv2.imshow('Frame', frame)

        # Her 25 ms'de bir klavye girdisini kontrol et
        # Eğer 'q' tuşuna basıldıysa döngüyü kır ve görüntü akışını durdur
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        # Eğer bir kare başarıyla okunmadıysa (yani kamera bağlantısında bir sorun varsa),
        # Döngüyü kır ve görüntü akışını durdur
        break

# Video yakalamayı serbest bırak
cap.release()

# Açık olan tüm OpenCV pencerelerini kapat
cv2.destroyAllWindows()
