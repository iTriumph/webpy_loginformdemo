import web
import time
from web import form

render = web.template.render('templates/')

#define a login form
myLoginForm = form.Form(
    form.Textbox('username',
        form.notnull),
    form.Password('password'),
    form.Button('Login'),
)

urls = (
    '/', 'index',
    '/login', 'login',
)

class index:
    def GET(self):
        web.header('Content-type', 'text/html')
        web.header('Transfer-Encoding','chunked')
        #return '<BR/>more data from server with multiple return.'
        yield '<BR/>going to sleep 3 sec'
        time.sleep(3)
        yield  '<BR/>hello' 
        time.sleep(3)
        yield ' world'
        time.sleep(3)
        yield '<BR/>end.'
        #return 'end...'

class login:
    def GET(self):
        loginformdef = myLoginForm()
        return render.login(loginformdef)
    def POST(self):
        i = web.input()
        inputs = ''.join(['<BR/>', 'got input from post, user=',i.username, ', pwd=', i.password, '<BR/>'])
        return inputs
   
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

