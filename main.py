from flask import Flask, request, jsonify, json
import flask

# import gaia_models_sarima as models
# import gaia_models_single as models
# import gaia_models_cnnlstm as models
# import gaia_models_xgb as models
# import gaia_models_br as models
# import gaia_models_holt as models
# import gaia_models_rf as models
import gaia_models_naive as models

from dateutil import parser
import statsmodels
import pandas as pd

app = Flask(__name__)

debug = False

@app.route("/gg",methods=["POST"])
def happen():
    d = request.get_json(force=True)
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    question = d['data'].get('question', {})
    truth = d['data'].get('truth', {})
    if question != {}:
        print('I got a question!!!')
        return jsonify({"result": on_question(question)})
    elif truth != {}:
        print('I got a truth!!!')
        on_truth(truth)
        return jsonify({"result": {}})
    else:
        print('what is going on???')
        return jsonify({"result": d['data'].get('question', {})})

def on_question(question):
    prediction = models.on_question(question)
    return prediction
    
def on_truth(truth):
    contestID = truth["responderInfo"]["contestID"]
    value = truth['units'][0]['value']
    str_time = truth['units'][0]['predictionTime']
    if str_time[-1] == 'Z':
        str_time = str_time[:-1]
    truth_time = parser.parse(str_time)
    models.on_truth(truth_time, value, contestID)

port = 8080
if __name__=="__main__":
    print("running on %d" % port)
    # app.run(host="0.0.0.0", port=port, debug=False)
    app.run(host="0.0.0.0", port=port, debug=False)
