import cv2  # OpenCV kütüphanesi içe aktarılır.

# 'paper.jpg' adlı görüntü dosyası okunur ve 'image' değişkenine atanır.
image = cv2.imread("../images/paper.jpg")
# Görüntü 512x512 boyutlarına yeniden boyutlandırılır.
image = cv2.resize(image, (512, 512))

# Görüntü gri tonlamaya çevrilir.
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Gri tonlamalı görüntüye Gauss bulanıklığı uygulanır. Bu, kenar algılama öncesi gürültüyü azaltır.
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

# Sobel operatörü kullanılarak x yönünde kenarlar tespit edilir.
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
# Sobel operatörü kullanılarak y yönünde kenarlar tespit edilir.
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
# Sobel operatörü kullanılarak hem x hem y yönlerinde kenarlar tespit edilir.
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

# Canny kenar algılama algoritması kullanılarak kenarlar tespit edilir.
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

# Canny kenar algılama sonucu olan görüntü gösterilir.
cv2.imshow("canny edge image", edges)
# Orjinal görüntü gösterilir.
cv2.imshow("image", image)
# Gri tonlamalı görüntü gösterilir.
cv2.imshow("Final Image", img_gray)

# Bir tuşa basılana kadar beklenir.
cv2.waitKey(0)
# Tüm OpenCV pencereleri kapatılır.
cv2.destroyAllWindows()
