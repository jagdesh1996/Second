import mysql.connector

connection = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='Product')
pointer = connection.cursor()

sql_1 = "Select * from customer"
pointer.execute(sql_1)
data = pointer.fetchall()
for i in data:
    print(i)
    if i==1:
        sql_1 = "update customer set cid=%s where cid = 1"
        val = (50,)
        pointer.execute(sql_1,val)
        connection.commit()
        print("ok")
        break

connection.close()
pointer.close()
