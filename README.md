# Create-A-REST-API-with-FastAPI-SQLAlchemy-and-PostgreSQL.
Create A REST API with FastAPI, SQLAlchemy and PostgreSQL.
[link](https://www.youtube.com/watch?v=2g1ZjA6zHRo)

venv 

    python3 -m venv .venv

    source .venv/bin/activate

    pip install --upgrade pip

    Para gerar esse arquivo, uma possibilidade é, dentro do ambiente virtual, digitar o seguinte comando:

        pip freeze > requirements.txt

    ## E, para instalar os pacotes necessários a um projeto, a partir de um arquivo requirements.txt:

        pip install -r requirements.txt

uvicorn main:app --reload
