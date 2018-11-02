from flask import Flask, render_template, request

from cutup import CutUp

app = Flask(__name__)

@app.route('/')
def cutup():
    return render_template("cutup.html")

@app.route("/cutup_results/", methods=['POST', 'GET'])
def cutup_results():
    if request.method=='POST':
        input1=request.form["cut_1"]
        input2=request.form["cut_2"]
        cutup=CutUp(input1,input2)

    return render_template("cutup_results.html", cutup_results = cutup)

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
