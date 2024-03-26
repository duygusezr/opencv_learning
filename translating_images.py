import cv2  # OpenCV kütüphanesi içe aktarılır.
import numpy as np  # NumPy kütüphanesi içe aktarılır.

# Görüntü, belirtilen dosya yolu kullanılarak okunur. Burada "../images/Groot.jpg" dosya yolu kullanılmıştır.
image = cv2.imread("../images/Groot.jpg")
# Görüntü, orijinal boyutunun yarısı kadar küçültülür. İnterpolasyon yöntemi olarak INTER_AREA kullanılır.
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# Görüntünün yeni boyutları alınır.
image_shape = image.shape

# Çeviri dönüşüm matrisi T oluşturulur. Görüntünün genişliğinin 1/3'ü kadar sağa ve yüksekliğinin 1/3'ü kadar aşağı taşınır.
T = np.float32([[1, 0, image.shape[1] / 3], [0, 1, image.shape[0] / 3]])
# Oluşturulan çeviri matrisi, warpAffine fonksiyonu ile görüntüye uygulanır.
image = cv2.warpAffine(image, T, (image_shape[1], image_shape[0]))  # Dikkat: Buradaki boyutların yer değiştirmesi gerekir.

# İşlenmiş görüntü ekranda gösterilir.
cv2.imshow("Reading image", image)

# Bir tuşa basılana kadar tüm pencereler açık kalır.
cv2.waitKey(0)
# Tüm OpenCV pencereleri kapatılır.
cv2.destroyAllWindows()
