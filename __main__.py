#!/usr/bin/python
import pymongo
import web
from web import form


render = web.template.render('templates/', base='layout')

urls = (
	'/', 'Index',
	'/crud', 'Crud',
)

app = web.application(urls, globals())

#formulario de login da area adm do crud
login = form.Form(
    form.Textbox('Username'),
    form.Password('Password'),
    form.Button('Login'),
    validators = [form.Validator("Password error", lambda i: i.Username == i.Password)]
)

#formulario de busca do CRUD
search = form.Form(
    form.Textbox('Fabricante'),
    form.Textbox('Modelo'),
    form.Textbox('Ano'),
    form.Button('Buscar'),
    validators = [form.Validator("Ano incorreto", lambda x: x.Ano < 9999)]
)

#funcao que busca registros de acordo com filtros do usuario, retorna lista
def filtra(db,filtros):
    #verifica se foi selecionado algum filtro
    filtro_values = 0
    for i in filtros.itervalues():
	if str(i):
	    filtro_values += 1
    #caso não tenha nenhum filtro, retorna lista completa
    if filtro_values == 0:
	busca = db.cars.find()
    else:
	busca = db.cars.find({'fabricante_lower':filtros['Fabricante'].lower()})
    r = []
    for i in busca:
	r.append(i)
    # "decodifica" unicode retornado pelo mongodb
    cars = []
    for i in r:
        cars.append(dict([(str(k), str(v)) for k, v in i.items()]))
    return cars


class Index:
    def GET(self):
	#conecta ao mongodb local
	client = pymongo.MongoClient('localhost', 27017)
	#define a base utilizada
	db = client.carscrud
	#busca registros na base e coloca em lista
        posts = db.cars.find()
	cars_list = []
	for i in posts:
	    cars_list.append(i)
	# "decodifica" unicode retornado pelo mongodb
	cars = []
	for i in cars_list:
	    cars.append(dict([(str(k), str(v)) for k, v in i.items()]))
	search_fields = search()
        return render.index(search_fields,cars)

    def POST(self):
	cars = []
	search_fields = search()
	if search_fields.validates():
	    return render.index(search_fields,cars)
	fabricante = search_fields['Fabricante'].value
	modelo = search_fields['Modelo'].value
	ano = search_fields['Ano'].value
	filtros = {'Fabricante':fabricante , 'Modelo':modelo , 'Ano':ano}
	#conecta ao mongodb local
        client = pymongo.MongoClient('localhost', 27017)
        #define a base utilizada
        db = client.carscrud
	cars = filtra(db,filtros)
	return render.index(search_fields,cars)


class Crud:
    def GET(self):
	form = login()
	print form.render()
        return render.login(form)

    def POST(self): 
        form = login() 
	if form.validates():
            return "Grrreat success! user: %s, senha: %s" % (form.d.Username, form['Password'].value)
	else:
            return "ERROr! user: %s, senha: %s" % (form.d.Username, form['Password'].value)


if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()

