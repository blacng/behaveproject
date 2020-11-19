Feature: Section Header 4.2 ensure test database is not installed
  
    As a cybersecurity analyst
    I want to ensure that the test
    database is not installed per CIS 1.1.0.

    Scenario Outline: Section Header: 4.2 Ensure the 'test' database is not installed on <host>
        Given a connection is made to <host>
        Then the database "test" is not installed

        Example: 
        |host        |
        |"localhost" |

Feature: Section Header: 4.4 ensure local_infile is disabled

    As a cybersecurity analyst,
    I want to ensure that certain
    variables are set to specific values.

    Scenario Outline: Section Header: 4.4 Ensure "local_infile" is disabled on <host>
        Given a connection is made to <host>
        Then variable "local_infile" is disabled

        Example: 
        |host        |db   |
        |"localhost" |mysql|


Feature: Section Header: 4.6 ensure symbolic links is disabled

    As a cybersecurity analyst,
    I want to ensure that certain 
    variables are set to specific values.

    Scenario Outline: Section Header: 4.6 Ensure 'symbolic links' is disabled on <host>
        Given a connection is made to <host>
        Then variable "have_symlink" is "DISABLED"

        Example: 
        |host        |db   |
        |"localhost" |mysql|
