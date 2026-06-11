from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)

# Mengaktifkan CORS
CORS(app)

# Mengaktifkan Talisman Keamanan
talisman = Talisman(
    app,
    content_security_policy=None,
    force_https=False
)

# Beri tahu linter untuk mengabaikan pengecekan impor di baris bawah ini
# flake8: noqa: F401
from service import routes, models