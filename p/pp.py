import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',passwd='1234', database='world')
p = con.cursor()
#p.execute("show databases")
sql = "select count(*),countrycode,language from countrylanguage group by countrycode,language"
sql1 = """select distinct language from countrylanguage"""
sql2 = """select  count(Continent), Continent  
from country group by Continent"""
sql3= """select * from actor"""
sql4 = """select amount , payment_id from payment group by amount,payment_id having abs(avg(amount))<4.30"""

sql5="""select customer.customer_id,payment.payment_id ,customer.first_name,payment.payment_id
 from customer 
 inner join payment 
 where customer.customer_id = payment.customer_id 
 order by customer.customer_id desc
 limit 100"""
sql6="""select film_id,title,description,length from film where (title='ACADEMY DINOSAUR' and length=86)
 or film_id=1
 """
sql7="""select film_id,title,description,length from film where (title='ACADEMY DINOSAUR' and length=86)
 and film_id<=120
"""
#%,_,NOT
sql8 = """select * from actor where first_name not like "_EN%" 
"""
sql9 = """select name,indepyear from country where Indepyear is not  NULL"""
sql10 = """select name,Continent from country where not (name = "Angola" or  Continent="North America")
"""
sql11 = """select name,Continent,LifeExpectancy from country where LifeExpectancy between 78.4 and 91.00
"""
sql12="""Create table cus(cid int,cname varchar(20) not null, primary key(cid))"""
#p.execute(sql12)
sql13 = """create table pro(pid int,pname varchar(20) not null,cid int,primary key(pid),
foreign key(cid) references cus(cid) ) """
# sql20 = "insert into cus(cid,cname) values(%s,%s)"
# for i in range(2):
#     id = int(input("Enter ID:"))
#     name = input("Enter Name:")
#     val = (id,name)
#     try:
#         p.execute(sql20,val)
#         con.commit()
#     except mysql.connector.Error as error:
#         con.rollback()
#         print(error)
        
#     print(p.rowcount)
#val = [(2,'Roman'),(3,'John'),(4,'John'),(5,'John'),(6,'John')]
# e=p.executemany(sql20,val)
# con.commit()
# print(p.rowcount)
#print("actor_id\t\tfirst_name\t\tlast_name\t\tlast_update")

# sql21 = """insert into pro(pid,pname,cid) values (%s,%s,%s)"""
# for i in range(2):
#         id = int(input("Enter P_ID:"))
#         name = input("Enter P_Name:")
#         cid = int(input("Enter C_ID:"))
#         val = (id,name,cid)
#         try:
#             p.execute(sql21,val)
#             con.commit()
#             print(p.rowcount)
#         except mysql.connector.Error as error:
#             con.rollback()
#             print(error)
            
#         print(p.rowcount)

sql23 = """Alter table pro 
add check(pid<=20) """
#p.execute(sql23)
sql24 = "insert into pro values(21,'ddd',5)"ls

#p.execute(sql24)

sql25 = """alter table pro
add email varchar(30) default "null" """
p.execute(sql25)

count=0
for i in p:
    count+=1
    for k in i:
        print(k,end='\t\t\t')
    print("")
print(count)


con.close()
p.close()