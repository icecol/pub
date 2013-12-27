import pymongo
import web
from web import form


render = web.template.render('templates/')

urls = (
	'/', 'Index',
	'/crud', 'Crud',
)

app = web.application(urls, globals())

login = form.Form(
    form.Textbox('Username'),
    form.Password('Password'),
    form.Button('Login'),
    validators = [form.Validator("Password error", lambda i: i.Username == i.Password)]
)


class Index:
    def GET(self):
	#conecta ao mongodb local
	client = pymongo.MongoClient('localhost', 27017)
	#define a base utilizada
	db = client.carscrud
        """ Show page """
        posts = db.cars.find()
	cars_list = []
	for i in posts:
	    cars_list.append(i)
	print cars_list

	# "decodifica unicode"
	cars = []
	for i in cars_list:
	    cars.append(dict([(str(k), str(v)) for k, v in i.items()]))
	print cars
        return render.index(cars)


class Crud:
    def GET(self):
	form = login()
	print form.render()
        return render.formtest(form)

    def POST(self): 
        form = login() 
	if form.validates():
            return "Grrreat success! user: %s, senha: %s" % (form.d.Username, form['Password'].value)
	else:
            return "ERROr! user: %s, senha: %s" % (form.d.Username, form['Password'].value)


if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
