Homework 7:


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



Homework 12:


Project Description:
Title:Strategy Pattern
Strategy Design Pattern: Dynamic Fare Calculation

Overview:
This project demonstrates the use of the Strategy Design Pattern to calculate ride fares dynamically based on different pricing strategies. The pattern allows for flexibility and scalability by enabling the addition of new pricing strategies without modifying existing code.

Components:
Abstract Base Class (PricingStrategy):

Defines the interface for all pricing strategies.
Enforces the implementation of calculate_price in all derived classes.
Concrete Strategies:

RegularPricing: Implements standard fare calculation.
PremiumPricing: Implements premium fare calculation.
Context (Ride):

Represents a ride and uses a pricing strategy object to calculate the fare.
Delegates the fare calculation to the strategy passed during initialization.
Client:

Chooses the strategy dynamically (e.g., RegularPricing or PremiumPricing) and uses the Ride class to calculate fares.
Use Case:
Regular Pricing: Suitable for standard users.
Premium Pricing: Suitable for users requiring premium services.

Requirements Diagram:


+------------------------------------------+
|           <<requirement>>                |
|       Select Pricing Strategy            |
|------------------------------------------|
| The system shall allow selecting a       |
| pricing strategy for the ride.           |
+------------------------------------------+
                  |
    +-----------------------------------+-----------------------------+
    |                                                                 |
    v                                                                 v
+------------------------------------------+      +------------------------------------------+
|           <<requirement>>                |      |           <<requirement>>                |
|         Regular Pricing                  |      |         Premium Pricing                  |
|------------------------------------------|      |------------------------------------------|
| The system shall calculate fares using   |      | The system shall calculate fares using   |
| the regular pricing strategy.            |      | the premium pricing strategy.           |
+------------------------------------------+      +------------------------------------------+

+------------------------------------------+
|           <<requirement>>                |
|            Calculate Fare                |
|------------------------------------------|
| The system shall calculate the fare      |
| based on the selected pricing strategy   |
| and distance.                            |
+------------------------------------------+
                  |
    +-----------------------------------------+-------------------------+
    |                                                                   |
    v                                                                   v
+------------------------------------------+      +------------------------------------------+
|            <<activity>>                  |      |            <<activity>>                 |
|        Apply Pricing Strategy            |      |          Compute Fare                   |
|------------------------------------------|      |------------------------------------------|
| The system shall apply the selected      |      | The system shall compute the fare based |
| pricing strategy to calculate the fare.  |      | on the distance traveled.               |
+------------------------------------------+      +------------------------------------------+
link: https://drive.google.com/file/d/1r1CZZI8UCLMLRgr1Yo9jzgOUX_KzRswR/view?usp=sharing