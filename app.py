from todoapi import app
import os

if __name__ == "__main__":
    isCloud = os.environ.get('IS_CLOUD', None)
    if isCloud is None or isCloud != 'TRUE':
        app.run(host='127.0.0.1', port=5000, debug=True)
    else:
        app.run()
