# -*- coding: utf-8 -*-
"""Introdução a Recomendação

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BRL-xoWxHitEDjn2tU2-KHt3TDjhSalk
"""

import pandas as pd

filmes = pd.read_csv("movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]
filmes = filmes.set_index("filmeId")
filmes.head()

notas = pd.read_csv("ratings.csv")
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.head()

notas.describe()

"""# Primeira tentativa de recomendação"""

total_de_votos = notas["filmeId"].value_counts()
total_de_votos.head()

filmes['total_de_votos'] = total_de_votos
filmes.head()

filmes.sort_values("total_de_votos", ascending = False).head()

