from flask import Flask, render_template, request, redirect, url_for, abort
import os
import yaml
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Ensure carts directory exists
os.makedirs(app.config['CARTS_DIR'], exist_ok=True)

def get_cart_files():
    """Get all YAML files in the carts directory"""
    files = []
    for filename in os.listdir(app.config['CARTS_DIR']):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            files.append(filename)
    return sorted(files)

def parse_yaml_file(filename):
    """Parse a YAML file and return its contents"""
    filepath = os.path.join(app.config['CARTS_DIR'], filename)
    with open(filepath, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {filename}: {e}")
            return None

@app.route('/')
def index():
    """Show all available resource files"""
    files = get_cart_files()
    resources = []
    for filename in files:
        data = parse_yaml_file(filename)
        if data and isinstance(data, dict):
            resources.append({
                'filename': filename,
                'name': data.get('name', filename.replace('.yaml', '').replace('.yml', '')),
                'description': data.get('description', 'No description available')
            })
        else:
            resources.append({
                'filename': filename,
                'name': filename.replace('.yaml', '').replace('.yml', ''),
                'description': 'Invalid YAML format'
            })
    return render_template('index.html', resources=resources)

@app.route('/resource/<filename>')
def resource(filename):
    """Show details of a specific resource file"""
    if not (filename.endswith('.yaml') or filename.endswith('.yml')):
        abort(404)
    
    filepath = os.path.join(app.config['CARTS_DIR'], filename)
    if not os.path.exists(filepath):
        abort(404)
    
    data = parse_yaml_file(filename)
    if not data:
        abort(400, description="Invalid YAML file")
    
    return render_template('resource.html', filename=filename, data=data)

@app.route('/add', methods=['GET', 'POST'])
def add_resource():
    """Add a new resource file"""
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file and (file.filename.endswith('.yaml') or file.filename.endswith('.yml')):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['CARTS_DIR'], filename))
            return redirect(url_for('index'))
    
    return render_template('add_resource.html')

if __name__ == '__main__':
    app.run(debug=True)