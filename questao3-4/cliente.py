import httpx

BASE_URL = "http://127.0.0.1:8000"

def criar_aluno(aluno):
    resp = httpx.post(
        f"{BASE_URL}/alunos", 
        json = {"nome" : aluno.get("nome"), "nota" : aluno.get("nota")})
    return resp.json()


def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/alunos")
    print(resp.json())

def pegar_nota_por_nome(nome):
    resp = httpx.get(f"{BASE_URL}/alunos/{nome}")
    print(resp.json())

print(criar_aluno({"nome" : "marcelo", "nota" : 9.4}))
pegar_nota_por_nome("marcelo")

listar_alunos()