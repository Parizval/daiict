from flask import Flask, render_template, request, redirect, url_for, session

#import mongo

app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "Nothing"


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def Login():
    return render_template('Login.html')


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.route("/sme")
def smeindex():
    return render_template('/sme/index.html')

@app.route("/sme/order")
def sme_order():
    return render_template('/sme/order.html')
@app.route("/ce")
def core():
    return render_template('/ce/index.html')


@app.route("/capital")
def capital():
    return render_template('/cap/index.html')


@app.route("/capital/market")
def capital_market():
    return render_template('/cap/marketplace.html')


@app.route("/capital/view/<order>")
def capital_view(order):
    print(order)
    return render_template('/cap/marketplace.html')


@app.route("/ce/create")
def CreateOrder():
    return render_template('/ce/createorder.html')


@app.route("/invoice")
def invoice():
    return render_template('/sme/invoice.html')
# Login and Sign Up Methods


@app.route('/login_action', methods=['POST'])
def login_action():

    email = request.form['email']
    password = request.form['password']
    print(email, password)
    if mongo.Login(email, password):
        return "Sucess"
    return "Error"


@app.route('/create_order', methods=['POST'])
def create_order():

    amount = request.form['Amount']
    quote = request.form['Quote']
    payment_date = request.form['Payment']
    delievery_date = request.form['Delievery']
    sme = request.form['SME']
#    print(sme,amount,quote,payment_date,delievery_date)

    return "Error"


@app.route('/sign_action', methods=['POST'])
def sign_action():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    category = request.form['category']

    print(name, email, password, category)
    if mongo.Register(email, name, password, category):
        return "Success"

    return "Error"


if __name__ == "__main__":
    app.run()
