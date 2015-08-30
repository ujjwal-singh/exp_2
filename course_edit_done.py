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
		old_course_no=formData.getvalue('old_course_no')
		course_no=formData.getvalue('course_no')
		course_name=formData.getvalue('course_name')
		instructor=formData.getvalue('instructor')
		slot=formData.getvalue('slot')
		try:
			cur.execute('delete from course where Course_No=%s;',(old_course_no))
			cur.execute('insert into course values(%s,%s,%s,%s);',(course_no,course_name,instructor,slot))
			db.commit()
			print ''' <h2> Course details edited successfuly </h2> '''
		except:
			print ''' <p> Course number already registered </p> '''
		print '''<br> <br> <br> <br> <br> <br>
				 <h3>
				 	<a href='course.py'> Go back </a> <br> <br>
				 	<a href='home.py'> Go to home </a>
				 </h3> '''
		tail()
	except:
		cgi.print_exception()