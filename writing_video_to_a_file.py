import cv2

# Kamera cihazından video yakalamayı başlat
cap = cv2.VideoCapture(0)

# Çerçeve boyutlarını al
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Video kaydetmek için VideoWriter objesi oluştur
video_cod = cv2.VideoWriter_fourcc(*"XVID")
video_output = cv2.VideoWriter("../images/videomuz.avi", video_cod, 30, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if ret:
        # Çerçeveyi göster
        cv2.imshow("Frame", frame)
        # Video dosyasına çerçeveyi yaz
        video_output.write(frame)

        # 'q' tuşuna basıldığında döngüden çık
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Kaynakları serbest bırak
cap.release()
video_output.release()
cv2.destroyAllWindows()
