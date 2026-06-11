# Flask Inventory Management System

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
