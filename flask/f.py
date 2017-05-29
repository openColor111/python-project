from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def index():
    f = open('log/demo.log')
    str1 = f.read().strip()
    l1 = str1.split("\n")
    str2 = '<table border="2"><tr>'
    for i in l1:
        name,age=i.split(":")
        str2+="<td>"+ name+ "</td>"
        str2+="<td>"+ age+ "</td>"
        str2+="</tr>"
    else:
        str2+="</table>"
    return str2
 

@app.route('/search')
def search():
    return request.args['user']

@app.route('/del',methods=['GET'])
def delete():
    return render_template('delete.html')


@app.route('/root')
def ka():
    return "reboot"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10008)

