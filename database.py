from firebase import firebase
import hashlib


class Database:

    def __init__(self):
        self.fb = firebase.FirebaseApplication(
            'https://daiict-db.firebaseio.com/', None)

    def get_data(self, category):
        data = self.fb.get('/{}'.format(category), None)
        return data

    def write_data(self, category, data, flag=False):
        if not flag:
            gen = data['name']
        else:
            gen = flag
        hash_object = hashlib.sha1(gen.encode())
        hex_dig = hash_object.hexdigest()
        result = self.fb.put('/' + category, hex_dig[-15:], data)
        return True


if __name__ == '__main__':
    db = Database()
    db.write_data('enterprises', {
        'name': 'Test SME',
        'fields': 'test fields'
    })
