from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    print(source_currency)
    print(amount)
    print(target_currency)

    cf = fetch_conversion(source_currency,target_currency)
    final_amount = amount*cf
    final_amount = round(final_amount,2)

    ans = {
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }

    return jsonify(ans)

def fetch_conversion(source,target):
    url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=c74c39465ef356144faf".format(source,target)

    response = requests.get(url)
    response = response.json()
    print(response)

    return response['{}_{}'.format(source,target)]
if __name__ == '__main__':
    app.run(debug=True)