from todoapi import app
import config

if __name__ == "__main__":
    if config.cloud_config:
        app.run()
    else:
        app.run(host='127.0.0.1', port=5000, debug=True)
