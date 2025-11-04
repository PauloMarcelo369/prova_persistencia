with open("dados_alunos.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

alunos = []
notas = []

for linha in linhas:

    nome, curso, nota = linha.split("#")
    nota = float(nota)

    alunos.append({"nome": nome, "curso": curso, "nota": nota})
    notas.append(nota)


media = sum(notas) / len(notas)
maior_nota = max(alunos, key=lambda a: a["nota"])
menor_nota = min(alunos, key=lambda a: a["nota"])

print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior_nota['nota']} ({maior_nota['nome']})")
print(f"Menor nota: {menor_nota['nota']} ({menor_nota['nome']})")