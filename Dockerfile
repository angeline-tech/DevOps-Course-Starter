FROM python:3 as base

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 

ENV PATH=$PATH:/root/.poetry/bin

WORKDIR /todo_app

COPY pyproject.toml poetry.lock ./

RUN poetry install

EXPOSE 5000

FROM base as production

COPY todo_app ./todo_app

ENTRYPOINT [ "poetry" , "run" ]

CMD [ "gunicorn","--bind", "0.0.0.0:5000", "todo_app.app:app" ]

FROM base as development

ENTRYPOINT [ "poetry" , "run" ]

CMD [ "flask","run", "--host=0.0.0.0" ]

