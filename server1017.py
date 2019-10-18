from flask import Flask, render_template, request
import bitUtil.stu

app = Flask(__name__)

@app.route("/info/<irum>")
def infoStudent(irum):
    s = bitUtil.stu.getStudent(irum)
    return render_template("infoStudent.html",s=s)

@app.route("/insert", methods=['GET'])
def infoStudentGet():
    return render_template("infoStudent.html")

@app.route("/insert", methods=['POST'])
def infoStudentPost():
    name = request.form['name']
    kor = int(request.form['kor'])
    eng = int(request.form['eng'])
    math = int(request.form['math'])
    doc = {"name":name,"kor":kor,"eng":eng,"math":math}
    s = bitUtil.stu.insertStudent(doc)
    return render_template("infoStudent.html")


@app.route("/hello/<irum>")
def hello(irum):
   return render_template("hello.html", name=irum)


@app.route("/listStudent")
def listStudent():
    return bitUtil.stu.listStudent()

@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
    app.run()
