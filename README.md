# CS50P - CS50's Introduction to Programming with Python

## 🎓 About The Course
This repository contains my solutions to the problem sets from **Harvard University's CS50P**. The course introduces students to programming using Python, focusing on learning how to read and write code, test it, and debug it. 

## 📚 Course Structure & Exercises

### Week 0: Functions, Variables
Introduction to the basics of Python: creating variables, formatting strings, and using built-in functions.
* **Indoor Voice**: Converts user input into lowercase.
* **Playback Speed**: Replaces spaces in a string with `...` to simulate slowed-down speech.
* **Making Faces**: Replaces text emoticons like `:)` and `:(` with corresponding emojis `🙂` and `🙁`.
* **Einstein**: Calculates energy equivalent (E=mc²) given mass as input.
* **Tip Calculator**: Calculates the tip amount based on the meal cost and desired percentage.

### Week 1: Conditionals
Learning control flow, boolean expressions, and `if`, `elif`, and `else` statements.
* **Deep Thought**: Checks if the user's input equals the Answer to the Great Question of Life (42).
* **Home Federal Savings Bank**: Returns a monetary output ($0, $20, or $100) depending on how a user greets the program.
* **File Extensions**: Returns the MIME media type of a file based on its suffix.
* **Math Interpreter**: Solves basic arithmetic expressions formatted as strings.
* **Meal Time**: Converts 12-hour and 24-hour formatted time into a decimal to output the correct meal time (breakfast, lunch, dinner).

### Week 2: Loops
Using `while` and `for` loops, iterating over lists and dictionaries.
* **camelCase**: Converts variable names formatted in camelCase into snake_case.
* **Coke Machine**: Simulates a vending machine, subtracting inserted coin values until a 50-cent Coke is paid for.
* **Just setting up my twttr**: Removes all vowels from the user's input string.
* **Vanity Plates**: Checks if a string meets the specific requirements to be a valid vanity license plate.
* **Nutrition Facts**: Outputs the number of calories for a given portion of fruit using a dictionary.

### Week 3: Exceptions
Handling runtime errors gracefully using `try` and `except` blocks.
* **Fuel Gauge**: Prompts the user for a fraction (X/Y), handles ZeroDivisionError and ValueError, and outputs fuel tank percentage.
* **Felipe's Taqueria**: Continuously accepts item orders and outputs the cumulative total cost using a dictionary.
* **Grocery List**: Takes grocery items as input and outputs a capitalized, sorted list grouped by quantity.
* **Outdated**: Converts date formats from `Month-Day-Year` to the standard `YYYY-MM-DD`.

### Week 4: Libraries
Importing and utilizing Python's built-in libraries and third-party packages via `pip`.
* **Emojize**: Converts alias strings into actual emojis using the `emoji` library.
* **Frank, Ian and Glen’s Letters**: Generates ASCII art fonts using the `pyfiglet` library.
* **Adieu, Adieu**: Formats a list of names with proper comma placement and grammar using the `inflect` library.
* **Guessing Game**: Implements a number-guessing game using the `random` library.
* **Little Professor**: Randomly generates arithmetic problems with varying levels of difficulty.
* **Bitcoin Price Index**: Fetches the current price of Bitcoin querying a JSON API via the `requests` library.

### Week 5: Unit Tests
Writing custom tests using the `pytest` library to ensure code reliability and avoid regressions.
* **Testing my twttr**: Writing tests for the Week 2 "twttr" program.
* **Back to the Bank**: Writing tests for the Week 1 "bank" program.
* **Re-requesting a Vanity Plate**: Writing tests for the Week 2 "plates" program.
* **Refueling**: Writing tests for the Week 3 "fuel" program.

### Week 6: File I/O
Reading from and writing to files, manipulating CSVs, and dealing with binary files (images).
* **Lines of Code**: Opens a Python file and counts the lines of code, excluding blank lines and comments.
* **Pizza Py**: Reads a CSV file and outputs its data formatted as an ASCII art table using `tabulate`.
* **Scourgify**: Cleans up a messy CSV file by splitting names and writing them into a new correctly formatted CSV.
* **CS50 P-Shirt**: Overlays a transparent PNG image (a CS50 shirt) onto user-provided images using the `Pillow` library.

