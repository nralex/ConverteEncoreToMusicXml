# 🎹🎻 Converter Encore para MusicXml 🎷🎺

Programa para automatizar o processo de conversão de arquivos .enc em MusicXml.

---

# ❗ Atenção

Este é um projeto que visa meramente colocar em pratica conceitos da linguagem python, sou curioso e estou aprendendo ainda, é possível que o programa não funcione bem na sua maquina.

---

## ⚙ Etapas da automação

* Localiza o diretório onde o executável está;
* Abre o Encore usando o botão Windows;
* Lista cada um dos arquivos presentes no diretório;
* Abre os arquivos, caso sejam do tipo .enc;
* Usa o Encore para converter em Xml;
* Fecha o arquivo e passa para o próximo;
* Ao final do processo fecha o Encore.

---

## 🛑 Importante

É necessário ter o Encore instalado na sua máquina. E por conta do uso da extensão [pyautogui](https://pyautogui.readthedocs.io/en/latest/index.html) não é possível usar a maquina durante a execução do programa. A não obediência a este aviso pode levar a resultados indesejados.

---

## ⚙ Uso

Faça o [DOWNLOAD](https://github.com/nralex/EncoreToMusicXml/blob/main/dist/EncoreToMusicXml.exe) do executável (SOMENTE WINDOWS), cole na pasta onde estão os arquivos .enc e execute a aplicação.
Dependendo da quantidade de arquivos é possível que o processo demore bastante, cada arquivo leva em média 4,5 segundos para passar por todo o processo de automação.

---

## 🛑 Observações

A exportação feita pelo encore não é perfeita e costuma perder elementos como letra e cifra. Por vezes, dependendo da origem do arquivo convertido também é possível que apareçam caracteres duplicados ou até compassos com caracteres a mais do que o desejado.
