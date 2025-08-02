

## 🧾 Flask CRUD App – Financial Transaction Manager

This is a simple web application built with **Flask** that performs basic **CRUD operations** (Create, Read, Update, Delete) on a list of financial transactions.

It was developed as part of a hands-on lab to practice routing, request handling, and HTML rendering using Flask.

---

### ✅ Features

* **Create** new transactions with date and amount
* **Read** and view all transactions in a tabular list
* **Update** any existing transaction
* **Delete** transactions (using POST for safety)
* Clean and styled frontend using Bootstrap
* No database — data is stored in memory (list of dictionaries)

---

### 🗂 Pages

* `/` – View all transactions (Transaction Records)
* `/add` – Add a new transaction
* `/edit/<id>` – Edit an existing transaction
* `/delete/<id>` – Delete a transaction (via POST)

---

### 🚀 Getting Started

#### 1. Clone the repo:

```bash
git clone https://github.com/your-username/flask-crud-app.git
cd flask-crud-app
```

#### 2. Install Flask:

```bash
pip install Flask
```

#### 3. Run the app:

```bash
python app.py
```

Then visit `http://127.0.0.1:5000` in your browser.

---

### 📁 Folder Structure

```
├── app.py
├── templates/
│   ├── transactions.html
│   ├── form.html
│   ├── edit.html
│   └── search.html
```

---

### 📌 Notes

* This is a learning project — it does not persist data between runs.
* Make sure to use `POST` (not `GET`) for deletion to follow proper web practices.
* The original lab was based on an IBM Developer Skills Network exercise.
