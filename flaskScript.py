from flask import Flask, render_template, request

from cutup import CutUp
from scrape import getText
from isUrl import isUrl

app = Flask(__name__)

@app.route('/')
def cutup():
    return render_template("cutup.html")

@app.route("/cutup_results/", methods=['POST', 'GET'])
def cutup_results():
    if request.method=='POST':
        input1=request.form["cut_1"]
        input2=request.form["cut_2"]

        if isUrl(input1) == True:
            input1 = getText(input1)
        if isUrl(input2) == True:
            input2 = getText(input2)

        cutup=CutUp(input1,input2)

    return render_template("cutup_results.html", cutup_results = cutup)

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
