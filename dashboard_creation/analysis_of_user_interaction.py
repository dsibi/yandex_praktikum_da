import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(connection_string)

query = '''
            SELECT * FROM dash_visits
        '''

dash_visits=pd.io.sql.read_sql(query, con = engine)

dash_visits.to_csv('dash_visits.csv')