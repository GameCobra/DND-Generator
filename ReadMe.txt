This is a program that will pull the data from the r/BehindTheTables and auto generate items and such.
I know this exists, but I want to auto generate a masive list of the items.
I have it being public so if anyone else wants to use this mostly usless tool then they can.

Well it looks like it dose will not accualy pull anything, instead I have a large list of tables (That I man)

How to:

Add tables:
1. Add your table to the Table Compendium with the following formating.
    a. Place a "%" at the begining of a line to denote that it is a header
    b. Place a "$" at the begining of a line to denote that it is a sub header
    c. The line imidietly affter a line break ("\n") denotes the name of a table
    d. All table names begin with "dx " where x is the number to role
    e. ALl table entries begin with "x. " where x is the number of that element ("x-y. " if you want a range, x is lower, y is higher)


Regenerate the tables
1. Remove the Tables.json file
2. Run the splitTableCompendium.py script