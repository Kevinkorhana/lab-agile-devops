from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)

# Task 23: Mengaktifkan CORS untuk semua domain
CORS(app)

# Task 22: Mengaktifkan Talisman Keamanan
# Catatan: force_https=False digunakan untuk keperluan testing lokal/dev environment
talisman = Talisman(
    app,
    content_security_policy=None,
    force_https=False
)

from service import routes, models