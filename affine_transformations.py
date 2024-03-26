import cv2
import numpy as np
# Gerekli kütüphaneleri içe aktar
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle ve boyutunu değiştir
image = cv2.imread("../images/Groot.jpg")  # 'Groot.jpg' adlı görüntüyü yükle
image = cv2.resize(image, (256, 256))  # Görüntüyü 256x256 boyutuna getir
image_shape = image.shape  # Görüntünün boyutlarını al

# Görüntünün satır, sütun ve kanal sayısını değişkenlere ata
rows, cols, channels = image_shape

# Dönüşüm uygulanacak noktaları belirle
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])  # Kaynak noktalar
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])  # Hedef noktalar
# Afin dönüşüm matrisini hesapla
M = cv2.getAffineTransform(pts1, pts2)
# Afin dönüşümü uygula
dst = cv2.warpAffine(image, M, (cols, rows))

# Giriş ve çıkış görüntülerini yan yana göster
plt.subplot(121)  # 1 satır 2 sütundan oluşan bir ızgara içinde 1. subplot
plt.imshow(image)  # Giriş görüntüsünü göster
plt.title("Input")  # Başlık

plt.subplot(122)  # 1 satır 2 sütundan oluşan bir ızgara içinde 2. subplot
plt.imshow(dst)  # Dönüşüm uygulanmış çıkış görüntüsünü göster
plt.title("Output")  # Başlık
plt.show()  # Grafikleri göster

# Pencereleri kapatmak için bir tuşa basılmasını bekler (sadece OpenCV pencereleri için geçerli)
cv2.waitKey()
cv2.destroyAllWindows()  # Tüm OpenCV pencerelerini kapat


