from nebula3.gclient.net import ConnectionPool

# def nebula_session_init(connection_pool:ConnectionPool ):
#     with connection_pool.session_context('root', 'nebula') as session:
#         session.execute('USE product_space')
#         return  session
from app.Query import query


class NebulaQuery:
    def __init__(self, connection_pool: ConnectionPool, user: str, passwd: str) -> None:
        self.connection_pool = connection_pool
        self.user = user
        self.passwd = passwd

    def _query(self, sentence):
        result = query(sentence, self.connection_pool, self.user, self.passwd)
        return result
