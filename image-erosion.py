import cv2  # OpenCV kütüphanesi içe aktarılır.
import numpy as np  # NumPy kütüphanesi içe aktarılır.

# Bir görüntü dosyası okunarak 'image' değişkenine atanır.
image = cv2.imread("../images/resim.jpg")

# 10x10 boyutlarında, tüm değerleri 1 olan bir matris (çekirdek) oluşturulur.
# Bu çekirdek erozyon işleminde kullanılır.
kernel = np.ones((10, 10), np.uint8)

# 'cv2.erode' fonksiyonu ile 'image' üzerinde erozyon işlemi uygulanır.
# 'kernel' erozyon için kullanılan yapılandırıcı elementtir.
# 'iterations=1' parametresi erozyon işleminin kaç kez tekrarlanacağını belirtir. Burada 1 kez uygulanır.
erode_image = cv2.erode(image, kernel, iterations=1)

# Orijinal görüntü ile erozyon uygulanmış görüntü yatay eksen boyunca (axis=1) birleştirilir.
# Bu sayede her iki görüntü yan yana gösterilebilir.
concat_image = np.concatenate((image, erode_image), axis=1)

# Birleştirilmiş görüntü ekranda gösterilir.
cv2.imshow("Final Image", concat_image)

# Bir tuşa basılana kadar beklenir. Bu komut, görüntünün ekranda kalmasını sağlar.
cv2.waitKey(0)

# Program kapatıldığında tüm OpenCV pencereleri kapatılır.
cv2.destroyAllWindows()
