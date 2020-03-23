import re
from flask import Flask, jsonify, abort, request
import exercise1and2 as ex1and2

# Exercise: 3
# Lav en flask server, hvor du åbner minimum 2 endpoints:
# - GET: returner data omkring antallet af crimes i en given periode
# (giv to datoer med som query-param i URL'en)
# - POST: returner den totale mængde af "burglaries" i januar, men returner kun data,
# hvis request.body indeholder et json objekt med key-value {"key": "secret"}

app = Flask(__name__)


@app.route('/holethrough/')
def index():
    return "Goodbye world"


@app.route('/crimes', methods=['GET'])
def getCrimes():
    try:
        startDay = request.args.get('startday')
        endDay = request.args.get('endday')
        isnumber = re.compile(r'^[0-9]*$')
        if(isnumber.match(startDay) and isnumber.match(endDay)):
            result = ex1and2.ex2(startDay, endDay)
            return jsonify(result)
        return jsonify({"msg": "Parameters must be numbers"}), 400
    except:
        return jsonify({"msg": "Uncaught error"}), 404


@app.route('/crimes', methods=['POST'])
def getBurglaries():
    if (request.json['key'] == 'secret'):
        result = ex1and2.ex2()
        return jsonify(result)
    return jsonify({'msg': 'Something went wrong'}), 404


if __name__ == '__main__':
    app.run(debug=True)
