import os

# Configuration settings
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CARTS_DIR = os.path.join(BASE_DIR, 'carts')

# Flask settings
SECRET_KEY = 'your-secret-key-here'  # Change this in production