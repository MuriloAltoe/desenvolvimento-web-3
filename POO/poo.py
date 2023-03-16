def quebra_string(str_maior, str_quebra):
    return str_maior.split(str_quebra)

# def soma_tudo(a1,a2):
#     return a1+a2

# print(soma_tudo(10,30))

def soma_tudo(*numeros):
    print(numeros)
    soma = 0
    for n in numeros:
        if(type(n) == type(1)):
            soma = soma + n
    print(soma)

soma_tudo(10,65,30,[])

# print(quebra_string(input("digite o array"), ";"))


def mostra_parametro(**kwargs):
    print(kwargs)

mostra_parametro(par1="oi", par2="mundo", teste="teste")

class PrimeiraClasse:
    pass

obj1 = PrimeiraClasse()

class SegundaClasse:
    def imprime_1(self, parametro1):
        print(parametro1)

obj2 = SegundaClasse()

isinstance(obj1, PrimeiraClasse)

obj2.imprime_1("banana")

obj1.nome = "nomezinho"

print(obj1.__dict__)

SegundaClasse.imprime_1(SegundaClasse, "oi")

# Criando uma nova virtual machine

# virtualenv -p 'nomedavenv' = cria nova venv
# source nomedavenv/bin/activte = entra na nova venv

# pip freeze = escreve as dependencias
# pip freeze > requirements.txt = salva as dependencias em um txt

# pip install -r requirements.txt = instala todas as dependecias salvas no requeriments.txt