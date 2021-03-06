### An SQLAlchemy layout tutorial

#### This doc uses the file [customers_db.py](https://github.com/andela-jmuli/learning-python/blob/master/Databases/customers_db.py)  and [engine_test]() as a reference

The first step in writing SQL Alchemy code is opening a connection to the database you are gonna be using. This is done by creating an SQL Engine object, which knows how to talk to a particular type of database.

``` db = create_engine('sqlite', opts={'filename': 'customers.db'}) ```

The Engine object also doubles as a connection object, creating a pool of database connections and reusing them automatically as needed. *NOTE* Most of the time you don't even need to think about the db connections, just use the SQLEngine object that **create_engine()** returns.

In engine_test, note that ``` echo = True ``` is passed,  this tells the engine object to log all the SQL it executed to ``` sys.stdout ```.
``` connection ``` is a SQLAlchemy Connection object. ``` result ``` is a SQLAlchemy ``` ResultProxy``` object that allows you to iterate over the results of the statement you executed.

SQLAlchemy has tried as much as possible to redirect users from writing raw SQL thus calling the **execute()** method allows one to execute queries as desired. The **INSERT** statement enables one to manipulate a specific table-space with reference, i.e:

```i = users.insert() ```

When an ```i.execute() ``` is run, SQLAlchemy will generate the appropriate *INSERT INTO users VALUES (...)* statement for the values we pass into execute().
NOTE: One can also pass parameters to execute() as 'what should be inserted to specified tablename'

### Metadata and Type APIs

The metadata and type systems describe the db schema in an RDBMS-independent manner.
A metadata obj holds all the information about the tables, columns, types, foreign keys, indexes and sequences that make up a db structure.
The metadata obj can be used to create database tables, to do this bind the ``` metadata ``` to an engine and call its ``` create_all ``` method.


### Declarative_base()

SQLAlchemy object-relational config involves the combination of Table, mapper() and class objects to define a mapped class. *declerative* allows all three to be expressed at once within the class declaration.
