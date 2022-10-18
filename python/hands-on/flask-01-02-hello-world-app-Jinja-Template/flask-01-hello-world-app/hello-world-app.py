from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Hello World!</h1>"

@app.route('/second')
def second():
    return 'Bize her yer Trabzon!!!'

@app.route('/third/subthird')
def third():
    return '''This is the subpage of Akgun's third page.'''

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'

if __name__ == "__main__":
    app.run(debug=True, port=2000)