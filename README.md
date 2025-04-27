# Prediksi Tipe Kustomer API

## Fitur
```
- Memprediksi tipe kustomer untuk kebutuhan analisis lebih lanjut.
- Hasil prediksi: '0 untuk Customer dengan tipe Normal', '1 untuk Customer dengan tipe Member'

```

### 1. Clone Repository
Clone Repository menggunakan terminal Visual Studio Code
```cmd
git clone https://github.com/ivaryu/prediksi_tipe_kustomer.git
```

### 2. Buat Virtual Environment pada Folder

```cmd
python -m venv .env
.env\Scripts\activate
```

### 3. Install Library

```cmd
pip install -r requirements.txt
```

### 4. Jalankan API

```cmd
uvicorn main:app --reload
```

### 5. Akses Swagger UI

Buka browser:  
 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## ✏ Contoh JSON Input

```json
{
  "City": 1,
  "Gender": 1,
  "Product_line": 3,
  "Unit_price": 69.3,
  "Total": 554.4,
  "Payment": 2,
  "cogs": 510,
  "Jam": 15
}
```

## ✅ Contoh Output

```json
{
  "prediction": 1
}
