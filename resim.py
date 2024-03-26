import cv2

# Görüntünün dosya yolunu bir değişkene ata. Doğru dosya yolu kullanılmalı.
image_path = "../images/Groot.jpg"

# cv2.imread fonksiyonu ile görüntüyü diskten oku ve bir değişkene ata
image = cv2.imread(image_path)

# Eğer image None ise, dosya yolu doğru değil veya dosya okunamıyor demektir.
if image is None:
    print(f"Görüntü {image_path} yolundan yüklenemedi. Lütfen dosya yolunu kontrol edin.")
else:
    # Görüntünün rengini griye çevir ve yeni bir değişkene ata
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Griye çevrilen görüntüyü yeni bir dosya olarak kaydet
    new_image_path = "Groot_gray.jpg"  # Kaydedilecek dosyanın adı
    cv2.imwrite(new_image_path, gray_image)

    # Kaydedilen yeni gri görüntüyü oku
    saved_gray_image = cv2.imread(new_image_path)

    # Kaydedilen gri görüntüyü ekranda göster
    cv2.imshow("Yeni Kaydedilmis Gri Fotograf", saved_gray_image)

    # cv2.waitKey fonksiyonu bir tuşa basılmasını bekler (0, sonsuz bekleme anlamına gelir)
    cv2.waitKey(0)

    # cv2.destroyAllWindows fonksiyonu tüm OpenCV pencerelerini kapatır
    cv2.destroyAllWindows()

