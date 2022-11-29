from flask import Flask, render_template
import random
from jinja2.utils import markupsafe 

app = Flask(__name__)

# list of cat images
images = [
    "https://cataas.com/cat/gif",
    "https://cataas.com/cat"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
