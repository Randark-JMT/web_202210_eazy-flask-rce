import flask
import subprocess

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "Try to access the /rce"


@app.route("/www.zip")
def return_SourceCode():
    with open("./app.py", "r") as f:
        return f.read()


@app.route("/rce", methods=['GET', 'POST'])
def action_rce():
    if flask.request.method == "GET":
        return "Why not try to search the backup"
    elif flask.request.method == "POST":
        action = flask.request.form["act"]
        with open("/app/temp.sh", "w") as f:
            f.write(action[1:-1])
        res = subprocess.run(["/bin/bash", "/app/temp.sh"], stdout=subprocess.PIPE)
        # print(res)
        return "success"


if __name__ == '__main__':
    app.run(debug=True)
