import webbrowser

f = open('index.html', 'w')

message = """<!DOCTYPE HTML>

<html>
<head><title> FBX Viewer </title></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('index.html')