### Week 7: Regular Expressions
Using the `re` library to match patterns, validate data, and extract specific substrings.
* **NUMB3RS**: Validates whether a given string is a correct IPv4 address.
* **Watch on YouTube**: Extracts the unique video ID from a YouTube HTML iframe string.
* **Working 9 to 5**: Uses regex to convert time ranges from 12-hour AM/PM format to 24-hour format.
* **Regular, um, Expressions**: Counts the occurrences of the standalone word "um" in a given text.
* **Response Validation**: Uses a third-party library to strictly validate email addresses.

### Week 8: Object-Oriented Programming
Designing classes, defining methods, using properties (`@property`), and understanding encapsulation.
* **Seasons of Love**: Calculates the user's exact age in minutes and prints the number in English words using `datetime`.
* **Cookie Jar**: Implements a `Jar` class to store cookies, controlling capacity and raising exceptions for invalid deposits/withdrawals.
* **CS50 Shirtificate**: Generates a custom PDF certificate with an overlaid image and user name using the `fpdf2` library.

### Week 9: Final Project
* Pokemon analyzer.


# CS50P - Introducción a la Programación con Python (CS50)

## 🎓 Sobre el Curso
Este repositorio contiene mis soluciones a los ejercicios (Problem Sets) del curso **CS50P de la Universidad de Harvard**. El curso es una introducción exhaustiva a la programación utilizando Python, centrado en escribir, leer, probar ("testear") y depurar código.

## 📚 Estructura del Curso y Ejercicios

### Semana 0: Funciones y Variables
Introducción a los conceptos básicos de Python: creación de variables, formateo de cadenas (strings) y uso de funciones integradas.
* **Indoor Voice**: Convierte el texto introducido por el usuario a minúsculas.
* **Playback Speed**: Reemplaza los espacios de una cadena de texto por `...` para simular un habla pausada.
* **Making Faces**: Reemplaza los emoticonos de texto como `:)` y `:(` por los emojis correspondientes `🙂` y `🙁`.
* **Einstein**: Calcula la equivalencia entre masa y energía (E=mc²) usando la masa introducida.
* **Tip Calculator**: Calcula la propina de una cuenta de restaurante basándose en un porcentaje elegido.

### Semana 1: Condicionales
Aprender el flujo de control, expresiones booleanas y las sentencias `if`, `elif` y `else`.
* **Deep Thought**: Comprueba si el usuario introduce la respuesta a la pregunta final de la vida (42).
* **Home Federal Savings Bank**: Devuelve una salida monetaria ($0, $20 o $100) dependiendo del saludo que el usuario escriba.
* **File Extensions**: Devuelve el tipo MIME (media type) de un archivo basándose en su extensión (ej. `.jpg`, `.pdf`).
* **Math Interpreter**: Resuelve operaciones aritméticas básicas introducidas en formato de texto.
* **Meal Time**: Convierte formatos de hora de 12 y 24 horas a decimal para indicar si es hora del desayuno, comida o cena.

### Semana 2: Bucles (Loops)
Uso de bucles `while` y `for`, iterando sobre listas y diccionarios.
* **camelCase**: Convierte nombres de variables en formato camelCase a formato snake_case.
* **Coke Machine**: Simula una máquina expendedora, restando monedas hasta cobrar los 50 centavos que cuesta la Coca-Cola.
* **Just setting up my twttr**: Elimina todas las vocales de una frase introducida.
* **Vanity Plates**: Comprueba si una cadena de texto cumple con las normas de tráfico para ser una matrícula personalizada válida.
* **Nutrition Facts**: Devuelve las calorías de una porción de fruta introducida por el usuario consultando un diccionario.

