# FruityVice API Project

## Overview

This project demonstrates how to interact with the FruityVice REST API using Python. It covers the fundamentals of working with APIs, including sending HTTP GET requests, handling query parameters, parsing JSON responses, and extracting useful nutritional information from the returned data.

The project was developed as part of learning Python for data retrieval and analysis.

---

## Features

This project demonstrates how to:

* Send HTTP GET requests using the `requests` library.
* Retrieve fruit information from the FruityVice API.
* Use query parameters to filter API responses.
* Parse JSON responses into Python objects.
* Extract specific nutritional information.
* Search for a fruit by name and display its protein content.
* Find the fruit with the highest sugar content.

---

## Technologies Used

* Python 3
* Requests library
* FruityVice REST API

---

## Project Structure

```
Fruityvice-project/
│
├── Fruityvice project.py
├── README.md
```

---

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/fruityvice-project.git
```

Navigate into the project folder:

```bash
cd fruityvice-project
```

Install the required package:

```bash
pip install requests
```

---

## How to Run

Run the Python script:

```bash
python "Fruityvice project.py"
```

---

## API Endpoints Used

### Retrieve fruits based on minimum fat content

```text
https://www.fruityvice.com/api/fruit/fat?min=5
```

### Retrieve a specific fruit

```text
https://www.fruityvice.com/api/fruit/banana
```

---

## Example Tasks

### 1. Request fruits with a minimum fat content

The script retrieves all fruits whose fat content is greater than or equal to 5 grams.

### 2. Find the protein content of a selected fruit

Example:

```
Least favourite fruit: Avocado
Protein: 2.0 g
```

### 3. Find the fruit with the highest sugar content

The program searches through all returned fruits and identifies the one containing the highest amount of sugar.

Example output:

```
Fruit with the highest sugar content:
Name: Durian
Sugar: 6.75 g
```

---

## Skills Demonstrated

* REST API integration
* HTTP requests
* JSON parsing
* Python dictionaries
* Python lists
* Loops
* Conditional statements
* Lambda functions
* Built in Python functions (`max`)
* Data extraction

---

## Learning Objectives

This project helped develop practical experience with:

* Consuming REST APIs
* Working with JSON data
* Automating data retrieval
* Performing simple data analysis in Python

---

## Future Improvements

Possible extensions include:

* Allow users to search for any fruit interactively.
* Display all nutritional values in a formatted table.
* Sort fruits by calories, sugar, protein, or fat.
* Export results to a CSV file.
* Visualize nutritional information using Matplotlib.
* Build a simple web interface using Flask or Streamlit.

---



Created by **Your Name**

This project was developed for learning Python programming, REST APIs, and JSON data handling.
