### An SQLAlchemy layout tutorial
#### This doc uses the file [customers_db.py] as a reference
The first step in writing SQL Alchemy code is opening a connection to the database you are gonna be using. This is done by creating an SQL Engine object, which knows how to talk to a particular type of database.

``` db = create_engine('sqlite', opts={'filename': 'customers.db'}) ```

The Engine object also doubles as a connection object, creating a pool of database connections and reusing them automatically as needed. *NOTE* Most of the time you don't even need to think about the db connections, just use the SQLEngine object that **create_engine()** returns.

SQLAlchemy has tried as much as possible to redirect users from writing raw SQL thus calling the **execute()** method allows one to execute queries as desired. The **INSERT** statement enables one to manipulate a specific table-space with reference, i.e:

```i = users.insert() ```

When an ```i.execute() ``` is run, SQLAlchemy will generate the appropriate *INSERT INTO users VALUES (...)* statement for the values we pass into execute().
NOTE: One can also pass parameters to execute() as 'what should be inserted to specified tablename'
