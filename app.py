from flask import Flask, jsonify, request

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


# 3. POST: Menambahkan buku baru (Status: 201 / 400)
@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"message": "Data harus berupa JSON"}), 400

    required_fields = ['title', 'author', 'year', 'stock']

    if not all(field in data for field in required_fields):
        return jsonify({
            "message": "Field title, author, year, dan stock wajib diisi"
        }), 400

    # Validasi tipe data
    if (
        not isinstance(data['title'], str)
        or not data['title'].strip()
        or not isinstance(data['author'], str)
        or not data['author'].strip()
        or type(data['year']) is not int
        or type(data['stock']) is not int
        or data['stock'] < 0
    ):
        return jsonify({
            "message": "Data buku tidak valid"
        }), 400

    # Membuat ID baru berdasarkan ID terbesar
    new_id = max((book['id'] for book in books), default=0) + 1

    new_book = {
        "id": new_id,
        "title": data['title'].strip(),
        "author": data['author'].strip(),
        "year": data['year'],
        "stock": data['stock']
    }

    books.append(new_book)

    return jsonify({
        "message": "Buku berhasil ditambahkan",
        "book": new_book
    }), 201

if __name__ == '__main__':
    app.run(debug=True, port=3000)