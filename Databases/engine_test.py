from sqlalchemy.engine import create_engine


engine = create_engine('sqlite:///:memory:', echo=True)
connection = engine.connect()
connection.execute()
result = connection.execute("SELECT username FROM users")
for row in result:
        print "username: ", row['username']
connection.close()
