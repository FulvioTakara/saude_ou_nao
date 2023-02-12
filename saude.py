"""Estudo prático sobre classes e objetos"""
class Corpo():
    _forte = False;
    _obeso = False;

class Adoecido(Corpo):
    _obeso = True;
    print('Cuidado: Ficar acima do peso pode gerar patologias como diabetes, colesterol, hipertensão.')

class Saudavel(Corpo):
    _forte = True;
    print("Parabéns: Um percentual alto de musculos evita patologias como diabetes, colesterol, hipertensão.")

Maria = Adoecido;
print(Maria);
Almerinda = Saudavel;
print(Almerinda);
Joao = Adoecido;
print(Joao);
