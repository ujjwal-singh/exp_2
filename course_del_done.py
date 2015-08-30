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
		course_no=formData.getvalue('course_no')
		try:
			cur.execute('select * from course where Course_No=%s;',(course_no))
			temp=cur.fetchall()[0][0]
			cur.execute('delete from course where Course_No=%s;',(course_no))
			db.commit()
			print ''' <p> Course deleted successfully. </p> '''
		except:
			print ''' <p> Invalid course number </p> '''
		print ''' <br> <br> <br> <br> <br> <br>
				<h3>
					<a href='course.py'> Go back </a> <br> <br>
					<a href='home.py'> Go to home </a>
				</h3> '''
		tail()
	except:
		cgi.print_exception()