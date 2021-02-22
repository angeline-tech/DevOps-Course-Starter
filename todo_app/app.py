from flask import Flask, render_template, request, redirect, Blueprint

from todo_app.data.ViewModel import ViewModel
from todo_app.flask_config import Config
import todo_app.service.trello_service as trello

bp = Blueprint('todo_app', __name__)

@bp.route('/heartbeat')
def heartbeat():
    return 'Flask Server is Running'


@bp.route('/')
def trello_cards():
    ascending = request.args.get('ascending') != 'false' # default to true
    show_older = request.args.get('show_older') != 'false' # default to true
    trello.fetch_updated_cards()
    model = ViewModel(trello.get_cards(ascending), ascending,show_older)
    return render_template('index.html', view_model=model)


@bp.route('/add', methods=['POST'])
def add_to_do():
    trello.create_to_do(request.form['title'])
    return redirect('/')


@bp.route('/complete', methods=['POST'])
def complete_to_do():
    card_id = request.form['id']
    trello.move_card_to_complete(card_id)
    return redirect('/')


@bp.route('/start', methods=['POST'])
def start_to_do():
    card_id = request.form['id']
    trello.move_card_to_in_progress(card_id)
    return redirect('/')


@bp.route('/reset', methods=['POST'])
def reset_to_do():
    card_id = request.form['id']
    trello.move_card_to_to_do(card_id)
    return redirect('/')


@bp.route('/delete', methods=['POST'])
def delete_to_do():
    card_id = request.form['id']
    trello.delete_card(card_id)
    return redirect('/')


@bp.route('/sort', methods=['POST'])
def sort():
    ascending = request.form['id'] == 'ASCENDING'
    return redirect('/?ascending=true') if ascending else redirect('/?ascending=false')


@bp.route('/show_older', methods=['POST'])
def show_older():
    show_older = request.form['id'] == 'true'
    return redirect('/?show_older=true') if show_older else redirect('/?show_older=false')

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
