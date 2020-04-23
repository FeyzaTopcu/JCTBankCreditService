import pickle
from flask import Flask, request, jsonify, render_template

class predictionDefault:
    def __init__(self,result):
        self.result = result;
    
    def serialie(self):
        return {'Sonuc': self.result}

app = Flask(__name__)
Model = pickle.load(open('Model.pkl','rb'))
@app.route('/')
def index():

    return render_template('CreditInfo.html') 

@app.route('/result', methods=['GET', 'POST'])
def creditPrediction():
    if(request.data != None):
        data = request.get_json()
        LoanAmount = data['LoanAmount']
        Age = data['Age']
        HasHouse = data['HasHouse']
        CreditCount = data['UsedCredits']
        HasPhone = data['HasPhone']
        
        predict = Model.predict([[float(LoanAmount),
                                    float(Age),
                                    float(HasHouse),
                                    float(CreditCount),
                                    float(HasPhone),]])
        creditResult = predict[0]
        if(creditResult>=1):
            creditState = "Kredi verilebilir."
            creditResult = 1
        else:
            creditState = "Kredi verilemez."
            creditResult = 0
        
        return jsonify({"Error":None, "Data":{"Message":creditState,"Success":creditResult}})
    else:
        return jsonify({"Error":"Bir hata meydana geldi.", "Data":None})

if __name__ == '__main__':
    try:
        app.run(debug=False)
        print("Sunucu aktif!")
    except:
        print("Sunucu hatası!")