import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
Model = pickle.load(open('Model.pkl','rb'))

@app.route('/')
def index():
    return render_template('CreditInfo.html') 

@app.route('/result', methods=['GET', 'POST'])
def creditPrediction():
    if request.method == 'POST':
        LoanAmount = request.form['loanAmount']
        Age = request.form['age']
        HasHouse = request.form['home']
        CreditCount = request.form['creditCount']
        HasPhone = request.form['phone']
         
        predict = Model.predict([[float(LoanAmount),
                                    float(Age),
                                    float(HasHouse),
                                    float(CreditCount),
                                    float(HasPhone),]])
        creditResult = predict[0]
        if(creditResult>=1):
            creditState = "Kredi verilebilir."
        else:
            creditState = "Kredi verilemez."
        
        return render_template("result.html",creditState = creditState)
    else:
        return render_template('CreditInfo.html')

if __name__ == '__main__':
    try:
        app.run(debug=False)
        print("Sunucu aktif!")
    except:
        print("Sunucu hatası!")