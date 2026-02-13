# pylint: disable=invalid-name
"""
Este módulo calcula el costo total de ventas basado en un catálogo de precios
y un registro de ventas proporcionados en formato JSON.
"""
import json
import sys
import time


def load_json_file(filename):
    """Carga un archivo JSON y maneja errores de lectura/formato."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{filename}' no tiene formato JSON válido.")
        return None
    except Exception as err:  # pylint: disable=broad-except
        print(f"Error inesperado leyendo '{filename}': {err}")
        return None


def create_price_catalogue(catalogue_data):
    """Convierte la lista de precios a un diccionario para búsqueda rápida."""
    price_map = {}
    for item in catalogue_data:
        title = item.get("title")
        price = item.get("price")
        if title and isinstance(price, (int, float)):
            price_map[title] = price
    return price_map


def compute_total_sales(price_map, sales_data):
    """Calcula el total acumulado de las ventas."""
    total_cost = 0.0

    for sale in sales_data:
        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if not product or not isinstance(quantity, (int, float)):
            print(f"Error: Datos de venta inválidos: {sale}")
            continue

        if product in price_map:
            total_cost += price_map[product] * quantity
        else:
            print(f"Advertencia: El producto '{product}' no existe.")

    return total_cost


def main():
    """Función principal."""
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py priceCatalogue.json "
              "salesRecord.json")
        sys.exit(1)

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    start_time = time.time()

    catalogue_data = load_json_file(price_file)
    sales_data = load_json_file(sales_file)

    if catalogue_data is None or sales_data is None:
        sys.exit(1)

    price_map = create_price_catalogue(catalogue_data)
    total_cost = compute_total_sales(price_map, sales_data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    output_lines = [
        "TOTAL DE VENTAS",
        "-" * 20,
        f"Costo Total: ${total_cost:,.2f}",
        f"Tiempo de ejecución: {elapsed_time:.4f} segundos"
    ]

    for line in output_lines:
        print(line)

    with open("SalesResults.txt", "w", encoding='utf-8') as results_file:
        for line in output_lines:
            results_file.write(line + "\n")


if __name__ == "__main__":
    main()
