# from src import db
#
# # for many to many relationship (contact e groups)
# agrupamentos = db.Table('agrupamentos',
#                         db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True),
#                         db.Column('contact_id', db.Integer, db.ForeignKey('contact.id'), primary_key=True))
#
#
# class Contact(db.Model):
#     __tablename__ = "contact"
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(100))
#     endereco = db.Column(db.String(100))
#     cidade = db.Column(db.String(100))
#     telefone = db.Column(db.String(100))
#     cep = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     groups = db.relationship('group', secondary=agrupamentos, backref=db.backref('participants', lazy=True))
#     id_contatos = 0
#
#     def __init__(self, nome, endereco, cidade, telefone, cep, email):
#         self.id = Contact.id_contatos
#         Contact.id_contatos += 1
#         self.nome = nome
#         self.endereco = endereco
#         self.cidade = cidade
#         self.telefone = telefone
#         self.cep = cep
#         self.email = email
#
#     def to_json(self):
#         return {'id': self.id,
#                 'nome': self.nome,
#                 'endereco': self.endereco,
#                 'cidade': self.cidade,
#                 'telefone': self.telefone,
#                 'cep': self.cep,
#                 'email': self.email}
#
#
# class Group(db.Model):
#     __tablename__ = "group"
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(100))
#     descricao = db.Column(db.String(100))
#     # membros ?
#
#     id_grupos = 0
#
#     def __init__(self, nome, descricao, membros):
#         self.id = Group.id_grupos
#         Group.id_grupos += 1
#         self.nome = nome
#         self.descricao = descricao
#         self.membros = [self.membros.append(membro) for membro in membros]
#
#     def to_json(self):
#         return {'id': self.id,
#                 'nome': self.nome,
#                 'descricao': self.descricao,
#                 'membros': self.membros}
#
#
# class Account(db.Model):
#     __tablename__ = "account"
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     senha = db.Column(db.String(100))
#
#     id_contas = 0
#
#     def __init__(self, nome, email, senha):
#         self.id = Account.id_contas
#         Account.id_contas += 1
#         self.nome = nome
#         self.email = email
#         self.senha = senha
#
#     def to_json(self):
#         return {'id': self.id,
#                 'nome': self.nome,
#                 'email': self.email,
#                 'senha': self.senha}
#
#
# # db.create_all()
# # eu = Contact("Raquel", "Rua1", "fortaleza", "12411432", "248233", "raquel@gmail")
# # db.session.add(eu)
# # db.session.commit()
