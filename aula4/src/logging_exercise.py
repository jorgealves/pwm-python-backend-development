import logging

logging.basicConfig(filename="logging.log", level=logging.DEBUG)

def ask_question(question:str, output_response_type:callable):
    logging.info("asking question...")
    response: str = input(question)
    logging.debug(f"got {response}")
    if output_response_type == bool:
        response = True if response=='yes' else False
    return output_response_type(response)

def build_response(name,age,email,like_programming):
    like = "I Love Programming" if like_programming else "I Don't like Programming"
    return f"Hi! I'm {name}, I'm {age}y. You can email me to {email} and {like}"


def start():
    questions = [
        ("What's your name?", str),  # Tuple 
        ("How old are you?", int),
        ("What's your email?", str),
        ("Do you like Programing?",bool)
    ] 
    responses = []  
    for question, output_response_type in questions:
        try:
            responses.append(ask_question(question,output_response_type))
            logging.info("response added to array")
        except ValueError as err:
            logging.error(err)
            print("error. Program terminated")
            return
    
    logging.debug(responses)
    print(build_response(responses[0],responses[1],responses[2],responses[3]))


if __name__ == '__main__':
    start()