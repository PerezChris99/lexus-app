from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']rere
        comments = request.form['comments']
        #print(customer, dealer, rating, comments)

        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter the required fields')
        return render_template('success.html')



if __name__ == '__main__':
    app.debug = True
    app.run()