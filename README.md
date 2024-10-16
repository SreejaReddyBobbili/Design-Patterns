# Design-Patterns

Design Patterns Implementation: Factory Method & Strategy
Project Overview
This project demonstrates the implementation of two common design patterns:

Factory Method Pattern: A creational pattern used to define an interface for creating objects, but allowing subclasses to alter the type of objects that will be created.
Strategy Pattern: A behavioral pattern that enables selecting algorithms at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable.
The project is implemented in python.


Design Patterns:
1. Factory Method
The Factory Method design pattern defines a method in a superclass that returns an object of a class. Subclasses implement the factory method to create different types of objects based on specific conditions.

Product: The common interface for objects created by the factory method.
ConcreteProductA and ConcreteProductB: Concrete implementations of the product interface.
Creator: An abstract class that declares the factory method.
ConcreteCreatorA and ConcreteCreatorB: Subclasses of the creator that implement the factory method to return objects of ConcreteProductA and ConcreteProductB.
2. Strategy
The Strategy pattern allows different algorithms to be defined and swapped at runtime. The context class uses a strategy interface, allowing different strategy algorithms to be injected and executed.

Context: Maintains a reference to a Strategy object.
Strategy: Defines an interface for the algorithm.
ConcreteStrategyA and ConcreteStrategyB: Implementations of different algorithms that conform to the Strategy interface.

class Diagrams:

a.Factory Method 

+-------------------+
|       User        |
|-------------------|
| + get_role()      |
+-------------------+
        ^
        |
        |-------------------+
        |                   |
+-----------------+  +-----------------+
|      Rider      |  |     Driver      |
|-----------------|  |-----------------|
| + get_role()    |  | + get_role()    |
+-----------------+  +-----------------+

+-----------------------+
|      UserFactory      |
|-----------------------|
| + create_user(user_type): User |
+-----------------------+


link : https://drive.google.com/file/d/19sEFPNcXHRweQrmLannwFHNjTl2jxS2y/view?usp=sharing


b.Strategy Pattern:


+-------------------------+
|     PricingStrategy     |
|-------------------------|
| + calculate_price(distance) |
+-------------------------+
          ^
          |
          |-------------------+
          |                   |
+--------------------+ +--------------------+
|   RegularPricing   | |   PremiumPricing   |
|--------------------| |--------------------|
| + calculate_price(distance) | + calculate_price(distance) |
+--------------------+ +--------------------+

+--------------------+
|       Ride         |
|--------------------|
| - pricing_strategy: PricingStrategy |
| + __init__(pricing_strategy: PricingStrategy) |
| + calculate_fare(distance)   |
+--------------------+


link: https://drive.google.com/file/d/1ZVy4lPOKjtQulSNgUDukThTnQ_Pc7ItA/view?usp=sharing
