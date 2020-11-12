from flask import Flask, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item, save_item, get_item, delete_item
from todo_app.flask_config import Config
from todo_app.service.trello_service import get_all_cards

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/heartbeat')
def heartbeat():
    return 'Flask Server is Running'


@app.route('/session')
def session_cards():
    return render_template('index.html', items=get_items())


@app.route('/')
def trello_cards():
    return render_template('trello_index.html', cards=get_all_cards())


@app.route('/add', methods=['POST'])
def add_to_do():
    add_item(request.form['title'])
    return redirect('/')


@app.route('/complete', methods=['POST'])
def update_to_do():
    id = request.form['id']
    item = get_item(id)
    item['status'] = "Complete"
    save_item(item)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete_to_do():
    id = request.form['id']
    item = get_item(id)
    delete_item(item)
    return redirect('/')


@app.route('/playground')
def playground():
    response = get_all_cards()
    return response.__str__()


if __name__ == '__main__':
    app.run()
