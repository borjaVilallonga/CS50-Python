import pytest
from project import get_pokemon_data, calculate_matchups, analyze_team



def test_get_pokemon_data():
    # Prueba con un pokemon valido de primera generacion
    assert get_pokemon_data("bulbasaur") == ["grass", "poison"]
    assert get_pokemon_data("charizard") == ["fire", "flying"]

    # Prueba con un pokemon
    with pytest.raises(ValueError):
        get_pokemon_data("chikorita")

    # Prueba con texto inventado
    with pytest.raises(ValueError):
        get_pokemon_data("digimon")

    # Prueba con entrada vacia
    with pytest.raises(ValueError):
            get_pokemon_data("")



def calculate_matchups():
    # Prueba con un tipo unico
    weak_to, resists = calculate_matchups(["Electric"])
    assert "ground" in weak_to
    assert "electric" in resists
    assert "flying" in resists
    assert "steel" in resists

    # Prueba tipo doble
    weak_to_bulb, resists_bulb = calculate_matchups(["grass", "poison"])
    assert "fire" in weak_to_bulb
    assert "psychic" in weak_to_bulb
    assert "grass" in resists_bulb

    # Comprobacion de neutralidad cruzada
    assert "bug" in weak_to_bulb
    assert "bug" in resists_bulb



def test_analyze_team():
     # Creamos un equipo de prueba ficticio para no depender de la API en este test
    mock_team = {
        "charmander": {
            "types": ["fire"],
            "weak_to": ["water", "ground", "rock"],
            "resists": ["fire", "grass", "bug", "fairy"]
        },
        "bulbasaur": {
            "types": ["grass", "poison"],
            "weak_to": ["fire", "ice", "flying", "psychic"],
            "resists": ["water", "grass", "electric", "fighting", "fairy"]
        }
    }

    report = analyze_team(mock_team)

    # Buscar la fila correspondiente al ataque "Water" en el reporte generado
    # Formato de fila: [Ataque, Vulnerables, Counters, Estado]
    water_row = next(row for row in report if row[0] == "Water")
    assert water_row[1] == "Charmander"  # Charmander es el vulnerable
    assert "Bulbasaur" in water_row[2]   # Bulbasaur lo resiste
    assert "Cubierto" in water_row[3]

    # Buscar la fila correspondiente al ataque "Ground"
    ground_row = next(row for row in report if row[0] == "Ground")
    assert ground_row[1] == "Charmander"
    assert "Ninguno" in ground_row[2]
    assert "Critico" in ground_row[3]
