from firebase import firebase
import hashlib


class Database:

    def __init__(self):
        self.fb = firebase.FirebaseApplication(
            'https://daiict-db.firebaseio.com/', None)

    def get_data(self, category, unid):
        ratings = self.fb.get('/ratings', None)

    def write_data(self, category, data):
        gen = data['name']
        hash_object = hashlib.sha1(gen.encode())
        hex_dig = hash_object.hexdigest()
        result = self.fb.put('/' + category, hex_dig[-15:], data)


if __name__ == '__main__':
    db = Database()
    db.write_data('enterprises', {
        'name': 'Test SME',
        'fields': 'test fields'
    })
