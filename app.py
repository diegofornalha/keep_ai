from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from main import main
from server.config.settings import get_supabase_client

app = Flask(__name__, 
    template_folder='server/templates',
    static_folder='server/static'
)

# Inicializa o agente
agent = main()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.svg')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.svg', mimetype='image/svg+xml')

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '')
    try:
        response = agent.run(message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notes')
def get_notes():
    try:
        # Obtém o cliente Supabase usando a função do settings
        supabase = get_supabase_client()
        
        # Busca todas as notas ordenadas por data
        result = supabase.table('notes').select('*').order('data', desc=True).execute()
        
        # Retorna os dados diretamente
        return jsonify({
            'response': result.data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Obtém a porta do ambiente ou usa 3000 como padrão
    port = int(os.environ.get('PORT', 3000))
    # Executa o app Flask
    app.run(host='0.0.0.0', port=port, debug=True)
