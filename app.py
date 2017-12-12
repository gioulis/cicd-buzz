import os
import signal
from flask import Flask, render_template
from buzz import generator

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    buzz = generator.generate_buzz()
    return render_template('index.html', buzz=buzz)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port) # port 5000 is the default