### Semana 3: Excepciones (Exceptions)
Gestión de errores en tiempo de ejecución utilizando bloques `try` y `except`.
* **Fuel Gauge**: Pide al usuario una fracción (X/Y), gestiona errores de división por cero y devuelve el porcentaje del tanque de gasolina.
* **Felipe's Taqueria**: Suma el coste total de los pedidos de comida introducidos consultando el precio en un diccionario.
* **Grocery List**: Toma una lista de la compra y devuelve el recuento de los productos ordenados alfabéticamente y en mayúsculas.
* **Outdated**: Convierte fechas del formato americano `Mes-Día-Año` al estándar internacional `YYYY-MM-DD`.

### Semana 4: Bibliotecas (Libraries)
Importar y usar bibliotecas nativas de Python y de terceros instaladas con `pip`.
* **Emojize**: Convierte alias de texto en emojis visuales reales usando la biblioteca `emoji`.
* **Frank, Ian and Glen’s Letters**: Genera letras en formato ASCII Art usando la biblioteca `pyfiglet`.
* **Adieu, Adieu**: Formatea correctamente una lista de nombres respetando la gramática inglesa usando la biblioteca `inflect`.
* **Guessing Game**: Un juego de adivinar el número usando la biblioteca `random`.
* **Little Professor**: Genera de forma aleatoria problemas matemáticos de diferentes niveles de dificultad.
* **Bitcoin Price Index**: Obtiene el precio actual del Bitcoin consumiendo una API JSON con la biblioteca `requests`.

### Semana 5: Pruebas Unitarias (Unit Tests)
Escribir tests personalizados utilizando la biblioteca `pytest` para garantizar el buen funcionamiento del código.
* **Testing my twttr**: Escribir pruebas unitarias para el ejercicio "twttr" de la Semana 2.
* **Back to the Bank**: Escribir pruebas unitarias para el ejercicio "bank" de la Semana 1.
* **Re-requesting a Vanity Plate**: Escribir pruebas unitarias para el ejercicio "plates" de la Semana 2.
* **Refueling**: Escribir pruebas unitarias para el ejercicio "fuel" de la Semana 3.

### Semana 6: Lectura/Escritura de Archivos (File I/O)
Manipulación de archivos de texto plano, archivos CSV y archivos binarios (imágenes).
* **Lines of Code**: Abre un archivo Python y cuenta cuántas líneas de código reales tiene (excluyendo comentarios y espacios en blanco).
* **Pizza Py**: Lee un archivo CSV y muestra sus datos formateados como una tabla estética usando la biblioteca `tabulate`.
* **Scourgify**: Limpia un archivo CSV desordenado, separando los nombres propios y escribiéndolos en un nuevo CSV.
* **CS50 P-Shirt**: Superpone una imagen PNG transparente (una camiseta de CS50) a fotografías subidas por el usuario usando la biblioteca `Pillow`.

### Semana 7: Expresiones Regulares (Regular Expressions)
Uso de la biblioteca `re` para buscar patrones de texto, validar datos y extraer fragmentos específicos.
* **NUMB3RS**: Valida si un texto es una dirección IPv4 matemáticamente correcta.
* **Watch on YouTube**: Extrae el ID de un vídeo de YouTube a partir de su código HTML de inserción (iframe).
* **Working 9 to 5**: Usa Regex para convertir rangos de horas del formato AM/PM a formato militar de 24 horas.
* **Regular, um, Expressions**: Cuenta el número de veces que aparece la muletilla "um" de forma aislada en un texto.
* **Response Validation**: Valida la estructura de direcciones de email usando una biblioteca externa.

### Semana 8: Programación Orientada a Objetos (OOP)
Diseño de clases, métodos, encapsulamiento y el uso de propiedades (decorators).
* **Seasons of Love**: Calcula tu edad exacta en minutos e imprime el número escrito en inglés usando la biblioteca `datetime`.
* **Cookie Jar**: Crea una clase `Jar` para almacenar galletas, controlando los límites de capacidad mediante excepciones.
* **CS50 Shirtificate**: Genera un certificado PDF con imagen y texto personalizados utilizando la biblioteca `fpdf2`.

### Semana 9: Proyecto Final
* Analizador pokemon.
  

