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
		print ''' <h2> Department menu </h2> <br>
					<h3>
						<a href='dept_form.py'> Register new department </a> <br> <br>
						<a href='dept_edit.py'> Edit a department </a> <br> <br>
						<a href='dept_del.py'> Delete a department </a> <br> <br> <br> <br> <br> <br>
						<a href='home.py'> Go to home </a>
					</h3> '''
		tail()
	except:
		cgi.print_exception()