"""Estudo prático sobre classes e objetos"""
# Foi criada a classe de referência
class Corpo():
    _forte = False;
    _obeso = False;

# Foram criadas as classes herdeiras
class Adoecido(Corpo):
    _obeso = True;
    print('Cuidado: Ficar acima do peso pode gerar patologias como diabetes, colesterol, hipertensão.')

class Saudavel(Corpo):
    _forte = True;
    print("Parabéns: Um percentual alto de musculos evita patologias como diabetes, colesterol, hipertensão.")

# Objetos
Maria = Adoecido;
print(Maria);
Almerinda = Saudavel;
print(Almerinda);
Joao = Adoecido;
print(Joao);
