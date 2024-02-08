from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "hiii"

@app.route("/passs/<int:sco>")
def pas(sco):
    return "pass score " + str(sco)


@app.route("/fail/<int:sco>")
def fal(sco):
    return "fail score " + str(sco)

@app.route("/result/<int:sc>")
def decide(sc):
    if(sc>30):
        return redirect(url_for('passs',sco = sc))
    else:
        return redirect(url_for('fail',sco = sc))


if __name__ == "__main__":
    app.run(debug=True)



##building the url Dynamically
##Variable rules and url

# @app.route('/s/<int:s>')
# def a(s):
#     return 'welcome to page a' + str(s)


# @app.route('/result/<int:s>')
# def a(s):
#     if s<30:
#         return "Fail"
#     else:
#         return "Pass"
    
#####building the url Dynamically
# @app.route("/passs/<int:sco>")
# def pas(sco):
#     return "pass score " + str(sco)


# @app.route("/fail/<int:sco>")
# def fal(sco):
#     return "fail score " + str(sco)

# @app.route("/result/<int:sc>")
# def decide(sc):
#     if(sc>30):
#         return redirect(url_for('passs',sco = sc))
#     else:
#         return redirect(url_for('fail',sco = sc))