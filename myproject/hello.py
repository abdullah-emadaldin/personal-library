from datetime import *
import database
from flask import *



app = Flask(__name__)


@app.route("/",methods=['POST','GET'])
def signup():
     global us,ps #username and password
     if 'log' in request.form:
         us=request.form['name']
         ps=request.form['password']

         x=database.search_acc(us,ps)
         if x == 1:
             return redirect(url_for("hello_world"))
         else:
             x=["wrong username or password please try again","sfgsg"]
             return render_template("sign.html",row=x)

     elif 'sign' in request.form:

        u = request.form['name1']
        p = request.form['password1']
        e= request.form['email1']

        database.insert2(u,p,e)



        x = [" ", " "]
        return render_template("sign.html", row=x)
     else:
        x=[" "," "]
        return render_template("sign.html",row=x)





@app.route("/library")
def hello_world():

    data=database.view(us)
    return render_template("search_t.html",row=data)





@app.route("/add",methods=['POST','GET'])
def add_trainee():
    if request.method == 'POST':
        year=request.form['year']
        user=request.form['username']
        pas=request.form['password']
        database.insert(user,pas,year,us)
        print(user + '\n' + pas)

    return render_template("add.html")














@app.route("/update/<id>",methods=['POST','GET'])
def update(id):

    if request.method == "GET":
        conn = database.connect()
        conn=conn.cursor().execute("select * from task where id=?",(id,))
        row=conn.fetchone()
        conn.close()
        return render_template("update.html",row=row)
    elif request.method=="POST":
        year=request.form['year']
        name = request.form['fn']
        author = request.form['ln']
        database.update(id,name,author,year)
        data=database.view(us)
        return render_template("search_t.html",row=data)



    return redirect(url_for("hello_world"))



@app.post("/search")
def search():

    if 'name' in request.form:
        name=request.form['name']
        conn=database.connect()
        conn=conn.cursor().execute(f"select id,firstname,lastname,year from task where firstname like '{name}%' and username=?",(us,))
        data=conn.fetchall()
        conn.close()
        return render_template("search_t.html",row=data)
    row=database.view(us)
    return render_template("search_t.html",row=row)

@app.route("/delete/<id>")
def delete(id):
    conn=database.connect()
    conn.execute("delete from task where id=?",(id,))
    conn.commit()
    conn.close()
    return redirect(url_for("hello_world"))








@app.route("/borrow/<id>/<firstname>/<lastname>/<year>",methods=['POST','GET'])
def borrow(id,firstname,lastname,year):


    if request.method == "GET":
        conn = database.connect()
        conn = conn.cursor().execute("select * from task where id=?", (id,))
        row = conn.fetchone()
        conn.close()
        return render_template("borrowed_to.html", row=row)
    elif request.method == "POST":
        t=datetime.now()


        conn = database.connect()
        conn.execute("delete from task where id=?", (id,))
        conn.commit()
        conn.close()
        lend = request.form['l_to']
        database.insertborow(firstname,lastname,year,lend,us)
        database.insert3(firstname,lastname,year,t.strftime("%d/%m/%Y %H:%M:%S"),lend,us)
        row=database.viewborrow(us)
        return render_template("borrow.html", row=row)




    return redirect(url_for("hello_world"))

@app.route("/deleteborrow/<id>")
def deleteborrow(id):
    conn=database.connect2()
    conn.execute("delete from task2 where id=?",(id,))
    conn.commit()
    conn.close()
    data=database.viewborrow(us)
    return render_template("borrow.html", row=data)


@app.route("/view_borrow")
def view_borrow():
    data=database.viewborrow(us)
    return render_template("borrow.html",row=data)


@app.route("/retrieve/<id>/<firstname>/<lastname>/<year>",methods=['POST','GET'])
def retrieve(id,firstname,lastname,year):
    if request.method == "GET":
        conn = database.connect2()
        conn.execute("delete from task2 where id=?", (id,))
        conn.commit()
        conn.close()
        database.insert(firstname,lastname,year,us)
        row=database.view(us)
        return render_template("search_t.html", row=row)



@app.route("/updateb/<id>",methods=['POST','GET'])
def updateb(id):

    if request.method == "GET":
        conn = database.connect2()
        conn=conn.cursor().execute("select * from task2 where id=?",(id,))
        row=conn.fetchone()
        conn.close()
        return render_template("update_borrow.html",row=row)
    elif request.method=="POST":
        year=request.form['year']
        name = request.form['fn']
        author = request.form['ln']
        lend = request.form['l_to']
        database.updateborrowed(id,name,author,year,lend)
        data=database.viewborrow(us)
        return render_template("borrow.html",row=data)



    return redirect(url_for("hello_world"))


@app.route("/history",methods=['POST','GET'])
def show_borrowed_history():
    data=database.view3(us)

    return render_template("borrow_history.html",row=data)
