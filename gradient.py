import cv2  # OpenCV kütüphanesi içe aktarılır.
import numpy as np  # NumPy kütüphanesi içe aktarılır.

# Görüntü dosyası okunur ve 512x512 piksel boyutunda yeniden boyutlandırılır.
image1 = cv2.imread("../images/vazo.jpg")
image1 = cv2.resize(image1, (512, 512))

# Görüntü, BGR (Mavi-Yeşil-Kırmızı) renk uzayından HSV (Renk-Doygunluk-Değer) renk uzayına dönüştürülür.
hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)

# Belirli bir renk aralığını tanımlayan değerler belirlenir.
# Bu örnekte, mavi renk aralığı için değerler verilmiştir. Ancak, HSV renk uzayında uygun mavi aralığı için düzeltme yapılmalıdır.
blue1 = np.array([100, 0, 0])
blue2 = np.array([255, 255, 255])

# Belirlenen renk aralığında bulunan nesneler için bir maske oluşturulur.
mask = cv2.inRange(hsv, blue1, blue2)

# Maske kullanılarak, orijinal görüntü üzerinden sadece belirli renk aralığındaki nesnelerin bulunduğu bir görüntü elde edilir.
res = cv2.bitwise_and(image1, image1, mask=mask)

# Morfolojik işlemler için bir çekirdek (kernel) tanımlanır.
kernel = np.ones((5, 5), np.uint8)

# Elde edilen görüntü üzerinde morfolojik gradyan işlemi uygulanır.
# Bu işlem, nesnelerin kenarlarını vurgulayarak daha belirgin hale getirir.
gradient = cv2.morphologyEx(res, cv2.MORPH_GRADIENT, kernel)

# Orijinal görüntü ve işlem sonucu elde edilen görüntü ekranda gösterilir.
cv2.imshow("Original", image1)
cv2.imshow("Final image", gradient)

# Bir tuşa basılana kadar program bekler. Bu süre zarfında kullanıcı, oluşturulan pencereleri inceleyebilir.
cv2.waitKey(0)
# Tüm OpenCV pencereleri kapatılır ve program sonlandırılır.
cv2.destroyAllWindows()
