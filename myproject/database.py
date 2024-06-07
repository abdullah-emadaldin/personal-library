import sqlite3

def create_table():#for main books
    conn=sqlite3.connect("training.db")
    conn.cursor()
    conn.execute("create table if not exists task (id integer primary key,firstname text,lastname text,year text,username text)")



def create_table2():#for borrowed books
    conn=sqlite3.connect("training2.db")
    conn.cursor()
    conn.execute("create table if not exists task2 (id integer primary key,firstname text,lastname text,year text,l_to text,username text)")


def connect():
    conn = sqlite3.connect("training.db",detect_types=sqlite3.PARSE_DECLTYPES)
    return conn



def insert(fn,ln,year,u):
    conn=connect()
    conn.cursor()
    conn.execute("INSERT INTO task VALUES (NULL,?,?,?,?)",(fn,ln,year,u))
    conn.commit()
    conn.close()

def insertborow(fn,ln,year,l,u):
    conn=connect2()
    conn.cursor()
    conn.execute("INSERT INTO task2 VALUES (NULL,?,?,?,?,?)",(fn,ln,year,l,u))
    conn.commit()
    conn.close()

def view(u):
    conn = sqlite3.connect("training.db")
    cur = conn.cursor()
    cur.execute("SELECT id,firstname,lastname,year FROM task where username=?",(u,))
    rows = cur.fetchall()
    conn.close()
    return rows

def viewborrow(u):
    conn = sqlite3.connect("training2.db")
    cur = conn.cursor()
    cur.execute("SELECT id,firstname,lastname,year,l_to FROM task2 where username=?",(u,))
    rows = cur.fetchall()
    conn.close()
    return rows



def update(id,fn,ln,y):
    conn = sqlite3.connect("training.db")
    cur = conn.cursor()
    cur.execute("UPDATE task SET firstname=?, lastname=?,year=? WHERE id=?",(fn,ln,y,id))
    conn.commit()
    conn.close()


def updateborrowed(id,fn,ln,y,l):
    conn = sqlite3.connect("training2.db")
    cur = conn.cursor()
    cur.execute("UPDATE task2 SET firstname=?, lastname=?,year=?,l_to=? WHERE id=?",(fn,ln,y,l,id))
    conn.commit()
    conn.close()

def search(id):
    conn = sqlite3.connect("training.db")
    cur = conn.cursor()
    cur.execute("SELECT id,firstname,lastname,year FROM task WHERE id=?",(id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def connect2():
    conn = sqlite3.connect("training2.db",detect_types=sqlite3.PARSE_DECLTYPES)
    return conn



def create_table3():
    conn=sqlite3.connect("training3.db")
    conn.cursor()
    conn.execute("create table if not exists task3 (id integer primary key,firstname text,lastname text,year text,l timestamp,l_to text,username text)")

def view3(u):
    conn = sqlite3.connect("training3.db")
    cur = conn.cursor()
    cur.execute("SELECT id,firstname,lastname,year,l,l_to FROM task3 where username=?",(u,))
    rows = cur.fetchall()
    conn.close()
    return rows

def insert3(fn,ln,y,d,l,u):#lend history , d for date , l for lend to

    conn=sqlite3.connect("training3.db")
    conn.cursor()
    conn.execute("INSERT INTO task3 VALUES (NULL,?,?,?,?,?,?)",(fn,ln,y,d,l,u))
    conn.commit()
    conn.close()



def create_table_acc():#for accounts
    conn=sqlite3.connect("accounts.db")
    conn.cursor()
    conn.execute("create table if not exists acc (username text primary key, pass text,email text)")

def insert2(u,p,e):

    conn=sqlite3.connect("accounts.db")
    conn.cursor()
    conn.execute("INSERT INTO acc VALUES (?,?,?)",(u,p,e))
    conn.commit()
    conn.close()

def search_acc(u,p):
    conn = sqlite3.connect("accounts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM acc WHERE username=? AND pass=?", (u,p))
    rows = cur.fetchall()
    conn.close()
    try:
        if u in rows[0][0]:
            print("i found it")
            return 1
    except IndexError  as x:
            print("sorry :(")
            return 0
def view_acc():
    conn = sqlite3.connect("accounts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM acc")
    rows = cur.fetchall()
    conn.close()
    return rows



create_table_acc()
create_table3()
create_table2()
create_table()
connect2()


print(view_acc())