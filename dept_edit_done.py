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
		old_dept_code=formData.getvalue('old_dept_code')
		dept_code=formData.getvalue('dept_code')
		dept_name=formData.getvalue('dept_name')
		try:
			cur.execute('delete from department where Dept_Code=%s;',(old_dept_code))
			cur.execute('insert into department values(%s,%s);',(dept_code,dept_name))
			db.commit()
			print ''' <p> Department details edited successfully. </p> '''
		except:
			print ''' <p> Department code is already registered </p> '''
		print '''   <br> <br> <br> <br> <br> <br>
					<h3>
					<a href='dept.py'> Go back </a> <br> <br>
					<a href='home.py'> Go to home </a>
				   </h3> '''
		tail()
	except:
		cgi.print_exception()