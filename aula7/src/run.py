from fastapi import FastAPI, Response
from queue import Queue
import random
import logging
# api para um restaurante
# um endpoint que adiciona comidas (str) e grava numa lista
# um endpoint que adiciona um utilizador a uma fila (queue)
# endpoint que tira o primeiro da fila e atribui uma comida aleatoriamente e retorna um texto onde diz o que o cliente vai comer
api = FastAPI()

logging.basicConfig(level=logging.DEBUG)

ementa = list()
users = Queue()

@api.post("/menu", tags=["menu"])
async def add_food(name:str):
    logging.debug("ementa",ementa)
    ementa.append(name)
    logging.debug("ementa",ementa)
    return "added"

@api.get("/menu",  tags=["menu"])
async def list_menu():
    return ementa

@api.post("/user",tags=["user"])
async def add_user(name:str):
    logging.debug("fila",users.queue)
    users.put(name)
    logging.debug("fila", users.queue)

@api.get("/user", tags=["user"])
async def list_users():
    if users.empty():
        return []
    user_list = list(users.queue)
    return user_list

@api.get("/process")
async def process_order(response: Response):
    logging.debug("fila para processar", users.queue)
    if users.empty():
        logging.error("fila vazia")
        response.status_code = 450
        return response
    user = users.get()
    logging.debug("user", user)
    if not ementa:
        logging.warning("ementa vazia")
        response.status_code = 460
        return response
    food = random.choice(ementa)
    logging.debug("escolhida a comida", food)
    return f"{user} escolheu para comer o prato {food}"