import json
import os

if os.name == "nt": #windows
	slash_path = '\\'
else:
	slash_path = '/'#unix

class theme():
#Текущая цветовая схема
	scheme = {}
	scheme_dir = ""
#Функция принимает один из основных ключей интерфейса: "startmenu", "settings", "authorization"...
	def set_default_theme():
		#Смотрится текущая тема в файле themes.json
		with open("themes.json", "r") as read_file:
			data = json.load(read_file)
		theme.scheme_dir = data["current"]
		#dir/color_scheme.json
		theme.set_scheme(theme.scheme_dir)

	def set_scheme(filename):
		#Находим и парсим необходимый .json файл
		theme_path = "themes" + slash_path + filename + slash_path + "color_scheme.json"
		with open(theme_path, "r") as read_file:
			theme.scheme = json.load(read_file)

	def set_style(fill_scheme, color_scheme):
		for item in range(len(fill_scheme)):
			#Получение списка ключей конкретного элемента
			tmp = list(color_scheme.keys())[item]
			for style in color_scheme[tmp]:
				#Проверка на то, является ли элемент списком
				if type(fill_scheme[item]) == list:
					#Присвоение стиля каждому из элементов
					for i in range(len(fill_scheme[item])):
						if fill_scheme[item][i] != None:
							fill_scheme[item][i][style] = color_scheme[tmp][style]
				#Проверка на то, инициализирован ли элемент схемы
				elif fill_scheme[item] != None:
					fill_scheme[item][style] = color_scheme[tmp][style]
