from fastapi import FastAPI


api = FastAPI()

turma = [
        "Alexandre",
        "Artur",
        "David",
        "Inna",
        "Jamie",
        "Tomás"
    ]

@api.get("/")
async def hello():
    return "Hello a todos"


@api.post("/")
async def hello2():
    return "Hello aasdasd todos2"


@api.get("/turma")
def get_turma():
    return turma

@api.post("/turma")
def add_new_to_turma(name:str):
    turma.append(name)

@api.get("/{name}")
def get_name(name:int):
    return name