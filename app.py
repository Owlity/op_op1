import pymysql
from flask import Flask, render_template, request
import random

 
app = Flask(__name__)

def koble_til_database():
   forbindelse = pymysql.connect(
      host= "10.200.15.16",
      user= "eksternbruker",
      password ="1234!",
      database="oppdrag1_db", 
      charset="utf8mb4", 
      cursorclass=pymysql.cursors.DictCursor,
      connect_timeout=5

    )
   return forbindelse

   
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order", methods=['GET','POST'])
def order():
    itemliste = ["mus", "iphone", "valve", "uno", "3ds"]
    if request.method == "POST":
        produkt = request.form.get("produkt")
        items = request.form.get("items")
        navn = request.form.get("navn")
        email = request.form.get("email")
        pnummer = request.form.get("pnummer")
        
        
        print(produkt)
        print(items)    
        return render_template("resultat.html", items=items, produkt=produkt, navn=navn, pnummer=pnummer, email=email)

    with (
       koble_til_database() as forbindelse,
       forbindelse.cursor() as peker,
    ):
       sql = (
          "SELECT kunde_id, navn, epost, telefon "
          "FROM kunder ORDER BY navn"
       )
       peker.execute(sql)
       kundeliste = peker.fetchall()
    return render_template("orders.html", itemliste=itemliste)


@app.route("/about")    
def about():
    return render_template("about.html")
if __name__ == "__main__":
 app.run(debug=True)




