from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

alunos_df = pd.DataFrame(columns=[ "nome", "nota"])

#estou usando baseModel por simplicidade e pq eu so sei desse jeito :)
class Aluno(BaseModel):
    nome : str
    nota : float

@app.post("/alunos")
def adicionar_aluno(aluno: Aluno):
    global alunos_df

    aluno_exists = alunos_df.index[alunos_df["nome"] == aluno.nome]

    if aluno_exists.empty:
        alunos_df = pd.concat([alunos_df, pd.DataFrame([aluno.dict()])],ignore_index=True)
        mensagem = "Aluno criado com sucesso."
    else:
        alunos_df.loc[aluno_exists, ["nome", "nota"]] = [aluno.nome, aluno.nota]
        mensagem = "Aluno atualizado com sucesso."

    return {"mensagem": mensagem, "aluno": aluno.dict()}

@app.get("/alunos/{nome}")
def pegar_nota_do_aluno_por_nome(nome : str):
    aluno_series = alunos_df["nome"] == nome
    aluno = alunos_df[aluno_series]

    if (aluno.empty):
        raise HTTPException(status_code=404, detail=f"Aluno com o nome:{nome}, não encontrado")

    nota = float(aluno.to_dict(orient="records")[0].get("nota"))

    # return aluno.to_dict(orient="records")[0]

    return {
        "nota" : nota
    }


@app.get("/alunos")
def listar_alunos():
    return alunos_df.to_dict(orient="records")
