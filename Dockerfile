FROM python:3

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 

ENV PATH=$PATH:/root/.poetry/bin

WORKDIR /todo-app

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY todo_app ./todo_app

EXPOSE 5000

ENTRYPOINT [ "poetry" , "run" ]

CMD [ "gunicorn","--bind", "0.0.0.0:5000", "todo_app.app:app" ]



