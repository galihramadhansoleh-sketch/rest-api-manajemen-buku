from flask import Flask, jsonify

app = Flask(__name__)

# Simulasi Database Menggunakan Array Lokal
books = [
    {"id": 1, "title": "Laskar Pelangi", "author": "Andrea Hirata", "year": 2005, "stock": 4},
    {"id": 2, "title": "Bumi Manusia", "author": "Pramoedya Ananta Toer", "year": 1980, "stock": 3}
]

# 1. GET: Mendapatkan daftar semua buku (Status: 200)
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# 2. GET: Mendapatkan detail buku berdasarkan ID (Status: 200 / 404)
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return jsonify({"message": "Buku tidak ditemukan"}), 404
    return jsonify(book), 200

if __name__ == '__main__':
    app.run(debug=True, port=3000)