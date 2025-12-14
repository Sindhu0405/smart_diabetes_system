from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
user_data = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_data['name'] = request.form['username']
        user_data['age'] = request.form['age']
        return redirect(url_for('symptoms'))
    return render_template('login.html')

@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    if request.method == 'POST':
        symptoms = request.form.to_dict()
        user_data['glucose'] = symptoms.get('glucose')
        insulin = 5 + sum(symptoms.get(k) == 'yes' for k in ['fatigue', 'blurred_vision', 'increased_thirst', 'frequent_urination']) * 2
        return render_template('result.html', name=user_data['name'], age=user_data['age'],
                               glucose=user_data['glucose'], insulin=insulin)
    return render_template('symptoms.html')

if __name__ == '__main__':
    app.run(debug=True)
