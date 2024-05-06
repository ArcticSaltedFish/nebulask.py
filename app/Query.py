from nebula3.gclient.net import ConnectionPool

from app.nebula.FormatResp import result_to_dict


def query(setence, connection_pool: ConnectionPool, user: str, passwd: str) -> dict:
    query_sentence = f"USE product_space;" f"SHOW TAGS;"
    with connection_pool.session_context(user, passwd) as session:
        query_result = session.execute(query_sentence)

    if not query_result.is_succeeded():
        ngql_msg = f"Something is wrong when query " f"{query}"
        return {"msg": ngql_msg}

    if query_result.is_empty():
        ngql_msg = f"There is nothing found by " f"{query}"
        return {"msg": ngql_msg}
    query_result = result_to_dict(query_result)
    return query_result
