import requests

BASE_URL = "https://api-colombia.com/api/v1"

def dish_fetch(dish_id=None):
   # """Hace la petición a la API. Si recibe un ID trae uno, si no, trae todos."""

    if dish_id is not None:
        url = f"{BASE_URL}/TypicalDish/{dish_id}"

    else:
        url = f"{BASE_URL}/TypicalDish"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        
        print(f"No me pude conectar, ayudame: {e}")
        return None

def mostrar_menu_platos():
    print("=" * 50)
    print("   🍽️ MENÚ GASTRONÓMICO DE COLOMBIA   ")
    print("=" * 50)

    # 1) ACEPTA ENTRADAS: El cliente busca por texto, sin adivinar números
    search = input("¿Qué plato deseas buscar? O (presiona ENTER para ver todo): ").lower()
    
    platos = dish_fetch()
    if platos is not None:
        # Filtramos la lista según lo que escribió el cliente
        # Si el cliente no escribió nada, mostramos todo. Si escribió algo, filtramos por nombre.
        # #   [   3. Qué guardamos 1. El ciclo 2. La condición   
        platos_filtrados = [p for p in platos if search in p.get("name", "").lower()]
        
        if not platos_filtrados:
            print(f"\n No encontramos platos que coincidan con el que estas diciendo '{search}'.")
            return

        print(f"\nSe encontraron estos {len(platos_filtrados)} platillos tradicionales:\n")
        print("-" * 50)
        
        for plato in platos_filtrados:
            nombre = plato.get("name", "No lo conozco")
            descripcion = plato.get("description", "Ahora mismo no contamos con una descripción disponible.")
            
            print(f"🍽️ Platillo: {nombre}")
            print(f"📝 Detalle: {descripcion}")
            print("-" * 50)
    else:
        print("No se pude cargar la información del menú.")

def main():
    print("Iniciando aplicación gastronómica en 1, 2, 3...")
    mostrar_menu_platos()
    input("\nPresiona ENTER para salir...")

if __name__ == "__main__":
    main()