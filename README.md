# Konsol Tabanlı Kütüphane Uygulaması

Bu proje, Python ile geliştirilen ve JSON tabanlı veri saklama kullanan basit bir konsol kütüphane yönetim sistemi sunar.  
Kitap ekleme, silme, listeleme ve arama işlemlerini Nesne Yönelimli Programlama (OOP) prensipleriyle gerçekleştirir.

---

## Proje Yapısı

Python202Project/ 
├── README.md 
├── requirements.txt 
├── PythonApplication1/ 
│ ├── main.py				 # Konsol uygulama döngüsü
│ ├── src/
│ │ ├── models/
│ │ ├── routers/
│ │ │ ├── api.py             # API yönlendirme işlemleri
│ │ │ ├── book.py            # Kitap sınıfı
│ │ │ ├── library.py         # Kütüphane sınıfı
│ ├── tests/
| ├── data/
│ │ ├── library.json         # Kitap verilerinin saklandığı JSON dosyası

---

## Özellikler

- Kitap ekleme, silme, listeleme ve ISBN ile arama  
- Verilerin `library.json` dosyasında saklanması  
- Modüler mimari: `book.py`, `library.py`, `main.py`  
- JSON tabanlı veri yönetimi
- Konsol üzerinden etkileşimli kullanım

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
   ```bash
	pip install -r requirements.txt


3. Uygulamayı başlatın:
   ```bash
	python PythonApplication1/main.py


4. Konsol üzerinden kitap ekleyebilir, silebilir, listeleyebilir ve arama yapabilirsiniz.
	- Kitap ekleme (ISBN, başlık, yazar, yıl bilgisi girerek)
	- Kitap silme (ISBN ile)
	- Tüm kitapları listeleme
	- Belirli bir kitabı ISBN ile arama

---

## Notlar

	- library.json dosyası otomatik oluşturulmazsa, boş bir JSON dizisi ile manuel ekleyebilirsiniz: []
	- Kodlar PythonApplication1 klasöründe yer almaktadır. Tüm modüller bu klasörde bulunur.
