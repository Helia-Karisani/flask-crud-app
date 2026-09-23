## Flask CRUD App – Financial Transaction Manager

A simple web application built with **Flask** that performs basic **CRUD operations** (Create, Read, Update, Delete) on a list of financial transactions.

I built it as a hands-on lab to practice routing, request handling, and HTML rendering with Flask.

---

### Features

* **Create** new transactions with date and amount
* **Read** and view all transactions in a table
* **Update** any existing transaction
* **Delete** transactions (using POST)
* Frontend styled with Bootstrap
* No database: data is stored in memory (list of dictionaries)

---

### Pages

* `/` – View all transactions
* `/add` – Add a new transaction
* `/edit/<id>` – Edit an existing transaction
* `/delete/<id>` – Delete a transaction (via POST)

---

### Getting Started

#### 1. Clone the repo

```bash
git clone https://github.com/Helia-Karisani/flask-crud-app.git
cd flask-crud-app
```

#### 2. Install Flask

```bash
pip install Flask
```

#### 3. Run the app

```bash
python app.py
```

Then visit `http://127.0.0.1:5000` in your browser.

---

### Folder Structure

```
├── app.py
├── templates/
│   ├── transactions.html
│   ├── form.html
│   ├── edit.html
│   └── search.html
```

---

### Notes

* Data is not saved between runs.
* Deletion uses `POST` instead of `GET`.
