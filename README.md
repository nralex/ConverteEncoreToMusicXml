---
marp: true
---
# Converter Encore para MusicXml

Repositório da minha tentativa de automatizar a conversão de arquivos encore par MusicXml

---

## Etapas

* Localiza o diretório onde o executável está;
* Abre o Encore usando o botão Windows;
* Lista cada um dos arquivos presentes no diretório;
* Abre os arquivos, caso sejam do tipo .enc;
* Usa o Encore para converter em Xml;
* Fecha o arquivo e passa para o próximo;
* Ao final do processo fecha o Encore.

---

## Importante

É necessário ter o Encore instalado na sua máquina. E por conta do uso da extensão [pyautogui](https://pyautogui.readthedocs.io/en/latest/index.html) não é possível usar a maquina durante a execução do programa.