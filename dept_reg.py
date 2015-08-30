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
		code=formData.getvalue('dept_code')
		name=formData.getvalue('dept_name')
		try:
			cur.execute('insert into department values(%s,%s);',(code,name))
			db.commit()
			print ''' <p> New dept. registered </p> '''
		except:
			print ''' <p> Department already registered </p> '''
		print '''<h3>
					<br> <br> <br> <br>
					<a href='dept.py'> Go back </a> <br> <br>
					<a href='home.py'> Go to home </a>
				</h3> '''
		tail()
	except:
		cgi.print_exception()