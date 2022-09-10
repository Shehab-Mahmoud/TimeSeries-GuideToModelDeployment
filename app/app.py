from flask import Flask,render_template,request
from model import predict
from datetime import datetime as dt

app = Flask(__name__)


@app.route('/',methods = ['POST','GET'])
def index():
    if request.method =='POST':
        date = request.form['content']
        temp = round(predict(date))
        date_out = dt.strptime(date,"%Y-%m-%d").date()
        date_out = str(date_out.month) + '-'+ str(date_out.year)
        return render_template('index.html',prediction =temp , date = date_out)
        
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')