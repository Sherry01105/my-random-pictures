import random
from flask import Flask, redirect

app = Flask(__name__)

GITHUB_USER = "Sherry01105"
GITHUB_REPO = "my-random-pictures"

IMAGE_FILES = [
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
    "7.png",
    "8.png"
]

@app.route('/')
def random_image():
    selected_file = random.choice(IMAGE_FILES)
    raw_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main/{selected_file}"
    return redirect(raw_url)

if __name__ == '__main__':
    app.run(debug=True)
