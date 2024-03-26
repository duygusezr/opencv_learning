import cv2  # OpenCV kütüphanesi içe aktarılır.
import numpy as np  # NumPy kütüphanesi içe aktarılır.

# Görüntü, belirtilen yoldan okunur. Burada "../images/Groot.jpg" dosya yolu kullanılmıştır.
image = cv2.imread("../images/Groot.jpg")
# Görüntünün boyutları alınır.
image_shape = image.shape

# Perspektif dönüşümü için kaynak noktaları belirlenir. Bu noktalar görüntüde dönüşüm yapılacak alanı temsil eder.
pts1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])
# Perspektif dönüşümü sonrası hedef noktalar. Kaynak noktaların dönüşüm sonrası nereye denk geleceğini gösterir.
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [400, 640]])

# Kaynak ve hedef noktaları kullanarak perspektif dönüşüm matrisi hesaplanır.
M = cv2.getPerspectiveTransform(pts1, pts2)
# Hesaplanan dönüşüm matrisi ile perspektif dönüşümü uygulanır. Sonuç olarak dönüştürülmüş görüntü elde edilir.
result = cv2.warpPerspective(image, M, (500, 600))

# Orjinal görüntü ekranda gösterilir.
cv2.imshow("Input", image)
# Dönüştürülmüş görüntü ekranda gösterilir.
cv2.imshow("Output", result)

# Bir tuşa basılana kadar tüm pencereler açık kalır.
cv2.waitKey(0)
# Tüm OpenCV pencereleri kapatılır.
cv2.destroyAllWindows()
