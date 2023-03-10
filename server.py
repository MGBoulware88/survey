from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ABC123'

@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/survey', methods=['POST', 'GET'])
def survey():
    print("Survey Submitted!")
    session["name"] = request.form['name']
    session["location"] = request.form['location']
    session["lang"] = request.form['lang']
    session['comment'] = request.form['comment']

    return redirect('/result')

@app.route('/result')
def survey_result():
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)