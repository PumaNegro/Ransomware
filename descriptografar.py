from cryptography.fernet import Fernet
import os

def Carregar_chave():
    with open("chave.key", "rb") as file:
        return file.read()

def descriptografar_arquivo(arquivo,chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()

        dados_descriptografados = f.decrypt(dados)

        nome_saida = arquivo + ".restaurado"

    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
    
                 lista.append(caminho)

    return lista

def main():
    chave = Carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
        print("Arquivos restaurados com sucesso!")

if __name__ == "__main__":
    main()