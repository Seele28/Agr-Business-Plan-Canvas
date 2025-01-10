from flask import Flask
from flask import render_template, request, url_for
from client import Client
from process import parse_answer
import time

app = Flask(__name__)

client = Client()

@app.route('/')
def start():  # put application's code here
    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        message = request.form['idea']
        start_time = time.time()
        answer = client.chat(message)
        end_time = time.time()
        answer = parse_answer(answer)
        return render_template('bmc.html',
                             key_partners=answer['key_partners'],
                             key_activities=answer['key_activities'],
                             key_resources=answer['key_resources'],
                             value_proposition=answer['value_propositions'],  #note that it doesnt match here
                             customer_relationship=answer['customer_relationships'],  # note that it doesnt match here
                             channels=answer['channels'],
                             customer_segments=answer['customer_segments'],
                             cost_structure=answer['cost_structure'],
                             revenue_streams=answer['revenue_streams'],
                             response_time=round(end_time-start_time, 2))

    return render_template('generate.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        q1 = request.form['question1']
        q2 = request.form['question2']
        q3 = request.form['question3']
        q4 = request.form['question4']
        q5 = request.form['question5']
        q6 = request.form['question6']
        q7 = request.form['question7']
        q8 = request.form['question8']
        q9 = request.form['question9']

        message = f"Construct a Business Canvas Model according to the information: {q1} {q2} {q3} {q4} {q5} {q6} {q7} {q8} {q9}"
        start_time = time.time()
        answer = client.chat(message)
        end_time = time.time()
        print(answer)
        answer = parse_answer(answer)

        return render_template('bmc.html',
                               key_partners=answer['key_partners'],
                               key_activities=answer['key_activities'],
                               key_resources=answer['key_resources'],
                               value_proposition=answer['value_propositions'],
                               customer_relationship=answer['customer_relationships'],
                               channels=answer['channels'],
                               customer_segments=answer['customer_segments'],
                               cost_structure=answer['cost_structure'],
                               revenue_streams=answer['revenue_streams'],
                               response_time=round(end_time - start_time, 2))

    return render_template('question.html')


if __name__ == '__main__':
    app.run()