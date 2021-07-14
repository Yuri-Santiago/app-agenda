from src.models.usuario import Usuario
import pickle

usuarios = [Usuario(1000, "Yuri", "yuri@gmail.com", "senha"), Usuario(1001, "Raquel", "raquel@gmail.com", "12345"),
            Usuario(1002, "Pablo", "pablo@gmail.com", "secreto"), Usuario(1003, "Kelvin", "kelvin@gmail.com", "54321")]

with open('banco.pickle', 'wb') as novo_banco:
    pickle.dump(usuarios, novo_banco)
