from app import app 
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Thai'}
    return '''
<html>
    <head>
        <title>Home Page - Myblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''