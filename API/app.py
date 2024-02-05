from flask import Flask, render_template, jsonify
from flask_cors import CORS  # Pour gérer les requêtes CORS
import psutil  # Pour obtenir des informations système

app = Flask(__name__)
CORS(app)  # Autorise les requêtes CORS pour l'accès depuis un autre domaine

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/system_stats')
def system_stats():
    # Obtenez les statistiques système (à adapter en fonction de vos besoins)
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    # Retourne les statistiques sous forme de JSON
    return jsonify({'cpu_percent': cpu_percent, 'memory_percent': memory_percent})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
