from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
import todo_app.service.trello_service as trello

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/heartbeat')
def heartbeat():
    return 'Flask Server is Running'


@app.route('/')
def trello_cards():
    ascending = request.args.get('ascending') != 'false'
    trello.fetch_updated_cards()
    return render_template('index.html', cards=trello.get_cards(ascending), sort_status = ascending)


@app.route('/add', methods=['POST'])
def add_to_do():
    trello.create_to_do(request.form['title'])
    return redirect('/')


@app.route('/complete', methods=['POST'])
def complete_to_do():
    card_id = request.form['id']
    trello.move_card_to_complete(card_id)
    return redirect('/')


@app.route('/start', methods=['POST'])
def start_to_do():
    card_id = request.form['id']
    trello.move_card_to_in_progress(card_id)
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset_to_do():
    card_id = request.form['id']
    trello.move_card_to_to_do(card_id)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete_to_do():
    card_id = request.form['id']
    trello.delete_card(card_id)
    return redirect('/')


@app.route('/sort', methods=['POST'])
def sort():
    ascending = request.form['id'] == 'ASCENDING'
    return redirect('/?ascending=true') if ascending else redirect('/?ascending=false')


if __name__ == '__main__':
    app.run()
