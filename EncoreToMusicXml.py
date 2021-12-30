import pyautogui as pag
from time import sleep
from os import listdir as ld

'''
Este script é  usado para converter arquivos Encore para arquivos MusicXML.'''
pag.press('win') # leva até o botão Windows
sleep(0.5)
pag.typewrite('encore') # escreve Encore
sleep(0.5)
pag.press('enter') # entra no Encore
arquivos = ld () # lista os arquivos
for a in arquivos: # para cada arquivo
    if '.enc' in a: # se for um arquivo Encore
        sleep(1)
        pag.hotkey('ctrl', 'o') # abre um arquivo Encore
        '''
        Necessita indicar o caminho da pasta onde estão os arquivos Encore.
        '''
        sleep(1)
        pag.write(a) # escreve o nome do arquivo Encore
        pag.hotkey('alt', 'a')
        sleep(0.5)
        pag.keyDown('alt') # converte o arquivo Encore para MusicXML
        pag.press('f')
        pag.keyUp('alt')
        pag.press('down', presses=7)
        pag.press('right')
        pag.press('down')
        pag.press('enter')
        sleep(0.5)
        pag.press('enter')
pag.hotkey('alt', 'f4') # fecha o Encore