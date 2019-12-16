# import Flask
from flask import Flask, redirect, render_template, request, session, flash, get_flashed_messages
# the "re" module will let us perform some regular expression operations
import re
app = Flask(__name__)
app.secret_key = "HG&xAGe886DwcmG%Em[GN,kc?/42Gy/2D4d9HAXRRMYNkG)Vv2mEDcr.;LRcq2Fm"

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/process', methods=['POST'])
def process_form():

    # Validate Email
    if len(request.form['email']) < 1:
        flash("Email cannot be blank", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!', 'email')
    if len(request.form['name']) < 1:
        flash('Name cannot by empty', 'name')
    elif len(request.form['name']) <= 3:
        flash('Name must be 3+ characters', 'name')
    
    if '_flashes' in session.keys():
        print (session['_flashes'])
        return redirect('/')
    else:
        return redirect("/success")
    # else:
    #     flash(f"Success! Your name is {request.form['name']}")
        # message = get_flashed_messages('name')
        # print(message[0][1])

    # print(get_flashed_messages(True))

    # for message in get_flashed_messages(True):
    #     print(message)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
