import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab_10_user:ywXp3cXmRpClRAPlpfr5SpcgEfZUnBNN@dpg-cl5gifl6fh7c73emv5i0-a/lab_10")
    conn.close()
    return "Database Connection Successful!"
