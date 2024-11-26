import sqlite3
import subprocess #https://docs.python.org/3/library/subprocess.html

def veritabanina_baglan():
    conn = sqlite3.connect("arac_bakim.db")  # Veritabanı dosyasının adı
    return conn

def bakimi_guncel_olanlar(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT musteri_ad, musteri_tel, arac_plaka, son_bakim_tarihi
        FROM arac_bakim
        WHERE DATE(son_bakim_tarihi) >= DATE('now', '-1 year');
    """)
    return cursor.fetchall()

def bakimi_gecikmis_olanlar(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT musteri_ad, musteri_tel, arac_plaka, son_bakim_tarihi
        FROM arac_bakim
        WHERE DATE(son_bakim_tarihi) < DATE('now', '-1 year');
    """)
    return cursor.fetchall()

def html_dosyasi_olustur(guncel_bakim, gecikmis_bakim):
    """Verileri HTML dosyasina yaz."""
    with open("bakim_durumlari.html", "w") as f:
        f.write("<html><head><title>Bakim Durumlari</title></head><body>")
        f.write("<h2>Bakimi Güncel Olanlar</h2><table border='1'>")
        f.write("<tr><th>Müşteri Adi</th><th>Müşteri Telefonu</th><th>Plaka</th><th>Son Bakım Tarihi</th></tr>")
        for veri in guncel_bakim:
            f.write(f"<tr><td>{veri[0]}</td><td>{veri[1]}</td><td>{veri[2]}</td><td>{veri[3]}</td></tr>")
        f.write("</table>")

        f.write("<h2>Bakimi Gecikmiş Olanlar</h2><table border='1'>")
        f.write("<tr><th>Müşteri Adı</th><th>Müşteri Telefonu</th><th>Plaka</th><th>Son Bakım Tarihi</th></tr>")
        for veri in gecikmis_bakim:
            f.write(f"<tr><td>{veri[0]}</td><td>{veri[1]}</td><td>{veri[2]}</td><td>{veri[3]}</td></tr>")
        f.write("</table>")
        f.write("</body></html>")

    # HTML dosyasını manuel olarak açmak için subprocess
    subprocess.run(["start", "Microsoft Edge", "bakim_durumlari.html"], shell=True)
    print("HTML dosyasi tarayicida açildi.")

def main():
    conn = veritabanina_baglan()

    guncel_bakim = bakimi_guncel_olanlar(conn)
    
    gecikmis_bakim = bakimi_gecikmis_olanlar(conn)

    html_dosyasi_olustur(guncel_bakim, gecikmis_bakim)
    
    conn.close()

if __name__ == "__main__":
    main()
