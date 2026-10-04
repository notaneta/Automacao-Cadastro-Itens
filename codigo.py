# Primeira coisa a se fazer antes de começar, Exemplificar oque tem que fazer manualmente para depois automatizar

# Abrir sistema da empresa
# Fazer login
# Abrir base de dados
# Cadastrar produto
# Repetir passo 4 até acabar produtos

import pyautogui
import time


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#  Abrir sistema da empresa
 # Abrir navegador
 # Entrar no site
pyautogui.PAUSE = 0.5 # Config do tempo necessário para executar comandos

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")


# Fazer login
    # Colocar email e senha

pyautogui.write(link)
pyautogui.press("enter")
# Pausa para site carregar
time.sleep(5)
# Cordenadas x, y para clicar no campo de login
pyautogui.click(x=1552, y=551)  # Cordenadas variaveis de acordo com o a tela do pc do usuário, use o arquivo util para poder localizar 
pyautogui.write("login@login.com") # Email
pyautogui.press("tab") 
pyautogui.write("Abc123") # Senha
pyautogui.press("tab")
pyautogui.press("enter") # Confirma o botão Logar 
time.sleep(5) # Pausa para carregar

# Abrir base de dados
# pip install pandas openpyxl (para base de dados em excel)
import pandas

tabela = pandas.read_csv("produtos.csv")  # Faz a leitura do arquvido pelo pandas, e importa para a variavel tabela 
print(tabela)

# Cadastrar produto
    # Produto
    # Marca
    # Tipo
    # Categoria
    # Preço
    # Custo
    # OBS

for linha in tabela.index:
    # clicar no primeiro campo da tela
    pyautogui.click(x=1654, y=367)
    
    # pegar da tabela e preencher o campo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    pyautogui.press("enter") # cadastra o produto (botao enviar)

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

