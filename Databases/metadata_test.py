from sqlalchemy import schema, types


metadata = schema.MetaData()


model_table = schema.Table('page', metadata,
                           schema.Column('id', types.Integer, primary_key=True),
                           schema.Column('name', types.Unicode(255), default=u' '),
                           schema.Column('version', types.Unicode(255), default=u'New Version'),
                           schema.Column('description', types.Text, default=u' '),
                           )
for t in metadata.sorted_tables:
        print "Table name: ", t.name
        print "t is model_table: ", t is model_table

for column in model_table.columns:
        print "Column Table name: ", column.type

from sqlalchemy.engine import create_engine

engine = create_engine('sqlite:///:memory:' , echo=True)
metadata.bind = engine

metadata.create_all(checkfirst=True)
