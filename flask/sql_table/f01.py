from flask import Flask,request
import util
app = Flask(__name__)


@app.route('/')
def index():
    util.update_data()
    return util.get_all_html()

@app.route('/add')
def add():
    util.update_data()
    data = util.file_data
    user = request.args['user']
    age = request.args['age']
    if not user or not age:
        res = '<p>you need input user and age</p>'+res
    elif user in data:
        res = '<p>user already exist</p>' + res
    else:
        util.update_file(user,age)
        util.file_data[user] = age
    return util.get_all_html()

@app.route('/delete')
def delete():
    util.update_data()
    user = request.args.get('user')
    if user and user in util.file_data:
        util.dele(user)
        del util.file_data[user]
        return  util.get_all_html()
    else:
        return "invalid user"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='52000')

