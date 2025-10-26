from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ekspresi = ""
    hasil = ""

    if request.method == "POST":
        tombol = request.form["tombol"]
        ekspresi = request.form.get("ekspresi", "")

        # Tombol clear
        if tombol == "AC":
            ekspresi = ""
            hasil = ""
        # hapus 1 karakter terakhir
        elif tombol == "DEL":
            ekspresi = ekspresi[:-1]  
        # Tombol sama dengan
        elif tombol == "=":
            try:
                ekspresi_eval = ekspresi.replace("X", "*").replace(",", ".")
                hasil = str(eval(ekspresi_eval))
                ekspresi = hasil  # tampilkan hasil di layar
            except:
                hasil = "Error"
                ekspresi = ""

        # Tombol operator
        elif tombol in ["+", "-", "X", "/", ","]:
            # Hindari dua operator berurutan
            if ekspresi and ekspresi[-1] in ["+", "-", "X", "/", ","]:
                ekspresi = ekspresi[:-1] + tombol
            elif ekspresi or tombol in ["-"]:  # boleh minus di awal
                ekspresi += tombol

        # Tombol angka
        else:
            ekspresi += tombol

    return render_template("index.html", ekspresi=ekspresi, hasil=hasil)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
