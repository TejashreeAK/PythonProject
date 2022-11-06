import pymysql as p
def getConnection():
    return p.connect(host="localhost",user="root",password="",database="first")
def insert(t):
    con=getConnection()
    cur=con.cursor()
    sql="insert into details values(%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
def check(email):
    con=getConnection()
    cur=con.cursor()
    sql="select email,password from details where email = %s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
def userdetails():
    con=getConnection()
    cur=con.cursor()
    sql="select * from details"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
def singleuser(email):
    con=getConnection()
    cur=con.cursor()
    sql="select * from details where email=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def update(t):
    con=getConnection()
    cur=con.cursor()
    sql="update details set name=%s,phone=%s,email=%s,password=%s,option=%s,note=%s where email= %s"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
def delete(email):
    con=getConnection()
    cur=con.cursor()
    sql="delete from details where email = %s"
    cur.execute(sql,email)
    con.commit()
    con.close()

