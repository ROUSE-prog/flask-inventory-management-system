import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"


def fetch_product_by_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    headers = {
        "User-Agent": "FlaskInventoryApp/1.0 (student project)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return {
                "error": "API request failed",
                "status_code": response.status_code
            }

        data = response.json()

        if data.get("status") == 0:
            return {"error": "Product not found"}

        product = data.get("product", {})

        return {
            "name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "ingredients": product.get("ingredients_text", "No ingredients listed")
        }

    except requests.exceptions.RequestException as error:
        return {"error": f"Connection error: {error}"}