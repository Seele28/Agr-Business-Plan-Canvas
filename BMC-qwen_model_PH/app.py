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
        q10 = request.form['question10']
        q11 = request.form['question11']
        q12 = request.form['question12']
        q13 = request.form['question13']
        q14 = request.form['question14']
        q15 = request.form['question15']
        q16 = request.form['question16']
        q17 = request.form['question17']
        q18 = request.form['question18']
        q19 = request.form['question19']
        q20 = request.form['question20']
        q21 = request.form['question21']
        q22 = request.form['question22']
        q23 = request.form['question23']
        q24 = request.form['question24']
        q25 = request.form['question25']
        q26 = request.form['question26']
        q27 = request.form['question27']
        q28 = request.form['question28']
        q29 = request.form['question29']
        q30 = request.form['question30']
        q31 = request.form['question31']
        q32 = request.form['question32']
        q33 = request.form['question33']
        q34 = request.form['question34']
        q35 = request.form['question35']
        q36 = request.form['question36']
        q37 = request.form['question37']
        q38 = request.form['question38']
        q39 = request.form['question39']
        q40 = request.form['question40']
        q41 = request.form['question41']
        q42 = request.form['question42']
        q43 = request.form['question43']
        q44 = request.form['question44']
        q45 = request.form['question45']

        message = f"Construct a Business Canvas Model according to the information: {q1} {q2} {q3} {q4} {q5} {q6} {q7} {q8} {q9} {q10} {q11} {q12} {q13} {q14} {q15} {q16} {q17} {q18} {q19} {q20} {q21} {q22} {q23} {q24} {q25} {q26} {q27} {q28} {q29} {q30} {q31} {q32} {q33} {q34} {q35} {q36} {q37} {q38} {q39} {q40} {q41} {q42} {q43} {q44} {q45}"
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
