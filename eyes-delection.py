import cv2


face_cascade = cv2.CascadeClassifier("../python/haarcascade_eye.xml")

# Kamera başlatılıyor
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        # Frame boyutunu azalt
        frame = cv2.resize(frame, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)

        # Griye çevir ve histogram eşitle
        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.equalizeHist(image_gray)

        # Yüzleri algıla
        faces = face_cascade.detectMultiScale(image_gray)

        for (x, y, w, h) in faces:
            center = (x + w//2, y + h//2)
            frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

        # Frame'i göster
        cv2.imshow("Frame", frame)

        # 'q' tuşuyla çıkış yap
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Kaynakları serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
