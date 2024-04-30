
import time
import json

from nebula3.gclient.net import ConnectionPool

from nebula3.Config import Config
from nebula3.common import *
from FormatResp import print_resp

if __name__ == '__main__':
    client = None
    try:
        config = Config()
        config.max_connection_pool_size = 2
        # init connection pool
        connection_pool = ConnectionPool()
        assert connection_pool.init([('127.0.0.1', 9669)], config)

        # get session from the pool
        client = connection_pool.get_session('root', 'nebula')
        assert client is not None

        # get the result in json format
        resp_json = client.execute_json("yield 1")
        json_obj = json.loads(resp_json)
        #print(json.dumps(json_obj, indent=2, sort_keys=True))

        resp=client.execute(
            'USE product_space;CREATE TAG INDEX `atom_func_class` ON \
                `atom_func` ( `class`(99));CREATE TAG INDEX `atom_func_name` ON \
                    `atom_func` ( `name`(99));CREATE TAG INDEX `req_name` ON \
                        `req` ( `name`(99));'
        )
        assert resp.is_succeeded(), resp.error_msg()
        # for a in resp:
        #     print(a)
        #     delete_query = f"DELETE VERTEX {a}"
        #     resp=client.execute(delete_query)
        # assert resp.is_succeeded(), resp.error_msg()




    except Exception as x:
        import traceback

        print(traceback.format_exc())
        if client is not None:
            client.release()
        exit(1)