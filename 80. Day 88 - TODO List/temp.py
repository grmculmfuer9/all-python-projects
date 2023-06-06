from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['input_field']
        return f'The data entered is: {data}'
    return '''
        <form method="POST">
            <input type="text" name="input_field">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)