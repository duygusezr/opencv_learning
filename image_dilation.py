import cv2  # OpenCV kütüphanesi içe aktarılır.
import numpy as np  # NumPy kütüphanesi içe aktarılır.

# Bir görüntü dosyası okunarak 'image' değişkenine atanır. '../images/resim.jpg' yolu kullanılır.
image = cv2.imread("../images/resim.jpg")

# 10x10 boyutlarında, tüm değerleri 1 olan bir matris (çekirdek) oluşturulur.
# Bu çekirdek genişletme (dilasyon) işleminde kullanılır.
kernel = np.ones((10, 10), np.uint8)

# 'cv2.dilate' fonksiyonu ile 'image' üzerinde genişletme işlemi uygulanır.
# 'kernel' genişletme için kullanılan yapılandırıcı elementtir.
# 'iterations=1' parametresi genişletme işleminin kaç kez tekrarlanacağını belirtir. Burada 1 kez uygulanır.
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Orijinal görüntü ile genişletilmiş görüntü yatay eksen boyunca (axis=1) birleştirilir.
# Bu sayede her iki görüntü yan yana gösterilebilir.
concat_image = np.concatenate((image, dilated_image), axis=1)

# Birleştirilmiş görüntü ekranda gösterilir.
cv2.imshow("Final Image", concat_image)

# Bir tuşa basılana kadar beklenir. Bu komut, görüntünün ekranda kalmasını sağlar.
cv2.waitKey(0)

# Program kapatıldığında tüm OpenCV pencereleri kapatılır.
cv2.destroyAllWindows()
