#!C:/Python27/python

print "Content-Type: text/html"
print ""

import cgi
import MySQLdb

def head():
	print '''<html>
				<head>
					<title> Exp </title>
				</head>
				<body>'''
				
def tail():
	print '''</body>
			</html>'''
			
if __name__=="__main__":
	try:
		head()
		db=MySQLdb.connect(host='localhost',user='root',passwd='',db='courses')
		cur=db.cursor()
		formData=cgi.FieldStorage()
		roll_no=formData.getvalue('roll_no')
		try:
			cur.execute('select * from student where Roll_no=%s;',(roll_no))
			temp=cur.fetchall()[0][0]
			cur.execute('delete from student where Roll_no=%s;',(roll_no))
			print ''' <p> Student record deleted </p> ''' 
			db.commit()
		except:
			print ''' <p> Invalid roll number, not in database. </p> ''' 
		print ''' <br> <br> <br> <br> <br> <br>
				<h3>
					<a href='stud.py'> Go back </a>  <br> <br>
					<a href='home.py'> Go to Home </a>
				</h3>'''
		tail()
	except:
		cgi.print_exception()