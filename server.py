from operator import contains
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def main():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html')
@app.route('/count')
def count():
    pass
@app.route('/delete')
def delete():
    session.clear()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)