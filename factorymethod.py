from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass

class Rider(User):
    def get_role(self):
        return "I am a Rider"

class Driver(User):
    def get_role(self):
        return "I am a Driver"

class UserFactory:
    @staticmethod
    def create_user(user_type):
        if user_type == 'Rider':
            return Rider()
        elif user_type == 'Driver':
            return Driver()

# Usage
rider = UserFactory.create_user('Rider')
driver = UserFactory.create_user('Driver')
print(rider.get_role())  # Output: I am a Rider
print(driver.get_role())  # Output: I am a Driver
