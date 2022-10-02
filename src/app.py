import flask
import subprocess

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "Try to access the /rce"


@app.route("/www.zip")
def return_sourcecode():
    with open("./app.py", "r") as f:
        return f.read()

@app.route("/rce", methods=['GET', 'POST'])
def action_rce():
    if flask.request.method == "GET":
        return "Why not try to search the backup"
    elif flask.request.method == "POST":
        action = flask.request.form["act"]
        action = action.split(" ")
        if action[0] not in ["ls", "cat", "env"]:
            return "What are you doing!"
        for i in range(len(action)):
            if action[i]==" " or action[i]=="":
                action.pop(i)
        if len(action)>1 and "/" in action[1]:
            return "nonono"
        else:
            res = subprocess.run(action, stdout=subprocess.PIPE)
            print(res)
            return res.stdout

if __name__ == '__main__':
    app.run(debug=True)
