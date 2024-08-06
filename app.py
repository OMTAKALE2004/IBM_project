from flask import Flask, request, render_template, redirect, url_for, flash
import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY=os.getenv('API_KEY')

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnosis.html')
def home1():
    return render_template('diagnosis.html')

@app.route('/diabetes.html',methods=["GET"])
def home2():
    return render_template('diabetes.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        f1 = request.form['pregnant']
        f2 = request.form['glucose']
        f3 = request.form['bp']
        f4 = request.form['skt']
        f5 = request.form['ins']
        f6 = request.form['bmi']
        f7 = request.form['dvp']
        f8 = request.form['Age']
    except KeyError as e:
        return f"Missing form key: {str(e)}", 400
    except ValueError as e:
        return f"Invalid input: {str(e)}", 400

    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]


    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    
    # Prepare the payload for scoring
    payload_scoring = {
        "input_data": [{
            "field":  ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'],
            "values": [[0, f2, f3, f4, f5, f6, f7, f8]]
        }]
    }

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/544c1e5f-d9da-43e3-ac00-d75aab80526e/predictions?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    # print("Scoring response")
    # print(response_scoring.json())
    prediction=response_scoring.json()
    # print(prediction)
    error=prediction['trace']
    # print(f"erro{error}")
    
    if 'predictions' in prediction:
        print(prediction['predictions'])
        percent = round(prediction['predictions'][0]['values'][0][1][1] * 100, 2)
        prediction=int(prediction['predictions'][0]['values'][0][0])
        # print(percent,prediction)
        # prediction=[prediction,percent]
        # print(prediction[0])
        return redirect(url_for('result', prediction=prediction,percent=percent))
    else:
        return redirect(url_for('result', prediction='-1'))

@app.route('/result')
def result():
    prediction = request.args.get('prediction')
    percent=request.args.get('percent')
    # print(f"result:/n {prediction},{percent}")
    return render_template('result.html', prediction=prediction,percent=percent)

@app.route('/heart.html',methods=["GET"])
def home3():
    return render_template('heart.html')

@app.route("/predictt",methods=["POST"])
def predictt():
    try:
    
        f1 = request.form['Gender']
        f2 = request.form['Age']
        f3 = request.form['cpt']
        f4 = request.form['rbp']
        f5 = request.form['chl']
        f6 = request.form['fbs']
        f7 = request.form['recg']
        f8 = request.form['mhr']
        f9 = request.form['exang']
        f10 = request.form['op']
        f11 = request.form['stslope']
        
    except KeyError as e:
        return f"Missing form key: {str(e)}", 400
    except ValueError as e:
        return f"Invalid input: {str(e)}", 400
    
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    payload_scoring = {
        "input_data": [{
            "field":  ['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope'],
            "values": [[f2,f1,f3,f4,f5,f6,f7,f8,f9,f10,f11]]
        }]
    }
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/4e754c34-054e-4355-b40c-7f3df0cb64df/predictions?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    prediction=response_scoring.json()
 
    if 'predictions' in prediction:
        percent = round(prediction['predictions'][0]['values'][0][1][1] * 100, 2)
        prediction=int(prediction['predictions'][0]['values'][0][0])
       
        return redirect(url_for('resultheart', prediction=prediction,percent=percent))
    
    else:
        return  redirect(url_for('resultheart', prediction='-1'))
  
@app.route('/resultheart')
def resultheart():
    prediction = request.args.get('prediction')
    percent = request.args.get('percent')
    return render_template('resultheart.html', prediction=prediction,percent=percent)

@app.route('/consultdiabetes.html')
def consult():
    return render_template('consultdiabetes.html')

@app.route('/consultheart.html')
def consult1():
    return render_template('consultheart.html')



# if __name__ == '__main__':
#     app.run(debug=True)

