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
		name=formData.getvalue('name')
		course_no=formData.getvalue('course_no')
		dept_code=formData.getvalue('dept_code')
		try:
			cur.execute('insert into student values(%s,%s,%s,%s);',(roll_no,name,course_no,dept_code))
			db.commit()
			print ''' <p> New student registered </p> '''
		except:
			print ''' <p>Student already registered </p>'''
		print '''	<br> <br> <br> <br> <br> <br>
					<h3>
						<a href='stud.py'> Go back </a>  <br> <br>
						<a href='home.py'> Go to Home </a>
					</h3> '''
		tail()
	except:
		cgi.print_exception()