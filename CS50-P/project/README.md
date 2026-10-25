#  Pokemon Team Analyzer (1st Generation)
#### Video Demo: https://www.youtube.com/watch?v=H13p93zrNsE
#### Description:

This project is the final project of CS50P (CS50 Introduction to Programming with Python). It is a command-line interface (CLI) tool designed to help Pokemon players build competitive and balanced teams, focusing on the original 151 first-generation Pokemon.

## The problem
In pokemon, the combat system relies on elemental types that work like a complex game of rock-paper-scissors. Knowing the weaknesses of a singel Pokemon is relatively easy, but analyzing a full team of six is a bigger challenge.

The real problem is try to find a critical weakness across the entire team. For example, if you have Charmander(weak to water), you need to make sure you have someone like Bulbasaur (who resists water) on your team to make a safe switch during battle. This concept is called a "Counter" or defensive coverage.

## The solution
My program solves this problem by automating the team's synergistic analysis. The program evaluates the team as a total.

The user inputs up to 6 Pokemon names. The program does the following:
    1 **Validation and Data Extraction:** It connects to the PokeAPI to fetch the elemental types of the entires Pokemon. It also validates that the inputted Pokemon strictly belongs to the 1st Generation. If the user makes a typo, the program catches the exception and allows them to try again without crashing.
    2 **Dual Types Calculation:** Many pokemons have two types. The program uses comprehensive dictionaries for weaknesses, resistances, and immunities, multipliying the damage modifiers (x2, x0.5, x0). Thanks to this, it undertands that even thoung the Grass type is weak to Bug, the Poison type resists it, resulting in neutral damage.
    3 **Coverage Analysis:** Finally, it cross-references the weaknesses of each team member with the resistances of the rest of the team.

## Code Structure
The project consists of two main files:

### 'project.py'
Contains the core logic of the program and is divided into three main functions:
    *  'get_pokemon_data(pokemon_name)': Handles API calls and error handling if the pokemon doesn't exists or is from other generation.
    *  'calculate_matchups(types)': The math engine. It calculates damage modifiers to determine exactly what the pokemon is vulnerable to and what  it resists, perfectly handling dual-type combinations.
    *  'analyze_team(team_dict)': Groups the data and generates the final report. It determines if a vulnerability is covered by a "Counter" on the team, or if it is in a critical state.

### 'test_project.py'
Contains the core logic of the program and is divided into three main functions:
    *  That the API returns the correct types for valid Pokemon and raises errors for empty, erroneous, or out-of-generation inputs.
    *  That the dual-type math works (correctly neutralizing weaknesses).
    *  That the report generator correctly assigns the "Covered" or "Critical" state based on a diccionaries.

## Design decisions
One of the most important design decisions was how to handle modern types. Although the program is restricted to the original 151 Pokemon, the PokeAPI returns updated types according to modern standars. To ensure acurate calculations and prevent program crashes, I decided to include all 18 modern types in the internal logic dictionaries.

Another decision war the use of 'tabulate' to show the result in a better way.
