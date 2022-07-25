""" >>> incrementar:
o navegador é de teste porem nao tem conta
- add uma conta
- o que será assistido/pesquisado em cada streaming
"""

import PySimpleGUI as sg
from selenium import webdriver

# Layout
sg.theme('DarkPurple4')

layout = [
    # transforma todos os valores em minusculo
    [sg.Text('Streaming: '), sg.Input(key='streaming', size=(40,2))],
    [sg.Checkbox('Default profile: ')],
    [sg.Text('Watch: '), sg.Input(key='watch', size=(40,2))],
    [sg.Button('Clear'), sg.Button('Search')]
]

# janela

janela = sg.Window('O que vamos assistir?', layout, size=(340, 140))

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Search':
        # variaveis
        streaming = valores['streaming']
        watch = valores['watch']
        print(f"Streaming: {streaming} and watch: {watch}")

        # abrir o Chrome
        browser = webdriver.Chrome()

        # if hbo, netflix, youtube ou anime
        if streaming == 'hbo':
            browser.get('https://play.hbomax.com/page/urn:hbo:page:home')
            janela.close()
        if streaming == 'youtube':
            browser.get('https://www.youtube.com/')
            janela.close()
        if streaming == 'netflix':
            browser.get('https://www.netflix.com/browse')
            janela.close()
        if streaming == 'anime':
            browser.get('https://animesonline.cc/tv/')
            janela.close()
        break
