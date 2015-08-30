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
			all=cur.fetchall()
			print ''' <h2> Old information </h2>
						<form action='course_edit_done.py' method='POST' >
							<p> Course number </p>
							<input type='text' name='old_course_no' value='{all[0][0]}' readonly='readonly' />
							<p> Course name </p>
							<input type='text' name='old_course_name' value='{all[0][1]}' readonly='readonly' />
							<p> Instructor </p>
							<input type='text' name='old_instructor' value='{all[0][2]}' readonly='readonly' />
							<p> Slot </p>
							<input type='text' name='old_slot' value='{all[0][3]}' readonly='readonly' /> <br> <br>
							<h2> New information </h2>
							<p> Course number </p>
							<input type='text' name='course_no' autofocus required='required' value='{all[0][0]}' />
							<p> Course name </p>
							<input type='text' name='course_name' required='required' value='{all[0][1]}' />
							<p> Instructor </p>
							<input type='text' name='instructor' required='required' value='{all[0][2]}' />
							<p> Slot </p>
							<input type='text' name='slot' required='required' value='{all[0][3]}' /> <br> <br>
							<input type='submit' />
						</form> '''.format(**locals())
		except:
			print ''' <p> Invalid course number </p> '''
		print ''' <br> <br> <br> <br> 
				<h3>
				 	<a href='course.py'> Go back </a> <br> <br>
				 	<a href='home.py'> Go to home </a>
				 </h3> '''
		tail()
	except:
		cgi.print_exception()