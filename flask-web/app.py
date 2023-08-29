from flask import Flask, render_template, request, redirect, send_file, send_from_directory
import json, os

app = Flask(__name__)

def trim_text(data, amount=10000):
    data['actions_metadata'] = {}

    total_length = 0
    trimmed_actions = []

    for action in reversed(data['actions']):
        if total_length + len(action) <= amount:
            trimmed_actions.insert(0, action)
            total_length += len(action)
        else:
            break

    data['actions'] = trimmed_actions

    return data

@app.route('/', methods=['GET', 'POST'])
def trim_web():
    if request.method == 'POST':
        file = request.files['file']
        amount = int(request.form['amount'])
        
        if file and file.filename != '':
            data = json.load(file)
            trimmed_data = trim_text(data, amount)
            trimmed_filename = "trimmed_" + file.filename
            with open(trimmed_filename, 'w', encoding='utf-8') as trimmed_file:
                json.dump(trimmed_data, trimmed_file, ensure_ascii=False, indent=4)
            return send_file(trimmed_filename, as_attachment=True)
    
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/site.webmanifest')
def webmanifest():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'site.webmanifest', mimetype='application/manifest+json')

@app.route('/<icon_filename>')
def icon(icon_filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'icons'),
                               icon_filename, mimetype='image/png')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)
