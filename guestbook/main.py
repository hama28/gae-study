from flask import Flask, render_template, abort, request


app = Flask(__name__)


@app.route('/')
def home():
    message = 'App Engine勉強会 にようこそ'
    return render_template('index.html', message=message)


@app.route('/api/greetings')
def greetings(key_id=None):
    if request.method == 'GET':
        igarashi = {
            'id': 1,
            'author': 'Tsuyoshi Igarashi',
            'message': 'Hello'
        }
        miyayama = {
            'id': 2,
            'author': 'Ryutaro Miyayama',
            'message': 'Looks good to me'
        }
        shirakawa = {
            'id': 3,
            'author': 'Mai Shirakawa',
            'message': 'Banana!'
        }
        greetings = [igarashi, miyayama, shirakawa]
        res = {
            'greetings': greetings
        }
        return res


@app.route('/err500')
def err500():
    abort(500)


@app.errorhandler(404)
def error_404(exception):
    return {'message': 'Error: Resouce not found.'}, 404


@app.errorhandler(500)
def error_500(exception):
    return {'message': 'Please contact the administrator.'}, 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)