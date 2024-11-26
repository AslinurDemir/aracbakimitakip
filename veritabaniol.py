import sqlite3

def veritabani_olustur():
    conn = sqlite3.connect("arac_bakim.db")
    cursor = conn.cursor()

    # Tabloyu oluştur (Zaten varsa atla)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS arac_bakim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            musteri_ad TEXT NOT NULL,
            musteri_tel TEXT NOT NULL,
            arac_plaka TEXT NOT NULL,
            son_bakim_tarihi TEXT NOT NULL
        );
    """)
    print("Tablo oluşturuldu (veya zaten mevcut).")

    # Örnek veriler ekle
    cursor.execute("""
        INSERT INTO arac_bakim (musteri_ad, musteri_tel, arac_plaka, son_bakim_tarihi)
        VALUES 
            ('Al Yilmaz', '05551112233', '34ABC123', '2023-06-10'),
            ('Ay Demir', '05553334455', '06XYZ456', '2022-10-15'),
            ('Meh Ak', '05554445566', '35JKL789', '2024-08-20'),
            ('Seda Yıldız', '5556789012', '34MNO678', '2022-07-15'),
            ('Kaan Arslan', '5557890123', '34PQR901', '2022-01-10'),
            ('Emre Polat', '5558901234', '34STU234', '2021-05-25'),
            ('Hüseyin Demirtaş', '5559012345', '34VWX567', '2022-08-30'),
            ('Funda Aydın', '5550123456', '34YZA890', '2021-12-12'),
            ('Ahmet Yılmaz', '5551234567', '34ABC123', '2023-11-01'),
            ('Mehmet Kaya', '5552345678', '34XYZ456', '2023-12-15'),
            ('Ayşe Demir', '5553456789', '34DEF789', '2023-10-05'),
            ('Zeynep Kılıç', '5554567890', '34GHI012', '2023-09-20'),
            ('Ali Veli', '5555678901', '34JKL345', '2023-11-15');
    """)
    print("Örnek veriler eklendi.")
    
    conn.commit()
    conn.close()

def verileri_goster():
    conn = sqlite3.connect("arac_bakim.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM arac_bakim")
    veriler = cursor.fetchall()

    for veri in veriler:
        print(veri)

    conn.close()

# Veritabanını oluştur ve verileri ekle
if __name__ == "__main__":
    veritabani_olustur()
    
    # Verileri göster
    verileri_goster()
