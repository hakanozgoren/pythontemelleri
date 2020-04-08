import sqlite3 as sql
db = sql.connect("DB\IK.sqlite")
cur = db.cursor()
sorgu = f"""
SELECT adi,soyadi,email
  FROM personeller
 WHERE departman_id IN (
           SELECT departman_id
             FROM DEPARTMANLAR
            WHERE departman_adi = '{input("Sorgulamak istediğiniz departmanı yazınız: ")}'
       );
"""
cur.execute(sorgu)
for adi,soyadi,email in cur.fetchall():
    print("Adı: {} Soyadı: {} Email: {}".format (adi,soyadi,email))


