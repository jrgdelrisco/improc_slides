from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Curso PDI")


@app.route('/intro')
def intro():
    return render_template('slides_01.html', title="Introducción")


@app.route('/toolbox')
def toolbox():
    return render_template('slides_02.html', title="Laboratorio")


@app.route('/fourier')
def fourier():
    return render_template('slides_03.html', title="Transformada de Fourier")


@app.route('/enhancing')
def enhancing():
    return render_template('slides_04.html', title="Mejoramiento de Imágenes")


@app.route('/segmentation')
def segmentation():
    return render_template('slides_05.html', title="Segmentación")


if __name__ == '__main__':
    app.run(debug=True)
