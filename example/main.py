import logging
from flask import Flask, render_template, request


app = Flask(__name__)


# infomationレベル以下のログも出力させる
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/', methods=['GET'])
def home():
    message = 'Logging Sample'
    return render_template('index.html', message=message)


@app.route('/api/examples/<key_id>')
@app.route('/api/examples', methods=['GET', 'POST'])
def examples(key_id=None):
    if request.method == 'GET':
        if key_id:
            igarashi = {
                'author': 'Tsuyoshi Igarashi',
                'id': 1
            }
            return igarashi
        else:
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
    elif request.method == 'POST':
        json_data = request.get_json()
        res = {
            'id': 999,
            'author': json_data['author']
        }
        return res, 201


@app.errorhandler(404)
def error_404(exception):
    logging.exception(exception)
    return {'message': 'Error: Resouce not found.'}, 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)