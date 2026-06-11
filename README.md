# Flask Inventory Management System



<img width="1576" height="1092" alt="Screenshot 2026-06-11 at 5 14 35 PM" src="https://github.com/user-attachments/assets/332ff2de-95a1-4f11-a3b7-03c922a062d3" />

A Flask + CLI inventory management application with OpenFoodFacts API integration.

## Features

- Flask REST API
- CRUD inventory management
- Barcode product lookup
- CLI interface
- External API integration
- JSON responses

## Technologies

- Python
- Flask
- Requests
- REST APIs
- OpenFoodFacts API

## Run Project

```bash
pip install -r requirements.txt
python app.py
```

## Run CLI

```bash
python cli.py
```

## API Routes

| Method | Route | Description |
|---|---|---|
| GET | /inventory | Get all items |
| GET | /inventory/<id> | Get one item |
| POST | /inventory | Create item |
| PATCH | /inventory/<id> | Update item |
| DELETE | /inventory/<id> | Delete item |
| GET | /inventory/search/<barcode> | Barcode lookup |
