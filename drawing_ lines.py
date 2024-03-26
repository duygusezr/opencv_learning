import cv2  # cv2 (OpenCV) kütüphanesini içe aktar. Görüntü işleme işlemleri için gerekli.

image_path = "../images/Groot.jpg"  # Görüntü dosyasının konumunu 'image_path' değişkenine ata.
image = cv2.imread(image_path)  # 'cv2.imread' fonksiyonu ile görüntüyü diskten oku ve 'image' değişkenine ata.

# 'cv2.resize' fonksiyonu ile görüntünün boyutunu yarı yarıya küçült.
# 'fx' ve 'fy' parametreleri sırasıyla genişlik ve yükseklikteki ölçekleme faktörlerini belirtir (her ikisi de 0.5 olarak ayarlanmıştır).
# 'interpolation=cv2.INTER_AREA' parametresi, küçültme işlemi için kullanılacak interpolasyon metodunu belirtir.
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
image_shape = image.shape  # Küçültülen görüntünün boyutlarını 'image_shape' değişkenine ata.

# Görüntünün sol üst köşesi ile sağ alt köşesi arasında bir çizgi çizmek için iki nokta belirle.
# 'point1' ve 'point2', görüntünün sırasıyla %10 ve %90 koordinatlarında bulunan noktaları temsil eder.
point1 = int(image_shape[1]* 0.1), int(image_shape[0]* 0.1)
point2 = int(image_shape[1]* 0.9), int(image_shape[0]* 0.9)

# 'cv2.line' fonksiyonu ile 'point1' ve 'point2' arasında mavi renkli (255, 0, 0) ve 2 piksel kalınlığında bir çizgi çiz.
cv2.line(image, point1, point2, (255, 0, 0), thickness=2)

# 'cv2.imshow' fonksiyonu ile 'image' adı altında görüntüyü bir pencerede göster.
cv2.imshow("image", image)

cv2.waitKey(0)  # Bir tuşa basılana kadar programın beklemesini sağla.
cv2.destroyAllWindows()  # Açık tüm OpenCV pencerelerini kapat.
