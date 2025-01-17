from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventaris.db'
db = SQLAlchemy(app)

class Produk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), unique=True, nullable=False)
    harga = db.Column(db.Float, nullable=False)
    stok = db.Column(db.Integer, nullable=False)

class Pemasok(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kontak = db.Column(db.String(100), nullable=False)

@app.route('/produk')
def daftar_produk():
    produk = Produk.query.all()
    return render_template('daftar_produk.html', produk=produk)

@app.route('/produk/tambah', methods=['GET', 'POST'])
def tambah_produk():
    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        stok = request.form['stok']
        produk_baru = Produk(nama=nama, harga=harga, stok=stok)
        db.session.add(produk_baru)
        db.session.commit()
        return redirect(url_for('daftar_produk'))
    return render_template('tambah_produk.html')

@app.route('/laporan')
def laporan_stok():
    produk_habis = Produk.query.filter(Produk.stok < 10).all()
    return render_template('laporan_stok.html', produk=produk_habis)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)