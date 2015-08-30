#!C:/Python27/python

print "Content-Type: text/html"
print ""

import cgi

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
		print ''' <h1> New student registration form </h1>
					<form action='stud_reg.py' method='POST' >
						<p> Enter roll number </p>
						<input type='text' name='roll_no' autofocus required='required' />
						<p> Enter name </p>
						<input type='text' name='name' required='required' />
						<p> Enter course number (Comma separated) </p>
						<input type='text' name='course_no' required='required' placeholder='e.g. MA-101,CSO-101' style='width:20%' />
						<p> Enter department code </p>
						<input type='text' name='dept_code' required='required' /> <br> <br>
						<input type='submit' />
					</form>  <br> <br> <br> <br> <br> <br>
					<h3>
						<a href='stud.py'> Go back </a>  <br> <br>
						<a href='home.py'> Go to Home </a>
					</h3>'''
		tail()
	except:
		cgi.print_exception()