from flask import *
from DB import *
from DB import insert

from DB import check

from DB import userdetails

from DB import singleuser

from DB import update

from DB import delete

app=Flask(__name__)

@app.route("/")
def hom():
   return render_template("home.html")

@app.route("/reg")
def register():
    return render_template("register.html")

@app.route("/boot")
def boot():
    return render_template("boot.html")


@app.route("/log")
def login():
    return render_template("login.html")

@app.route("/details")
def details():
    data=userdetails()
    return render_template("showdetails.html",elist=data)

@app.route("/insert_data",methods=["post"])
def ins():
    name=request.form["name"]
    phone=request.form["phone"]
    email=request.form["email"]
    password=request.form["password"]
    option=request.form["options"]
    note=request.form["note"]
    t=(name,phone,email,password,option,note)
    insert(t)
    return redirect("/details")
@app.route("/login",methods=["post"])
def log():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=check(email)
    if t in t1:
        return redirect("/details")
    else:
        return redirect("/log")
@app.route("/edit")
def edit():
    email = request.args.get("email")
    info =singleuser(email)
    return render_template("edit.html",data=info[0])
@app.route("/insagain",methods = ["post"])
def insagain():
    name=request.form["name"]
    phone=request.form["phone"]
    email=request.form["email"]
    password=request.form["password"]
    option=request.form["options"]
    note=request.form["note"]
    t=(name,phone,email,password,option,note,email)
    update(t)
    return redirect("/details")

@app.route("/delete")
def delet():
    email: str | None=request.args.get("email")
    delete(email)
    return redirect("/details")



if __name__=="__main__":
    app.run(debug=True)
