from flask import Flask,render_template,request,redirect
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/heartbeat')
def heartbeat():
    return 'Flask Server is Running'


@app.route('/')
def index():
    return render_template('index.html', items=get_items())


@app.route('/add', methods=['POST','GET'])
def add_to_do():
    print("Add has been called")
    print(request.form.to_dict())
    add_item(request.form['title'])
    return redirect('/')


if __name__ == '__main__':
    app.run()
