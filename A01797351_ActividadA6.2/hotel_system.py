"""Sistema de Reservas."""
import json
import os


class HotelSystem:
    """Clase base del sistema."""

    def __init__(self, filename):
        """Inicializar filename."""
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Cargar datos del archivo."""
        try:
            if not os.path.exists(self.filename):
                return []
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def save_data(self):
        """Guardar datos en archivo."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4)
        except IOError:
            print("Error guardando datos")


class Hotel(HotelSystem):
    """Clase Hotel."""

    def __init__(self):
        """Inicializar Hotel."""
        super().__init__('hotels.json')

    def create_hotel(self, hotel_id, name, city, rooms):
        """Crear un hotel."""
        if any(h['id'] == hotel_id for h in self.data):
            return False
        self.data.append({
            "id": hotel_id,
            "name": name,
            "city": city,
            "rooms": rooms
        })
        self.save_data()
        return True

    def delete_hotel(self, hotel_id):
        """Borrar un hotel."""
        original = len(self.data)
        self.data = [h for h in self.data if h['id'] != hotel_id]
        if len(self.data) < original:
            self.save_data()
            return True
        return False

    def display_hotel_info(self, hotel_id):
        """Mostrar info del hotel."""
        for hotel in self.data:
            if hotel['id'] == hotel_id:
                return hotel
        return None

    def modify_hotel_info(self, hotel_id, name=None, city=None, rooms=None):
        """Modificar hotel."""
        for hotel in self.data:
            if hotel['id'] == hotel_id:
                if name:
                    hotel['name'] = name
                if city:
                    hotel['city'] = city
                if rooms:
                    hotel['rooms'] = rooms
                self.save_data()
                return True
        return False


class Customer(HotelSystem):
    """Clase Cliente."""

    def __init__(self):
        """Inicializar Cliente."""
        super().__init__('customers.json')

    def create_customer(self, cust_id, name, email):
        """Crear cliente."""
        if any(c['id'] == cust_id for c in self.data):
            return False
        self.data.append({"id": cust_id, "name": name, "email": email})
        self.save_data()
        return True

    def delete_customer(self, cust_id):
        """Borrar cliente."""
        original = len(self.data)
        self.data = [c for c in self.data if c['id'] != cust_id]
        if len(self.data) < original:
            self.save_data()
            return True
        return False

    def display_customer_info(self, cust_id):
        """Mostrar cliente."""
        for customer in self.data:
            if customer['id'] == cust_id:
                return customer
        return None

    def modify_customer_info(self, cust_id, name=None, email=None):
        """Modificar cliente."""
        for customer in self.data:
            if customer['id'] == cust_id:
                if name:
                    hotel_name = name  # Evitar error unused var
                    customer['name'] = hotel_name
                if email:
                    customer['email'] = email
                self.save_data()
                return True
        return False


class Reservation(HotelSystem):
    """Clase Reservacion."""

    def __init__(self):
        """Inicializar Reservacion."""
        super().__init__('reservations.json')

    def create_reservation(self, res_id, cust_id, hotel_id):
        """Crear reservacion."""
        if any(r['id'] == res_id for r in self.data):
            return False
        self.data.append({
            "id": res_id,
            "cust_id": cust_id,
            "hotel_id": hotel_id
        })
        self.save_data()
        return True

    def cancel_reservation(self, res_id):
        """Cancelar reservacion."""
        original = len(self.data)
        self.data = [r for r in self.data if r['id'] != res_id]
        if len(self.data) < original:
            self.save_data()
            return True
        return False
