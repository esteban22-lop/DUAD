#JSON

import json
import os


default_file_path = "Pokemon.json"


def load_pokemon_list(file_path: str) -> list[dict]:
    if not os.path.exists(file_path):
        return []
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return []
            
            data = json.loads(content)
            
            if not isinstance(data, list):
                print("Warning: JSON root is not a list. Starting with an empty list.")
                return []
            
            return data
    except(OSError, json.JSONDecodeError) as error:
        print(f"Warning: Could not load JSON file. Starting with an empty list. Details: {error}")
        return []


def save_pokemon_list(file_path: str, pokemons: list[dict]) -> None:
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(pokemons, file, indent=2, ensure_ascii=False)
    except OSError as error:
        print(f"Error: Could not save to file. Details: {error}")



def get_non_empty_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a non-empty value.")


def get_int_input(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")


def parse_types(types_raw: str) -> list[str]:
    parts = [t.strip() for t in types_raw.split(",")]
    return [t for t in parts if t]


def pokemon_name_exists(pokemons: list[dict], new_name: str) -> bool:
    new_name_lower = new_name.strip().lower()
    
    for p in pokemons:
        existing_game = p.get("name", {}).get("english", "")
        if existing_game.strip().lower() == new_name_lower:
            return True
    
    return False


def build_new_pokemon() -> dict:
    name_english = get_non_empty_input("Enter Pokemon name (english):  ")
    
    types_raw = get_non_empty_input(
        "Enter Pokemon types (comma-separated, e.g., 'Fire', or 'Fire, Flying'): "
    )
    types_list = parse_types(types_raw)
    
    base_stats = {
        "HP": get_int_input("Enter HP: "),
        "Attack": get_int_input("Enter Attack: "),
        "Defense": get_int_input("Enter Defense: "),
        "Sp. Attack": get_int_input("Enter Sp. Attack: "),
        "Sp. Defense": get_int_input("Enter Sp. Defense: "),
        "Speed": get_int_input("Enter Speed: "),
        
    }
    return {
        "name": {"english": name_english},
        "type": types_list,
        "base": base_stats,
        
    }


def main() -> None: 
    print(" Pokemon JSON Manager ")
    
    file_path = input(
        f"Enter JSON file path (Press Enter for {default_file_path}): "
    ).strip()
    
    if not file_path:
        file_path = default_file_path
    
    pokemons = load_pokemon_list(file_path)
    print(f"Loaded {len(pokemons)} Pokemon(s) from '{file_path}'. ")
    
    new_pokemon = build_new_pokemon()
    new_name = new_pokemon["name"]["english"]
    
    if pokemon_name_exists(pokemons, new_name):
        print(f"Error: A Pokemon named '{new_name}' already exists. Nothing was saved.")
        return
    
    pokemons.append(new_pokemon)
    save_pokemon_list(file_path, pokemons)
    
    print(f"Success! '{new_name}' was added.")
    print(f"Now the file contains {len(pokemons)} Pokemon(s). ")


if __name__ == "__main__":
    main()


