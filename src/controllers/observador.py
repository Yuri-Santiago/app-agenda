from flask import render_template

from src.controllers.i_observador import IObservador


class Observador(IObservador):
    def renderizar(self, tela, usuario):
        return render_template(tela, usuario=usuario)
