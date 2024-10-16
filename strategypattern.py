from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, distance):
        pass

class RegularPricing(PricingStrategy):
    def calculate_price(self, distance):
        return distance * 1.0  # Basic rate

class PremiumPricing(PricingStrategy):
    def calculate_price(self, distance):
        return distance * 1.5  # Premium rate

class Ride:
    def __init__(self, pricing_strategy: PricingStrategy):
        self.pricing_strategy = pricing_strategy
    
    def calculate_fare(self, distance):
        return self.pricing_strategy.calculate_price(distance)

# Usage
ride1 = Ride(RegularPricing())
ride2 = Ride(PremiumPricing())

print(ride1.calculate_fare(10))  # Regular pricing for 10 km
print(ride2.calculate_fare(10))  # Premium pricing for 10 km
