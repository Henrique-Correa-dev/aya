#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ =  "Henrique Correa"
__license__ = "Privado - distribuição não autorizada sem a licença dos autores"
__version__ = "0.0.1"

"""
AYA - Smart Interface
A smart interface    

Controle de Versão
    21/10/2021 - 0.0.1 - 
    Versao funcional 0.0.1 validado em 21/10/2021

 TO-DO:
    - Voz para nossa querida Aya  -

PAREI NO -->
  Data de entrada em funcionamento: xx/xx/xxxx (versao x.x.x)

Escrito para Python 3.7.3 ou posterior (incluindo bibliotecas externas)
"""

import pyttsx3

# Configurações de Voz
engine = pyttsx3.init()
engine.say("Hello World")

engine.runAndWait()