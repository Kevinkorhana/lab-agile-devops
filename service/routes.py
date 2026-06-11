from flask import jsonify, request, make_response, abort
from service import app
from service.models import Account, DataValidationError

@app.route("/health", methods=["GET"])
def health():
    """Endpoint untuk mengecek status aplikasi (Kubernetes Health Check)"""
    return make_response(jsonify(status="OK"), 200)

# ------------------------------------------------------------------
# 1. CREATE AN ACCOUNT (Task 13)
# ------------------------------------------------------------------
@app.route("/accounts", methods=["POST"])
def create_accounts():
    """Membuat akun baru"""
    app.logger.info("Request to create an Account")
    check_content_type("application/json")
    
    account = Account()
    account.deserialize(request.get_json())
    account.create()
    
    return make_response(jsonify(account.serialize()), 201)

# ------------------------------------------------------------------
# 2. LIST ALL ACCOUNTS (Task 10 & 14)
# ------------------------------------------------------------------
@app.route("/accounts", methods=["GET"])
def list_accounts():
    """Mengambil semua daftar akun"""
    app.logger.info("Request to list all Accounts")
    accounts = Account.all()
    return make_response(jsonify(accounts), 200)

# ------------------------------------------------------------------
# 3. READ AN ACCOUNT (Task 9 & 15)
# ------------------------------------------------------------------
@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    """Membaca data satu akun berdasarkan ID"""
    app.logger.info(f"Request to read Account with id: {account_id}")
    account = Account.find(account_id)
    if not account:
        abort(404, f"Account with id [{account_id}] could not be found.")
    return make_response(jsonify(account.serialize()), 200)

# ------------------------------------------------------------------
# 4. UPDATE AN ACCOUNT (Task 11 & 16)
# ------------------------------------------------------------------
@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    """Mengubah data akun yang sudah ada"""
    app.logger.info(f"Request to update Account with id: {account_id}")
    account = Account.find(account_id)
    if not account:
        abort(404, f"Account with id [{account_id}] could not be found.")
        
    account.deserialize(request.get_json())
    account.update()
    return make_response(jsonify(account.serialize()), 200)

# ------------------------------------------------------------------
# 5. DELETE AN ACCOUNT (Task 12 & 17)
# ------------------------------------------------------------------
@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    """Menghapus akun berdasarkan ID"""
    app.logger.info(f"Request to delete Account with id: {account_id}")
    account = Account.find(account_id)
    if account:
        account.delete()
    return make_response("", 204)

def check_content_type(media_type):
    """Mengecek tipe konten request"""
    if request.headers.get("Content-Type") == media_type:
        return
    app.logger.error(f"Invalid Content-Type: {request.headers.get('Content-Type')}")
    abort(415, f"Content-Type must be {media_type}")