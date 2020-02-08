from database import Database
import hashlib
import pygal
import time

db = Database()


def make_sme(name, address, ce):
    db.write_data('sme', {
        'name': name,
        'ce': ce,
        'address': address
    })


def update_sme(name, ce):
    hash_object = hashlib.sha1(name.encode())
    hex_dig = hash_object.hexdigest()
    old_data = db.get_data('sme/{}'.format(hex_dig[-15:]))
    db.write_data('sme', {
        'name': name,
        'ce': ce,
        'address': old_data['address']
    })


def make_ce(name, address, sme):
    db.write_data('enterprises', {
        'name': name,
        'sme': sme,
        'address': address
    })


def update_ce(name, sme):
    hash_object = hashlib.sha1(name.encode())
    hex_dig = hash_object.hexdigest()
    old_data = db.get_data('enterprises/{}'.format(hex_dig[-15:]))
    db.write_data('enterprises', {
        'name': name,
        'sme': sme,
        'address': old_data['address']
    })


def make_order(quote, amount, pd, dd, sme, ce='test'):
    hash = hashlib.sha1(str(time.time()).encode())
    hex_dig = hash.hexdigest()
    uid = hex_dig[-15:]
    db.write_data('orders', {
        'quote': quote,
        'amount': amount,
        'payment_date': pd,
        'delivery_date': dd,
        'sme': sme,
        'ce': ce,
        'approved': 'no',
        'sme_approved': 'no'
    }, flag=uid)
    return uid


def update_order(uid, approval):
    old_data = db.get_data('orders/{}'.format(uid))
    if approval:
        old_data['approved'] = 'yes'
        old_data['insurance'] = approval
        db.write_data('orders', old_data, flag=uid)
    else:
        db.write_data('orders', {}, flag=uid)


def update_order_sme(uid, wc, wcd):
    old_data = db.get_data('orders/{}'.format(uid))
    old_data['wc'] = wc
    old_data['wcd'] = wcd
    old_data['sme_approved'] = 'yes'
    db.write_data('orders', old_data, flag=uid)


def update_order_ce(uid, insurance):
    old_data = db.get_data('orders/{}'.format(uid))
    old_data['insurance'] = insurance
    old_data['approved'] = 'yes'
    db.write_data('orders', old_data, flag=uid)


def make_line_graph():
    graph = pygal.Line()
    graph.title = '% Change Coolness of programming languages over time.'
    graph.x_labels = ['2011', '2012', '2013', '2014', '2015', '2016']
    graph.add('Python',  [15, 31, 89, 200, 356, 800])
    graph.add('Java',    [15, 45, 76, 80,  91,  95])
    graph.add('All others combined!',  [5, 15, 21, 55, 92, 105])
    graph_data = graph.render_data_uri()
    return graph_data


if __name__ == '__main__':
    update_sme('Devyanshu Shukla', ['test'])


'''
ce: 
name:
address:bc
sme-approved: []

'''
'''
sme:
address: bc,
ce: [],
name: 
'''

''' 
name
'''


'''

wkc required
amount order

'''
