from app.nebula.ConfDB import parse_nebula_graphd_endpoint
from app import nebula
from flask_restful import Api
import os
from flask import Flask, jsonify
from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config


app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.route("/query", methods=["GET"])
def send():
    answer = nebulaer._query("1")
    print(answer)

    return jsonify(answer), 200


"""
--------------------------------------------
START FLASK_REST_API
START NEBULA CLIENT
--------------------------------------------
"""

USER_NAME = f"admin_product"
PASSWD = f"nebula"


# init flask api
api = Api(app)
api = Api(app, catch_all_404s=False)

# config ng_client
ng_config = Config()
ng_config.max_connection_pool_size = int(
    os.environ.get("NG_MAX_CONN_POOL_SIZE", 10))
ng_endpoints = parse_nebula_graphd_endpoint()
connection_pool = ConnectionPool()
connection_pool.init(ng_endpoints, ng_config)

# main func entry
if __name__ == "__main__":
    nebulaer = nebula.NebulaQuery(connection_pool, USER_NAME, PASSWD)
    try:
        app.run(
            port=5000,
            host="127.0.0.1",
            debug=True,
            threaded=True,
        )

    except Exception as x:
        import traceback
        print(traceback.format_exc())

    finally:
        connection_pool.close()
else:
    nebulaer = nebula.NebulaQuery(connection_pool, USER_NAME, PASSWD)
