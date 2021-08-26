import json
from models import Post,db
class WebServices:


    def post_request(self, j):
        data =json.loads(j)['root']
        name = data['name']
        lastname = data['lastname']
        age = int(data['age'])
        comment = data['txt']
        p = Post(name=name,lastname=lastname,age=age,comment=comment)
        db.session.add(p)
        db.session.commit()
#
