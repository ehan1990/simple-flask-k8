import datetime
import logging
import mysql.connector
import os
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(filename)s:%(lineno)d %(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

VERSION = "1.1.0"

db_user = os.environ.get("DB_USER", "root")
db_pw = os.environ.get("DB_PW", "rootroot")
db = mysql.connector.connect(host="database-1.cghrm8nwvfeb.us-west-2.rds.amazonaws.com", user=db_user, password=db_pw,
                             database="wallstreet")


@app.route("/healthcheck", methods=["GET"])
def healthcheck_endpoint():
    db_connected = db.is_connected()
    data = {
        "msg": f"Running version {VERSION}",
        "date": f"{datetime.datetime.utcnow().isoformat()[0:19]}Z",
        "db": db_connected
    }
    return jsonify(data)


def main():
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)


if __name__ == "__main__":
    main()
