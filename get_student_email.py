import pyodbc

login = 'zane_hill1'
pw = 'MIS4322student'

preList = {}
courseList = []
cn_str = (

    'Driver={SQL Server Native Client 11.0};'
    'Server=MIS-SQLJB;'
    'Database=School;'
    'UID='+login+';'
    'PWD='+pw+';'

)

# connect to server

cn = pyodbc.connect(cn_str)

cursor = cn.cursor()
cursor.execute('exec getStudentEmail')

data = cursor.fetchall()

#

print('First Name'.ljust(20), 'Last Name'.ljust(18), 'Personal Email'.ljust(30), 'Work Email'.ljust(30))
print('----------'.ljust(20), '---------'.ljust(18), '--------------'.ljust(30), '----------'.ljust(30))

for row in data:
    print(row[0].ljust(20), row[1].ljust(18), row[2].ljust(30), row[3].ljust(30))