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
			all=cur.fetchall()
			print ''' <form action='dept_edit_done.py' method='POST'>
						<h2> Old information </h2>
						<p> Department code </p>
						<input type='text' name='old_dept_code' value='{all[0][0]}' readonly='readonly' />
						<p> Department name </p>
						<input type='text' name='old_dept_name' value='{all[0][1]}' readonly='readonly' /> <br> <br>
						<h2> New information </h2>
						<p> Department code </p>
						<input type='text' name='dept_code' value='{all[0][0]}' autofocus required='required' />
						<p> Department name </p>
						<input type='text' name='dept_name' value='{all[0][1]}' required='required' /> <br> <br>
						<input type='submit' /> '''.format(**locals())
		except:
			print ''' <p> Invalid department code </p> '''
		print '''	<br> <br> <br> <br>
					<h3>
							<a href='dept.py'> Go back </a> <br> <br>
							<a href='home.py'> Go to home </a>
					</h3> '''
		tail()
	except:
		cgi.print_exception()