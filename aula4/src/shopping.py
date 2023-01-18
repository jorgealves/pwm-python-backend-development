import random 
from collections import deque


products = {'bananas':0.8, 'apples':0.6, 'ketchup':1.2,'lemon':0.4,'potatoes':0.76}

# criar 3 pessoas
# attribuir 4 produtos a cada pessoa aleatoriamente
# colocar numa queue
# fazer print do total

def start():

    clients = [
        'John',
        'Joe',
        'Amy'
    ]

    shopping_mall = deque()
    for client in clients:
        total = 0
        for _ in range(1,3):
            total+=random.choice(list(products.values()))
        shopping_mall.append((client,total))
        print(f"Client {client} will pay {total}")
    
    for _ in range(1,3):
        print(shopping_mall.popleft())

    print(clients)

if __name__ == '__main__':
    start()