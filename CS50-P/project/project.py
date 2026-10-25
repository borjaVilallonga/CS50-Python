import sys
import requests
from tabulate import tabulate

# Tabla simplificada de debilidades (ataques que hacen x2 de daño a cada tipo)
WEAKNESSES = {
    "normal": ["fighting"],
    "fire": ["water", "ground", "rock"],
    "water": ["electric", "grass"],
    "electric": ["ground"],
    "grass": ["fire", "ice", "poison", "flying", "bug"],
    "ice": ["fire", "fighting", "rock", "steel"],
    "fighting": ["flying", "psychic", "fairy"],
    "poison": ["ground", "psychic"],
    "ground": ["water", "grass", "ice"],
    "flying": ["electric", "ice", "rock"],
    "psychic": ["bug", "ghost", "dark"],
    "bug": ["fire", "flying", "rock"],
    "rock": ["water", "grass", "fighting", "ground", "steel"],
    "ghost": ["ghost", "dark"],
    "dragon": ["ice", "dragon", "fairy"],
    "steel": ["fire", "fighting", "ground"],
    "fairy": ["poison", "steel"],
    "dark": ["fighting", "bug", "fairy"]
}

RESISTANCES = {
    "normal": [],
    "fire": ["fire", "grass", "ice", "bug", "steel", "fairy"],
    "water": ["fire", "water", "ice", "steel"],
    "electric": ["electric", "flying", "steel"],
    "grass": ["water", "electric", "grass", "ground"],
    "ice": ["ice"],
    "fighting": ["bug", "rock", "dark"],
    "poison": ["grass", "fighting", "poison", "bug", "fairy"],
    "ground": ["poison", "rock"],
    "flying": ["grass", "fighting", "bug"],
    "psychic": ["fighting", "psychic"],
    "bug": ["grass", "fighting", "ground"],
    "rock": ["normal", "fire", "poison", "flying"],
    "ghost": ["poison", "bug"],
    "dragon": ["fire", "water", "electric", "grass"],
    "steel": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"],
    "fairy": ["fighting", "bug", "dark"],
    "dark": ["ghost", "dark"]
}

IMMUNITIES = {
    "normal": ["ghost"],
    "fire": [],
    "water": [],
    "electric": [],
    "grass": [],
    "ice": [],
    "fighting": [],
    "poison": [],
    "ground": ["electric"],
    "flying": ["ground"],
    "psychic": [],
    "bug": [],
    "rock": [],
    "ghost": ["normal", "fighting"],
    "dragon": [],
    "steel": ["poison"],
    "fairy": ["dragon"],
    "dark": ["psychic"]
}



def main():
    print("---Analizador de equipos pokemon (1ª generación)---")
    print("Escribe el nombre de tus Pokemons para añadirlos al equipo.")
    print("Escribe 'fin' cuando hayas terminado (maximo 6). ")

    team = {}

    # Bucle: si hay error, vuelve a preguntar sin detener el programa
    while len(team) < 6:
        name = input(f"Pokemon {len(team) + 1}/6: ").strip().lower()

        if name == 'fin':
            if len(team) == 0:
                sys.exit("El programa ha terminado. No añadiste ningun Pokemon.")
            break

        if name in team:
            print("Este pokemon ya esta en tu equipo. Elige otro.")
            continue

        try:
            # 1. Obtener datos de la API
            types = get_pokemon_data(name)

            # 2. Calcular sus debelidades
            weak_to, resists = calculate_matchups(types)

            # 3. Guardar en el equipo
            team[name] = {
                "types": types,
                "weak_to": weak_to,
                "resists": resists
            }

            print(f" {name.capitalize()} añadido! Tipos: { ', '.join(types).capitalize()}")

        except ValueError as e:
            #La salvaguarda atrapa el error y permite volver a intentar
            print(f" Error: {e} Intenta con otro nombre.")

    # 4. Analizar el equipo completo y mostrar reporte
    report_data = analyze_team(team)

    print("\n--- REPORTE DE VULNERABILIDADES DEL EQUIPO ---")
    print(tabulate(report_data, headers = ["Tipo de ataque", "Pokemon Vulnerables", "Tus Counters (resistencias)", "Estado del equipo"], tablefmt = "grid"))
    print("\nConsejo: Concéntrate en buscar Pokémon que cubran las filas con estado 'Crítico'.")



def get_pokemon_data(pokemon_name):
    """
    Llama a la PokemonAPI. Devuelve una lista con los tipos si es de la 1ª Generación.
    Levanta un ValueError si no existe o si la ID es mayor que 151
    """

    if not pokemon_name:
        raise ValueError("El nombre no puede estar vacio")

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

    if response.status_code != 200:
        raise ValueError("Pokemon no encontrado.")

    data = response.json()

    if data["id"] > 151:
        raise ValueError("El pokemon debe pertenecer a la 1ª generación")

    types = [t["type"]["name"] for t in data["types"]]
    return types



def calculate_matchups(types):
    """
    Calcula debilidades y resistencias considerando combinaciones
    de tipos dobles.
    """
    modifiers = {}
    all_attack_types = WEAKNESSES.keys()

    for attack in all_attack_types:
        mod = 1.0
        for t in types:
            if attack in WEAKNESSES.get(t, []):
                mod *= 2.0
            if attack in RESISTANCES.get(t, []):
                mod *= 0.5
            if attack in IMMUNITIES.get(t, []):
                mod *= 0.0
        modifiers[attack] = mod

    # Si mod > 1, recibe daño supereficaz (x2 o x 4)
    weak_to = [atk for atk, mod in modifiers.items() if mod > 1.0]
    # Si mod < 1, recibe daño supereficaz (x0.5, x0.25 o x0)
    resists = [atk for atk, mod in modifiers.items() if mod < 1.0]

    return weak_to, resists



def analyze_team(team_dict):
    """
    Analiza el equipo cruzando las debilidades de unos con las resistencias
    de otros.
    """
    all_weaknesses = {}
    all_resistances = {}

    for pokemon, data in team_dict.items():
        for w in data["weak_to"]:
            all_weaknesses.setdefault(w, []).append(pokemon.capitalize())
        for r in data["resists"]:
            all_resistances.setdefault(r, []).append(pokemon.capitalize())

    table_data = []

    #Solo revisamos los ataques para los que tenemos algun pokemon vunerable
    for attack, vulnerables in all_weaknesses.items():
        counters = all_resistances.get(attack, [])

        if not counters:
            estado = "Critico (sin counters)"
            counters_str = "Ninguno"
        else:
            estado = "Cubierto"
            counters_str = ", ".join(counters)

        table_data.append([
            attack.capitalize(),
            ", ".join(vulnerables),
            counters_str,
            estado
        ])

    # Ordenar tabla
    table_data.sort(key= lambda x: (0 if "Critico" in x[3] else 1, -len(x[1].split(","))))

    return table_data

if __name__ == "__main__":
    main()
