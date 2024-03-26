import cv2

# Haar cascade dosyasını yüklemek için CascadeClassifier'ı başlat
# Bu dosya, yüz tanıma için gerekli önceden eğitilmiş bir modeldir.
face_cascade = cv2.CascadeClassifier("../python/haarcascade_frontalface_default.xml")

# Bilgisayarın kamerasını başlatmak için VideoCapture nesnesini kullan
cap = cv2.VideoCapture(0)

# Sonsuz bir döngü içinde kamera görüntüsünden frame'leri oku
while True:
    ret, frame = cap.read()

    if ret:
        # Gelen görüntünün boyutunu artırarak daha büyük hale getir
        # fx ve fy parametreleri sırasıyla görüntünün genişlik ve yükseklik katsayılarıdır.
        frame = cv2.resize(frame, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)

        # Görüntüyü gri tona çevir
        # Yüz tanıma işlemleri için genellikle gri tonlamalı görüntüler kullanılır çünkü işlemi hızlandırır.
        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Görüntünün histogramını eşitleyerek kontrastı artır
        image_gray = cv2.equalizeHist(image_gray)

        # Gri tonlamalı görüntü üzerinde yüz tanıma işlemi gerçekleştir
        faces = face_cascade.detectMultiScale(image_gray)

        # Algılanan her yüz için bir döngü başlat
        for (x, y, w, h) in faces:
            # Yüzün merkezini bul
            center = (x + w//2, y + h//2)
            # Algılanan yüzün etrafına bir elips çiz
            # Bu, yüzün bulunduğunu görsel olarak işaretler.
            frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

        # İşlenmiş frame'i göster
        cv2.imshow("Frame", frame)

        # 'q' tuşuna basıldığında döngüden çık ve programı sonlandır
        # cv2.waitKey(10) ile her 10 milisaniyede bir klavye girdisi kontrol edilir.
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Kamera kaynağını serbest bırak
cap.release()
# Tüm OpenCV pencerelerini kapat
cv2.destroyAllWindows()
