from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Пример данных
performances = [
    {"id": 1, "name": "Hamlet", "date": "2025-02-28"},
    {"id": 2, "name": "Romeo and Juliet", "date": "2025-03-01"},
    {"id": 3, "name": "The Master and Margarita", "date": "2025-03-05"},
]

# Главная страница
@app.route('/')
def home():
    return "Добро пожаловать в Театр! Используйте /search для поиска спектаклей."

# Поиск спектаклей по имени
@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name', '').lower()
    date_str = request.args.get('date', '')
    
    # Если задана дата, парсим её
    date = None
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Неверный формат даты. Используйте формат YYYY-MM-DD"}), 400

    # Фильтрация по имени и дате
    result = []
    for performance in performances:
        match_name = name in performance['name'].lower() if name else True
        match_date = datetime.strptime(performance['date'], "%Y-%m-%d") == date if date else True
        
        if match_name and match_date:
            result.append(performance)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
