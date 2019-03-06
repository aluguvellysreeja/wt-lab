#!C:\Program Files\Python37\python.exe
def sortstr(a):
    words=a.split()
    words.sort()
    print("The sorted words are:")
    for word in words:
        print(word)
import cgi
print("content-type:text/html\n")
print("<html>")
print("<head> <title>My account CGI program</title>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("first")
print('<form method="post" action="exp2.py">')
print('<p>Enter string: <input type="string" name="first"/></p>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('<br>')
print("</body>")
print("</html>")
sortstr(a)
