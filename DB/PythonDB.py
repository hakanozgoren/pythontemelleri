import sqlite3 as sql
<<<<<<< HEAD
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
=======
class DB():
    def __init__(self,adres="DB\IK.sqlite"):
        self.db = sql.connect(adres)
        self.cur = self.db.cursor()
    def select(self,tabloadi,alanlar="*",where=""):
        sorgu = f"SELECT {alanlar} FROM {tabloadi}"
        if where:
            sorgu += f" WHERE {where}"
        return self.cur.execute(sorgu).fetchall()

class personelListe:
    def __init__(self):
        self.db = DB()
    
    def personelListeDep(self,param):
        print(self.db.select(tabloadi="personeller",alanlar="adi,soyadi,email",where=f""" departman_id IN (
            SELECT departman_id
              FROM DEPARTMANLAR
             WHERE departman_adi = '{param}'
        )"""))

liste = personelListe()
liste.personelListeDep('Finans')

# db = sql.connect("DB\IK.sqlite")
# cur = db.cursor()
# sorgu = f"""
# SELECT adi,soyadi,email
#   FROM personeller
#  WHERE departman_id IN (
#            SELECT departman_id
#              FROM DEPARTMANLAR
#             WHERE departman_adi = '{input("sorgulamak istediğiniz departmanı yazınız:")}'
#        );
# """
# cur.execute(sorgu)
# for adi,soyadi,email in cur.fetchall():
#     print(adi,soyadi,email)

>>>>>>> 2181c180bf6f24bf984d2117e812907b33d810e3


