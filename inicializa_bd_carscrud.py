#!/usr/bin/python

#Script de inicializcao da base de dados.
#Limpa e Insere registros de teste na base.
#27/12/2013

import pymongo

#conecta ao mongodb local
client = pymongo.MongoClient('localhost', 27017)
#define a base utilizada
db = client.carscrud
#limpa registros
db.drop_collection('cars')
#define a collection
cars = db.cars


#item a ser adicionado
new_car = {"ano": "2009",
	   "fabricante": "GM",
	   "modelo": "Vectra GT",
	   "foto": "fotoVectra.jpg"}
#insere novo item
car_id = cars.insert(new_car)
#item a ser adicionado
new_car = {"ano": "2010",
	   "fabricante": "VW",
	   "modelo": "GOL",
	   "foto": "fotoGol.jpg"}
#insere novo item
car_id = cars.insert(new_car)
#item a ser adicionado
new_car = {"ano": "2011",
	   "fabricante": "Ford",
	   "modelo": "Focus",
	   "foto": "fotoFocus.jpg"}
#insere novo item
car_id = cars.insert(new_car)
#item a ser adicionado
new_car = {"ano": "2012",
	   "fabricante": "GM",
	   "modelo": "Cruze",
	   "foto": "fotoCruze.jpg"}
#insere novo item
car_id = cars.insert(new_car)
#item a ser adicionado
new_car = {"ano": "2013",
	   "fabricante": "Ford",
	   "modelo": "Fusion",
	   "foto": "fotoFusion.jpg"}
#insere novo item
car_id = cars.insert(new_car)

#item a ser adicionado
new_car = {"ano": "2013",
	   "fabricante": "Ford",
	   "modelo": "Ecoesport",
	   "foto": "fotoEco01.jpg"}
#insere novo item
car_id = cars.insert(new_car)
#item a ser adicionado
new_car = {"ano": "2012",
	   "fabricante": "Ford",
	   "modelo": "Ecosport",
	   "foto": "fotoEco02.jpg"}
#insere novo item
car_id = cars.insert(new_car)
#item a ser adicionado
new_car = {"ano": "2011",
	   "fabricante": "Honda",
	   "modelo": "Civic",
	   "foto": "fotoCivic.jpg"}
#insere novo item
car_id = cars.insert(new_car)
#item a ser adicionado
new_car = {"ano": "2011",
	   "fabricante": "Honda",
	   "modelo": "Fit",
	   "foto": "fotoFit.jpg"}
#insere novo item
car_id = cars.insert(new_car)
#item a ser adicionado
new_car = {"ano": "2012",
	   "fabricante": "VW",
	   "modelo": "Tiguan",
	   "foto": "fotoTiguan.jpg"}
#insere novo item
car_id = cars.insert(new_car)

