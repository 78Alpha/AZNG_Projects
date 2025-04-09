from flask import Flask, render_template, url_for, request, request, redirect, session
import random
import code128
import os
import glob

app = Flask(__name__)
app.secret_key = 'code78'
images = ["image1.jpg", "image2.jpg", "image3.jpg"]


def code128_gen(text, name):
    image_ = f"static/images/{name}.png".replace(":", "_")
    code128.image(text).save(image_)

    return str(image_.strip("static"))


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/tip', methods=['GET', 'POST'])
def tip_calculator():
    if request.method == 'POST':
        tip = request.form.get('tip')
        # session['username'] = request.form['username'].upper()
        return redirect(url_for('celebration'))
    #session['username'] = request.form['username'].upper()
    #username = session.get('username').upper()
    return render_template('tip.html', username="AFM")


@app.route('/celebration', methods=['GET', 'POST'])
def celebration():
    # if request.method == 'POST':
    #     tip = request.form.get('tip')
    #     session['username'] = request.form['username'].upper()
    #     return redirect(url_for('celebration'))
    # session['username'] = request.form['username'].upper()
    #username = session.get('username').upper()

    return render_template('celebration.html', username="AFM")


@app.route('/barcode')
def barcode():
    return render_template('barcode.html', old_text="")

def name_pairing(data):
    image_names = []
    for image in data:
        base_name = os.path.basename(image)
        item_name = base_name.split(".png")[0]
        image = (image.split("./static")[-1]).replace("\\", "/")
        image_names.append((image, item_name))
    print(image_names)
    return image_names

@app.route('/reset', methods=['GET', 'POST'])
def reset_page():
    station_images = sorted(glob.glob("./static/utilities/station/*.png"))
    scanner_images = sorted(glob.glob("./static/utilities/scanner/*.png"))
    labor_track_images = sorted(glob.glob("./static/utilities/labor/*.png"))
    station_images = name_pairing(station_images)
    scanner_images = name_pairing(scanner_images)
    labor_track_images = name_pairing(labor_track_images)
    return render_template('reset.html', station=station_images, scanner=scanner_images, labor=labor_track_images)


@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    old_text = text.strip(" ")
    text_array = text.split("\r\n")
    images = []
    for text_snip in text_array:
        print(text_snip)
        images.append((code128_gen(text_snip, text_snip), text_snip))
    print(images)
    return render_template('barcode.html', images=images, old_text=old_text)



if __name__ == '__main__':
    app.run()
