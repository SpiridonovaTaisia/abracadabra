from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/heartbeat")
def hello_world():
    return {'message': 'OK'}

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/form', methods=['POST'])
def form():
    user_data = request.form['user_data']
    return render_template('result.html', user_data=user_data)

if __name__ == '__main__':
  app.run(debug=True)