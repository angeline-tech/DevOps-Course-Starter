FROM python:3

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 

ENV PATH=$PATH:/root/.poetry/bin

WORKDIR /todo-app

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY todo_app ./todo_app

EXPOSE 5000

ENTRYPOINT [ "poetry" , "run" , "flask","run" ]

CMD [ "--host=0.0.0.0"]


