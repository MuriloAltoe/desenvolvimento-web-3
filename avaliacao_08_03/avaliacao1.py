import pickle 
import csv
         
def extrair_chaves_dicionario(cidades):
    return list(cidades.keys())

def concatenar_listas(lista1, lista2):

     lista3 = lista1 + lista2
     return lista3

def quebrar_string_em_listas(string_maior, string_quebra):
    string_nova = string_maior.split(string_quebra)
    return string_nova

def gerar_lista_codigos(cidades = []):

    new_var = []
    for items in cidades:
        new_var.append(items.split(":")[0])

    return new_var

def gerar_lista_cidades(cidades):
    new_var = []
    for items in cidades:
        new_var.append(items.split(":")[1])

    return new_var

if __name__ == "__main__":
    with open('dados.bin', 'rb') as file:
        dados = pickle.load(file)

    estados = extrair_chaves_dicionario(dados)
    lista_codigos_cidades = []
    lista_cidades = []
    for estado in estados:
        lista1 = gerar_lista_cidades(dados[estado])
        lista2 = gerar_lista_codigos(dados[estado])
        lista_cidades = concatenar_listas(lista_cidades, lista1)
        lista_codigos_cidades = concatenar_listas(lista_codigos_cidades, lista2)

