import mysql.connector
import difflib, itertools

con=mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
a=input('Enter a word: ')
cursor =con.cursor()
q1=cursor.execute("SELECT Expression FROM Dictionary")
b=cursor.fetchall()
b=list(itertools.chain(*b))
q=cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"%a)
results=cursor.fetchall()
if results:
    for i in results:
        print(i[1])
elif len(difflib.get_close_matches(a,b))>0:
    c=input("did you mean %s ? if yes type Y, else N: "%(difflib.get_close_matches(a,b)[0]))
    if c=='Y' or c=='y':
        cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"%(difflib.get_close_matches(a,b)[0]))
        r=cursor.fetchall()
        if r:
            for i in r:
                print(i[1])

else:
    print('No word Found Please try again')