
import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler('log_file.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Animal(ABC):
    
    @abstractmethod
    def speak(self):
        pass
    

class Cat(Animal):
    def speak(self):
        return ("КОШКА ДЕЛАЕТ МЯУ!!!")
    
class Dog(Animal):
    def speak(self):
        return ("СОБАЧКА ДЕЛАЕТ ГАВ!!!")

class Lion(Animal):
    def speak(self):
        return ("ЛЕВ ИСПОЛЬЗУЕТ Рыг!!!")
    

cat_speak = Cat()
dog_speak = Dog()
lion_speak = Lion()


if __name__ == "__main__":
    logger.info(cat_speak.speak())
    logger.info(dog_speak.speak())
    logger.info(lion_speak.speak())