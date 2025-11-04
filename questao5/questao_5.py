from bs4 import BeautifulSoup

with open("jogadas.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")


table = soup.find("table", {"id" : "jogadas"})

# print(table)

rows = table.find_all("tr")

jogador_1_contador = 0

for row in rows:
    tds = row.find_all("td")
    if (tds != []):
        jogada1 = tds[0].string
        jogada2 = tds[1].string

        if (jogada1 == "pedra" and jogada2 == "tesoura"):
            jogador_1_contador += 1
        elif(jogada1 == "papel" and jogada2 == "pedra"):
            jogador_1_contador += 1
        elif(jogada1 == "tesoura" and jogada2 == "papel"):
            jogador_1_contador += 1


print ("quantidade de vezes que o jogador 1 venceu:", jogador_1_contador)