import cv2

image = cv2.imread("../images/Groot.jpg")

image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Kesilecek bölgenin başlangıç noktasını (x, y) ve bölgenin genişliğini (w) ve yüksekliğini (h) belirle.
x, y, w, h = 100, 50, 700, 750

# Görüntünün belirtilen bölgesini kes.
# Kesme işlemi için, 'image[y:y+h, x:x+w]' kullanılarak görüntü üzerinde bir dilimleme işlemi yapılır.
cropped_image = image[y:y+h, x:x+w]

cv2.imshow("image", image)  # Orijinal (ölçeklendirilmiş) görüntüyü bir pencerede göster.
cv2.imshow("cropped_image", cropped_image)  # Kesilmiş görüntüyü başka bir pencerede göster.

cv2.waitKey(0)
cv2.destroyAllWindows()  