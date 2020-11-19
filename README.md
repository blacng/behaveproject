# Behavior driven development in Python using behave for test automation

## What is behavior driven development (BDD)?

Behavior Driven Development is an agile development methodology that encourages close collaboration between technical and non-technical teams --- including developers, quality assurance, security engineers, and business teams --- by allowing for rapid specification and testing of desired behaviors (i.e. features) in a system.

## What does it mean to do BDD?

1. Encouraging collaboration across roles to build shared understanding of the desired behavior of the system.
2. Producing system documentation that guides development and is automatically checked against system's behavior.
3. Working in rapid, small iterations to increase feedback and the flow of value. 

## 3 Essential Characteristics of BDD:

1. Take a small, upcoming change to the system like a _User Story_ and have a conversation to explore, discover, and agree on the details of how we want the system to behave using **_concrete_** examples. 
2. You document those examples in a way that can be automated and check for agreements.
3. You actually begin coding and implementing the behavior described by each documented example starting with an automated test to guide the development of the code. 

## BDD Project Lifecycle

1. Discovery
2. Formulation
3. Automation 

## Example of BDD

```gherkin
Feature: Ensure MySQL servers are in compliance with the Center for Information Security (CIS) security benchmark v1.1.0 (August 18 2016)

# This example has three steps
    Scenario: Run CIS MySQL Benchmarks
        Given MySQL servers are operational
        When we implement the required tests
        Then execute all required tests in the mysql server
        And verify tests have been implemented

    Rule: 1. Operating System Level Configuration
        1.1. Place Databases on Non-System Partitions
        1.2. Use Dedicated Least Privileged Account for MySQL Daemon/Service
        1.3. Disable MySQL Command History 
        1.4. Verify that the MySQL_PWD Environment Variables Is Not In Use
        1.5. Disabale Interactive Login 
        1.6. Verify that MySQL_PWD is not set in user's profiles
```