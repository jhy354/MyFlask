from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return 'Here is root!'

@app.route('/user/<username>')
def user_username(username):
   return f"Hello , {username}!"

@app.route('/user')
def user(username):
    if username == "admin":
        return redirect(url_for('user_username'))
    else:
        return redirect(url_for('admin'))

@app.route('/admin')
def admin():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    exit(0)