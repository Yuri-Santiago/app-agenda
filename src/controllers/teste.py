from src import app


"""
CONTATOS ROUTERS

index/ login/ sign up/ botaosair
tela inicial/ ler grupos/ ler contatos
adicionar grupo
adicionar contato
editar grupo
editar contato




GET api/contatos
GET api/contato/id
POST api/contato
PUT api/contato/id
DELETE api/contato/id

"""


@app.route("/")
def index():
    return "render_template('index.html)"

@app.route("/")
def index():
    return "render_template('index.html)"
