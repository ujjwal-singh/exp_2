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
		print ''' <h1> HOME </h1>
				  <h2>
					<a href='course.py'> Course Registration </a> <br> <br>
					<a href='dept.py'> Department registration </a> <br> <br>
					<a href='slot.py'> Slot registration </a> <br> <br>
					<a href='stud.py'> Student registration </a> <br> <br>
					<a href='stud_data_form.py'> Get student details </a>
				  </h2> '''
		tail()
	except:
		cgi.print_exception()