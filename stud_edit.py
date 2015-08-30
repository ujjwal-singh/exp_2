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
		print ''' <form action='stud_edit_info.py' method='POST' >
					<p> Enter student roll number </p>
					<input type='text' name='roll_no' autofocus required='required' /> <br> <br>
					<input type='submit' /> 
				  </form> <br> <br> <br> <br> <br> <br>
   				  <h3>
					<a href='stud.py'> Go back </a>  <br> <br>
					<a href='home.py'> Go to Home </a>
				  </h3>'''
		tail()
	except:
		cgi.print_exception()