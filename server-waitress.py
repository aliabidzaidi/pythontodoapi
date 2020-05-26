from waitress import serve
from todoapi import app

# app.run(host='127.0.0.1', port=5000, debug=True)
# serve(app, host='127.0.0.1', port=5000)
serve(app)