FROM python:3.9-slim

# Menentukan working directory di dalam container
WORKDIR /app

# Menyalin file dependensi dan menginstalnya
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh kode proyek ke dalam container
COPY . .

# Membuka port sesuai instruksi Kubernetes (Port 8080)
EXPOSE 8080

# Menjalankan aplikasi menggunakan WSGI Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "service:app"]