from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    nama = request.form.get("nama")
    kelas = request.form.get("kelas")
    return f"<h1>Halo, {nama} dari kelas {kelas}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
