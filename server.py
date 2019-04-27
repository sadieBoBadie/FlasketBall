from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "unicorns"


@app.route('/') 
def index(): 
    session.clear()
    print(session)
    return render_template("index.html", )

@app.route('/leaderboard')
def leaderBoard():

    print(session)

    if "user_name" not in session:
        print('redirecting...')
        return redirect('/')

    if "first" not in session or "second" not in session or "third" not in session:
        session["no_rank"] = True
        session['first'] = 'Please assign a rank'
        session['second'] = 'Please assign a rank'
        session['third'] = 'Please assign a rank'


    return render_template("leaderboard.html", first=session['first'], second=session['second'], third=session['third'])

@app.route('/show/<rank>')
def show(rank):

    print(session)
    print(rank)

    name = ""

    if session["no_rank"]:
        return redirect('/leaderboard')

    if rank == "1":
        name = session['first']
        print(name)
    elif rank == "2":
        name = session['second']
    else:
        name = session['third']

    return render_template("showFriend.html", rank=rank, name=name)

@app.route('/enter', methods = ['POST'])
def enter():
    print(request.form)
    name = request.form["FirstName"] + " " + request.form["Last_Name"]
    session['user_name'] = name
    return redirect('/leaderboard')

@app.route("/changeRanks", methods = ["POST"])
def changeRanks():

    print(request.form)

    session["no_rank"] = False
    session['first'] = request.form['first']
    session['second'] = request.form['second']
    session['third'] = request.form['third']

    return redirect('/leaderboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)