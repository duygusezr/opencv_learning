import cv2  # cv2 kütüphanesini içe aktar

image_path = "../images/Groot.jpg"  # Görüntü dosyasının yolu
image = cv2.imread(image_path)  # Görüntüyü oku

# Görüntüyü yarı yarıya küçült
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

text = "YOUTUBE"  # Görüntüye eklenecek metin
position = (30, 50)  # Metnin görüntüdeki konumu
color = (0, 0, 255)  # Metnin rengi (BGR formatında)
font_size = 1  # Metnin font büyüklüğü
thickness = 2  # Metnin kalınlığı
font = cv2.FONT_HERSHEY_SIMPLEX  # Metnin fontu

# Görüntüye metin ekle
cv2.putText(image, text, position, font, font_size, color, thickness)

cv2.imshow("image", image)  # Görüntüyü ekranda göster

cv2.waitKey(0)  # Bir tuşa basılmasını bekle
cv2.destroyAllWindows()  # Tüm pencereleri kapat
