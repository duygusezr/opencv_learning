import cv2  # cv2 kütüphanesini içe aktar

image_path = "../images/Groot.jpg"  # Görüntü dosyasının yolu
image = cv2.imread(image_path)  # Görüntüyü oku

# Görüntüyü yarı yarıya küçült
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
image_shape = image.shape
# Merkez noktasını ve yarıçapı belirle
center_point = (int(image_shape[1] * 0.5), int(image_shape[0] * 0.5))  # x (genişlik) ve y (yükseklik) yer değiştirdi
radius = 100
cv2.circle(image, center_point, radius, (0, 255, 0), thickness=1)  # Daireyi çiz

cv2.imshow("image", image)  # Görüntüyü göster

cv2.waitKey(0)  # Bir tuşa basılmasını bekle
cv2.destroyAllWindows()  # Tüm pencereleri kapat
