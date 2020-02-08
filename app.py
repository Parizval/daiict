from flask import Flask, render_template, request, redirect, url_for, session
import utils
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



@app.route("/sme/decision")
def sme_decision():
    return render_template('/sme/order.html')


@app.route('/sme/approve', methods=['POST'])
def sme_approve():
    hash_number = request.form['HashCode']
    workingcapital = request.form['WorkingCapital']
    captialdeadline = request.form['CapitalDeadline']
    print(workingcapital, captialdeadline,hash_number)
    return "Error"

@app.route('/sme/reject', methods=['POST'])
def sme_reject():

    hash_number = request.form['HashCode']
    print(hash_number)
    return "Error"



@app.route("/ce")
def core():
    return render_template('/ce/index.html')


@app.route("/ce/decision")
def ce_decision():
    temp = utils.db.get_data('orders')
    data = {}
    for i in temp:
        if temp[i]['approved'] == 'no' and 'invested' not in temp[i]:
            data[i] = temp[i]
    if 'decision' in request.args:
        decision = request.args.get('decision')
        uid = request.args.get('hash')
        if decision == 'y':
            intd = request.args.get('intd')
            utils.update_order(uid, intd)

        else:
            utils.update_order(uid, False)
        return redirect('/ce/decision')
    else:
        return render_template('/ce/approve_order.html', data=data)


@app.route("/capital")
def capital():
    return render_template('/cap/index.html')


@app.route("/capital/market")
def capital_market():
    temp = utils.db.get_data('orders')
    data = {}
    for i in temp:
        if temp[i]['approved'] == 'yes' and 'invested' not in temp[i]:
            data[i] = temp[i]
    print(data)
    return render_template('/cap/marketplace.html', data=data)


@app.route("/capital/view/<order>")
def capital_view(order):
    data = temp = utils.db.get_data('orders/'+order)
    print(data)
    return render_template('/cap/vieworder.html', data=data, graph_data=utils.make_line_graph())


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
    uid = utils.make_order(quote, amount, payment_date, delievery_date, sme)
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
