import sqlite3 

conn = sqlite3.connect("kullanici_veritabani.db")
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar (
                                id integer PRIMARY KEY,
                                kullaniciadi text,
                                sifre text,
                                yas integer,
                                boy integer,
                                kilo integer,
                                cinsiyet text,
                                aktivite text,
                                hedef text,
                                günlükkalori integer,
                                sumiktarı integer
                                
                                )''')


conn.commit()
conn.close()

print("veritabanı oluşturuldu")