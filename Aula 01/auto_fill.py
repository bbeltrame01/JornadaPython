import time
import pandas
import pyautogui

# Auto preenchimento de fomulários com PyAutoGUI

# pyautogui.click -> Clicar em um ponto específico da tela
# pyautogui write -> Escrever texto
# pyautogui.press -> Pressionar um tecla
# pyautogui.hotkey -> Pressionar uma combinação de teclas

pyautogui.PAUSE = 1 # Tempo de pausa entre os comandos

# Passo 1: Acessar o site - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('win', 'up')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3) # Esperar o site carregar

# Passo 2: Fazer login
pyautogui.press('tab')
pyautogui.write('teste@teste.com.br')
pyautogui.press('tab')
pyautogui.write('password@123')
pyautogui.press('enter')

# Passo 3: Importar base de dados
tabela = pandas.read_csv('produtos.csv')
campoInicial = (900, 250)

time.sleep(3)

# Passo 4: Cadastrar um produto e Repetir o passo 4 para mais produtos
for linha in range(len(tabela)):
  pyautogui.click(campoInicial[0], campoInicial[1])
  for coluna in range(len(tabela.columns)):
    if str(tabela.iloc[linha, coluna]) != 'nan':
      pyautogui.write(str(tabela.iloc[linha, coluna]))
    pyautogui.press('tab')
  pyautogui.press('enter')
  pyautogui.scroll(10000)
