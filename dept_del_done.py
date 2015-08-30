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
		dept_code=formData.getvalue('dept_code')
		try:
			cur.execute('select * from department where Dept_Code=%s;',(dept_code))
			temp=cur.fetchall()[0][0]
			cur.execute('delete from department where Dept_Code=%s;',(dept_code))
			db.commit()
			print ''' <p> Department deleted successfuly. </p> '''
		except:
			print ''' <p> Invalid department code </p> '''
		print '''   <br> <br> <br> <br> <br> <br>
					<h3>
					<a href='dept.py'> Go back </a> <br> <br>
					<a href='home.py'> Go to home </a>
				   </h3> '''
		tail()
	except:
		cgi.print_exception()