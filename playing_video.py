# OpenCV kütüphanesini içe aktar
import cv2

# Video dosyasının yolu
video_path = "../images/video.mp4"

# VideoCapture objesi oluşturarak videoyu yakala
cap = cv2.VideoCapture(video_path)

# Video başarıyla açıldıysa bu döngüyü çalıştır
while cap.isOpened():
    # Videodan bir kare oku
    ret, frame = cap.read()

    # Eğer bir kare başarıyla okunduysa,
    if ret:
        # Okunan kareyi 'Frame' isimli bir pencerede göster
        cv2.imshow('Frame', frame)

        # Her 25 ms'de bir klavye girdisini kontrol et
        # Eğer 'q' tuşuna basıldıysa döngüyü kır ve video oynatmayı durdur
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        # Eğer bir kare başarıyla okunmadıysa (yani video sonuna gelindi),
        # Döngüyü kır ve video oynatmayı durdur
        break

# Video yakalamayı serbest bırak
cap.release()

# Açık olan tüm OpenCV pencerelerini kapat
cv2.destroyAllWindows()

