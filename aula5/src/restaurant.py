import random
# 4 clientes
# 10 menus, cada um com o seu preco
# cada cliente escolhe aleatoriamente entre 1 a 6 menus
# os clientes devem ser processados por ordem de chegada
# no fim, apresentar o total de cada cliente
# USAR CLASSES = opcional

def get_clients()->list:
    return [
        "Maria",
        "João",
        "Gonçalo",
        "Sandra"
    ]

def get_menu()->dict:
    return dict(
        bigmac=3.5,
        chicken_wings=3,
        sushi_combo=75.5,
        spicy_tacos=12.2,
        tuna_bowl=14.7,
        bacalhau=3.5,
        mista_carne=3,
        pato=75.5,
        burrito=12.2,
        paella=14.7
    )

def get_client_menu_choice(menu:dict)->dict:
    result = dict()
    nr_items:int = random.randint(1,6)
    while nr_items:
        item_index:str = random.choice(list(menu.keys()))
        result[item_index]=menu[item_index] 
        nr_items -=1
    return result


def start_program():
    clients: list = get_clients()
    menu: dict = get_menu()

    client_payments = dict()
    while clients:
        total = len(clients) - 1  # nr total de indices
        next_client:str = clients.pop(random.randint(0,total)) 
        client_menu:dict = get_client_menu_choice(menu=menu)
        client_payments[next_client] = sum(list(client_menu.values()))

    for client, payment in client_payments.items():
        print(f"client {client} have to pay {payment}")


if __name__ == '__main__':
    start_program()
