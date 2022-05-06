from distutils.log import debug
from flask import Flask, render_template, request, redirect
from scrapper import getJobs

app = Flask(__name__, template_folder="templates")

db = {}


@app.route("/")  # @:decorater below funcs(@ look only functons!)
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = getJobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", SearchingWord=word, resultNumber=len(jobs), jobs=jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        return f"Generate CSV for {word}"
    except:
        return redirect("/")


app.run(host="127.0.0.1", port="5000", debug=True)
