from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    message = 'Hello World!'
    return render_template('index.html', message=message)


@app.route('/api/examples')
def examples():
    if request.method == 'GET':
        igarashi = {
            'author': 'Tsuyoshi Igarashi',
            'id': 1
        }
        miyayama = {
            'author': 'Ryutaro Miyayama',
            'id': 2
        }
        shirakawa = {
            'author': 'Mai Shirakawa',
            'id': 3
        }
        examples = [igarashi, miyayama, shirakawa]
        res = {
            'examples': examples
        }
        return res


@app.errorhandler(404)
def error_404(exception):
    return {'message': 'Error: Resouce not found.'}, 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)