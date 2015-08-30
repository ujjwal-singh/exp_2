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
			all=cur.fetchall()
			print ''' <form action='stud_edit_done.py' method='POST'>
						<h2> Old information </h2>
						<p> Roll number </p>
						<input type='text' name='old_roll_no' value="{all[0][0]}" readonly='readonly' />
						<p> Name </p>
						<input type='text' name='old_name' value="{all[0][1]}" readonly='readonly' />
						<p> Course number </p>
						<input type='text' name='old_course_no' value="{all[0][2]}" readonly='readonly' style='width:20%' />
						<p> Department code </p>
						<input type='text' name='old_dept' readonly='readonly' value="{all[0][3]}" /> <br> <br> <br>
						<h2> New information </h2>
						<p> Enter roll number </p>
						<input type='text' name='roll_no' autofocus required='required' value="{all[0][0]}" />
						<p> Enter name </p>
						<input type='text' name='name' required='required' value="{all[0][1]}" />
						<p> Enter course number (Comma separated) </p>
						<input type='text' name='course_no' required='required' value="{all[0][2]}" style='width:20%' />
						<p> Enter department code </p>
						<input type='text' name='dept_code' required='required' value="{all[0][3]}" /> <br> <br>
						<input type='submit' />
					 </form>  <br> <br> <br> <br> <br> <br>
					<h3>
						<a href='stud.py'> Go back </a>  <br> <br>
						<a href='home.py'> Go to Home </a>
					</h3> '''.format(**locals())
		except:
			print ''' <p> Invalid roll number </p> '''
		tail()
	except:
		cgi.print_exception()