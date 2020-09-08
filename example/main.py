import logging
from datetime import datetime
from flask import Flask, render_template, request
from google.cloud import datastore


app = Flask(__name__)


# infomationレベル以下のログも出力させる
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    # res = insert()
    res = get_all()
    return res

def insert():
    # Datastoreのクライアントオブジェクトを取得
    client = datastore.Client()

    # Exampleカインドに保存するためのkeyを作成
    key = client.key('Example')

    # エンティティを作成し、プロパティを設定する
    entity = datastore.Entity(key=key)
    entity['author'] = 'Naruto Uzumaki'
    entity['created'] = datetime.now()

    # Datastoreに保存する
    client.put(entity)

    entity2 = datastore.Entity(key=key)
    entity2.update({
        'author': 'Sakura Haruno',
        'created': datetime.now(),
        })

    client.put(entity2)

    # エンティティにidプロパティを追加する
    entity['id'] = entity.key.id
    entity2['id'] = entity2.key.id

    # エンティティを返す
    return entity

def get_all():
    # Datastoreのクライアントオブジェクトを取得
    client = datastore.Client()

    # Queryオブジェクトを取得する
    query = client.query(kind='Example')

    # フィルターを追加
    query.add_filter('author', '=', 'Sasuke Uchiha')

    # 日付の新しい順
    #query.order = '-created'

    # クエリの実行
    entities = list(query.fetch())

    # すべてのエンティティにidプロパティを追加する
    for entity in entities:
        entity['id'] = entity.key.id
    
    # レスポンス用のJSONを作成
    res = {
        'example': entities
    }
    return res


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