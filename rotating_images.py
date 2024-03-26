import cv2  # OpenCV kütüphanesi içe aktarılır.
import numpy as np  # NumPy kütüphanesi içe aktarılır.

# Görüntü diske kaydedilmiş bir dosyadan okunur. Burada "../images/Groot.jpg" yolu kullanılır.
image = cv2.imread("../images/Groot.jpg")
# Görüntü, belirtilen boyuta (256x256) yeniden boyutlandırılır.
image = cv2.resize(image, (256, 256))
# Görüntünün şekli (boyutları ve kanal sayısı) alınır.
image_shape = image.shape

# Görüntü, saat yönünde 90 derece döndürülür.
image1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
# Görüntü, saat yönünün tersine 90 derece döndürülür.
image2 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
# Görüntü, 180 derece döndürülür.
image3 = cv2.rotate(image, cv2.ROTATE_180)

# Döndürülmüş görüntüler ekranda gösterilir.
cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("Image 3", image3)

# Üç döndürülmüş görüntü yatay eksende birleştirilir.
image_concat = np.concatenate((image1, image2, image3), axis=1)
# Birleştirilmiş görüntü ekranda gösterilir.
cv2.imshow("Image Concat", image_concat)

# Bir tuşa basılana kadar tüm pencereler açık kalır.
cv2.waitKey(0)
# Tüm OpenCV pencereleri kapatılır.
cv2.destroyAllWindows()
