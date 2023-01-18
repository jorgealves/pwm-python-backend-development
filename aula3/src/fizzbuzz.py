# se n for divisivel por 3, escrevem 'fizz' 
# se n for divisivel por 5, escrevem 'buzz' 
# se n for divisivel por 3 e por 5, escrevem 'fizzbuzz' 
import logging

logging.basicConfig(format= "%(asctime)s || %(levelname)s || %(msg)s", filename="fizzbuzz.log", level=logging.DEBUG)

def is_divisible(number,division):
    return number % division == 0
        

def fizzbuzz(number:int)->str:
    try:
        logging.warning(f"number is {number}")
        if is_divisible(number,3) and is_divisible(number,5):
            return "FizzBuzz"
        if is_divisible(number,3):
            return "Fizz"
        if is_divisible(number,5):
            return "Buzz"
   
        return str(number)
    except Exception as e:
        logging.error("big mistake", exc_info=e)
        

logging.info("Program is starting...")
print(fizzbuzz("asdasd"))
logging.info("Program is finished")