# Konsol Tabanlı Kütüphane Uygulaması

Bu proje, Python ile geliştirilen bir kitap yönetim sistemidir. İlk iki aşamada terminal üzerinden kitap ekleme, silme, arama ve listeleme işlemleri yapılırken; üçüncü aşamada FastAPI ile RESTful bir API sunucusu oluşturulmuştur. Veriler JSON dosyasında saklanır, modüler mimari ve test altyapısı ile sürdürülebilirlik hedeflenmiştir.

---

## Kurulum
- Reponun Klonlanması

			```bash
			git clone https://github.com/sevgitobas/Python202Project.git
			cd Python202Project

- Bağımlılıkların Kurulumu
			
			```bash
			pip install -r requirements.txt

---

## Kullanım
- Aşama 1 ve 2 : Terminal uygulaması
		
		'''bash
		python PythonApplication1/main.py

	Konsol üzerinden:
	- Kitap ekleyebilir (ISBN, başlık, yazar, yıl)
	- Kitap silebilir (ISBN ile)
	- Tüm kitapları listeleyebilir
	- Belirli bir kitabı ISBN ile arayabilirsiniz

- Aşama 3 : API Sunucusu

		'''bash
		uvicorn PythonApplication1.src.routers.api:app --reload
	
	API üzerinden:
	- Kitap ekleme (POST /books)
	- Kitap silme (DELETE /books/isbn)
	- Tüm kitapları listeleme (GET /books)
	- Belirli bir kitabı ISBN ile arama (GET /books/isbn)

	Sunucu çalıştıktan sonra tarayıcıdan şu adresten ulaşabilirsiniz: `http://http://127.0.0.1:8000/docs

- API Dokümantasyonu
	- POST/books : Yeni kitap ekler.
		
		'''json
		{
			"isbn": "1234567890",
			"title": "Kitap Başlığı",
			"author": "Yazar Adı",
			"year": 2023
		}
		'''
	
	- GET/books : Tüm kitapları listeler.
	- GET/books/isbn: Belirtilen ISBN’ye sahip kitabı getirir.
	- POST/books/isbn: Var olan kitabı günceller.
		
		'''json
		{
			"title": "Yeni Kitap Başlığı",
			"author": "Yeni Yazar Adı",
			"year": 2024
		}
		'''
	
	- DELETE/books/isbn: Belirtilen ISBN’ye sahip kitabı siler.


- Test Altyapısı

	Proje, `tests` klasörü altında yer alan test dosyaları ile birim testler içerir. Pytest ile testler yazılmıştır. `conftest.py` ile ortak fixture yönetimi sağlanmıştır. Testleri çalıştırmak için:
			
			```bash
			python -m unittest discover -s tests -p "*.py"


---

## Proje Yapısı
	
	Python202Project/ 
	├── README.md 
	├── requirements.txt 
	├── PythonApplication1/ 
	│ ├── main.py		     # Konsol uygulama döngüsü
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
