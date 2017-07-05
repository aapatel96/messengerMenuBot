import flask
import os
import time

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def moulton():
    x = {'menu': None}
    currenttime= int(time.ctime()[11:19][0:2]) -3
    if currenttime>= 5 and currenttime < 10:
        if moultonBreakfast == '':
            x['menu'] == 'No menus available'
            return jsonify(results=x)
        x['menu'] == moultonBreakfast
        return jsonify(results=x)
    elif currenttime>= 10 and currenttime < 14:
        if moultonLunch == '':
            x['menu'] == 'No menus available'
            return jsonify(results=x)
        x['menu'] == moultonLunch
        return jsonify(results=x)
    else:
        if moultonDinner == '':
            x['menu'] == 'No menus available'
            return jsonify(results=x)

        x['menu'] == moultonDinner
        return jsonify(results=x)



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', '5000'))

    app.run(
        host="0.0.0.0",
        port=PORT
    )
