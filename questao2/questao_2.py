import pandas as pd

arrecadado = pd.Series([12000, 17500, 14300, 16000, 19500], ["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Tom Hagen", "Michael Corleone"])

print("total arrecadado", arrecadado.sum())
print("media:", arrecadado.mean())
print("maia arrecadou:", arrecadado.idxmax())

#to fazendo o calclo da media de novo por preguiça mesmo
acima_da_media = arrecadado[arrecadado > arrecadado.mean() ]
print(acima_da_media)