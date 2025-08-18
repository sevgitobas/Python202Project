# Konsol Tabanlı Kütüphane Uygulaması

Bu proje, Python ile geliştirilen ve JSON tabanlı veri saklama kullanan basit bir konsol kütüphane yönetim sistemi sunar.  
Kitap ekleme, silme, listeleme ve arama işlemlerini Nesne Yönelimli Programlama (OOP) prensipleriyle gerçekleştirir.

---

## Özellikler

- Kitap ekleme, silme, listeleme ve ISBN ile arama  
- Verilerin `library.json` dosyasında saklanması  
- Modüler mimari: `book.py`, `library.py`, `main.py`  

---

## Dosya Yapısı

- `book.py`         : Kitap nesnesini tanımlar  
- `library.py`      : Kütüphane işlemlerini yönetir  
- `main.py`         : Konsol uygulama döngüsünü içerir  
- `library.json`    : Kitap verilerinin saklandığı dosya  
- `README.md`       : Proje açıklamaları  

---

## Kurulum ve Kullanım

1. Depoyu klonlayın ya da indirin:  
   ```bash
   git clone https://github.com/sevgitobas/Python202Project
   cd Python202Project


2. Gerekli kütüphaneleri yükleyin:
	pip install -r requirements.txt


3. Uygulamayı başlatın:
	py main.py

4. Konsol üzerinden kitap ekleyebilir, silebilir, listeleyebilir ve arama yapabilirsiniz.
	- Kitap ekleme (ISBN, başlık, yazar, yıl bilgisi girerek)
	- Kitap silme (ISBN ile)
	- Tüm kitapları listeleme
	- Belirli bir kitabı ISBN ile arama

