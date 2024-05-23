from flask import Flask, render_template, url_for, request
import random
import code128
import os
import glob

app = Flask(__name__)

# List of image filenames
images = ["image1.jpg", "image2.jpg", "image3.jpg"]


def code128_gen(text, name):
    image_ = f"static/images/{name}.png".replace(":", "_")
    code128.image(text).save(image_)
    return str(image_.strip("static"))


@app.route('/')
def home():
    # try:
    #     for item in glob.glob("static/images/*.*"):
    #         os.remove(item)
    # except:
    #     pass
    return render_template('home.html')


@app.route('/display_image')
def display_image():
    image_url = url_for('static', filename=f'images/{random.choice(images)}')
    return render_template('display_image.html', image_url=image_url)


@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    text_array = text.split("\r\n")
    images = []
    for text_snip in text_array:
        print(text_snip)
        images.append((code128_gen(text_snip, text_snip), text_snip))
    return render_template('result.html', images=images)


if __name__ == '__main__':
    app.run()