'''from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Function to fetch and format Nobel Prize data


def fetch_nobel_prize_data():
    try:
        url = 'https://api.nobelprize.org/v1/prize.json'
        response = requests.get(url)

        if response.status_code == 200:
            prizes = response.json()['prizes']
            formatted_prizes = []

            for prize in prizes:
                formatted_prize = {
                    "year": prize['year'],
                    "category": prize['category'],
                    "motivation": prize['motivation'],
                    "laureates": [
                        {
                            "id": laureate['id'],
                            "firstName": laureate['firstname'],
                            "surName": laureate['surname']
                        } for laureate in prize.get('laureates', [])
                    ]
                }
                formatted_prizes.append(formatted_prize)

            return formatted_prizes
        else:
            return None
    except requests.RequestException as e:
        print("Request Exception:", e)
        return None

# Route to serve Nobel Prize data


@app.route('/prizes')
def get_prizes():
    prizes = fetch_nobel_prize_data()

    if prizes:
        return jsonify({"prizes": prizes})
    else:
        return "Failed to fetch Nobel Prize data", 500


if __name__ == '__main__':
    app.run(debug=True)'''
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Function to fetch and format Nobel Prize data


def fetch_and_format_prize_data():
    try:
        url = 'https://api.nobelprize.org/v1/prize.json'
        response = requests.get(url)

        if response.status_code == 200:
            prizes = response.json().get('prizes', [])
            formatted_prizes = []

            for prize in prizes:
                formatted_prize = {
                    "year": prize.get('year', 'N/A'),
                    "category": prize.get('category', 'N/A'),
                    "motivation": prize.get('motivation', 'N/A'),
                    "laureates": [
                        {
                            "id": laureate['id'],
                            "firstName": laureate['firstname'],
                            "surName": laureate['surname']
                        } for laureate in prize.get('laureates', [])
                    ]
                }
                formatted_prizes.append(formatted_prize)

            return formatted_prizes
        else:
            return None
    except requests.RequestException as e:
        print("Request Exception:", e)
        return None

# Route to serve Nobel Prize data


@app.route('/prizes')
def get_prizes():
    prizes = fetch_and_format_prize_data()

    if prizes:
        return jsonify({"prizes": prizes})
    else:
        return "Failed to fetch Nobel Prize data", 500


if __name__ == '__main__':
    app.run(debug=True)
