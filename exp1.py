#!C:\Program Files\Python37\python.exe
def calc(a,b,c):
    if c=='+':
       print("addition:",(int(a)+int(b)))
    elif c=='-':
       print("substraction:",(int(a)-int(b)))
    elif c=='*':
       print("multiplication:",(int(a)*int(b)))
    elif c=='%':
       print("modules:",(int(a)%int(b)))
    elif c=='/':
       print("division:",(int(a)/int(b)))
import cgi
print("content-type:text/html\n")
print("<html>")
print("<head> <title>My account CGI program</title>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("first")
b=form.getvalue("second")
c=form.getvalue("operation")
print('<form method="post" action="exp1.py">')
print('<p>Enter first number: <input type="text" name="first"/></p>')
print('<p>Enter second number: <input type="text" name="second"/></p>')
print('<p>Select operation:</p><select name="operation"><option>+</option><option>-</option><option>*</option><option>%</option><option>/</option>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('<br>')
print("</body>")
print("</html>")
calc(a,b,c)
