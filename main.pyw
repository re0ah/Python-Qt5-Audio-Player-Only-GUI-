from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from functools import partial
import datetime
import os

#user libraries
from theme import *

def set_image(fname, obj, size):
	img = Image.open(fname)
	img = img.resize(size)
	photo = ImageTk.PhotoImage(img)
	obj.config(image=photo)
	obj.image=photo

class gui_authorization():
	height = (300)
	width  = (480)
	color_scheme = None
	fill_scheme = None

	def __init__(self):
		self.set_ui()
	
	def set_ui(self):
		self.set_window()
		self.set_top()
		self.set_mid()
		self.set_bot()
		self.set_scheme()
		self.set_style()

	root  = None
	title = ("Меню аккаунта")
	def set_window(self):
		self.root = Toplevel()
		self.root.geometry(str(self.width) + "x" + str(self.height))
		self.root.title(self.title)
		self.root.resizable(width=False, height=False)

	def set_scheme(self):
		self.color_scheme = theme.scheme["authorization"]

	def set_style(self):
		#см. класс theme, функция set_style насчет fill_scheme и color_scheme
		self.set_fill_scheme()
		theme.set_style(self.fill_scheme, self.color_scheme)

	def set_fill_scheme(self):
		#см. класс theme, функция set_style насчет fill_scheme
		self.fill_scheme = [self.root,
							self.top_frame,
							self.avatar_frame,
							self.avatar,
							self.info_frame,
							self.info_top_frame,
							self.name_lbl,
							self.date,
							self.action_menu,
							self.genres_frame,
							self.genres_lbl,
							self.genres_menu,
							self.groups_frame,
							self.groups_lbl,
							self.groups_menu,
							self.mid_frame,
							self.album_frame[0],
							self.album_frame[1],
							self.album_frame[2],
							self.album_frame[3],
							self.album_photo[0],
							self.album_photo[1],
							self.album_photo[2],
							self.album_photo[3],
							self.album_name[0],
							self.album_name[1],
							self.album_name[2],
							self.album_name[3],
							self.album_artist[0],
							self.album_artist[1],
							self.album_artist[2],
							self.album_artist[3],
							self.bottom_frame,
							self.wrap_bottom_btn[0],
							self.wrap_bottom_btn[1],
							self.wrap_bottom_btn[2],
							self.bottom_btn[0],
							self.bottom_btn[1],
							self.bottom_btn[2]
		]

	top_frame = None
	def set_top(self):
		self.top_frame = Frame(self.root)
		self.top_frame.pack(anchor=NW)
		self.set_avatar()
		self.set_info()
	
	avatar_frame = None
	avatar = None
	def set_avatar(self):
		self.avatar_frame = Frame(self.top_frame)
		self.avatar_frame.pack(side=LEFT,
							   padx=5,
							   pady=5)
		self.avatar = Label(self.avatar_frame)
		set_image("covers" + slash_path + "Black Sabbath - Vol. 4.jpeg",
				  self.avatar,
				  (100, 100))
		self.avatar.pack()

	info_frame = None
	info_top_frame = None
	name_lbl = None
	date = None
	def set_info(self):
		self.info_frame = Frame(self.top_frame)
		self.info_frame.pack(side=LEFT,
							 anchor=NW,
							 pady=(5, 0))
		#tmp_fr (временный фрейм) нужен чтобы объединить action_menu и name_lbl
		self.info_top_frame = Frame(self.info_frame)
		self.info_top_frame.pack(anchor=NW,
					pady=(0, 2))
		self.name_lbl = Label(self.info_top_frame,
							  text="Имя: re0ah",
							  font=("Arial", 12))
		self.name_lbl.pack(side=LEFT,
						   padx=(0, 175))
		self.set_action_menu()
		self.date = Label(self.info_frame,
						  text="Дата регистрации: " + str(datetime.date.today()),
						  font=("Arial", 12))
		self.date.pack(side=TOP,
					   anchor=NW,
					   pady=(0,2))
		self.set_genres()
		self.set_groups()

	action_menu = None
	action_select = None
	def set_action_menu(self):
		action_list = ["Действия",
					   "Выйти"]
		self.action_select = StringVar()
		self.action_select.set(action_list[0])
		self.action_menu = ttk.Combobox(self.info_top_frame,
									  	values=action_list,
										height=15,
										state="readonly",
										width=10,
										textvariable=self.action_select,
										font=("Arial", 12))
		self.action_menu.pack(side=LEFT,
							  anchor=NE)

	genres_frame = None
	genres_lbl = None
	genres_menu = None
	genres_select = None
	def set_genres(self):
		#Инициализация фрейма "Избранные жанры"
		self.genres_frame = Frame(self.info_frame)
		self.genres_frame.pack(anchor=NW)
		self.genres_lbl = Label(self.genres_frame,
								text="Избранные жанры: ",
								font=("Arial", 12))
		self.genres_lbl.pack(side=LEFT)
		genres_list = ["Сайкобилли",		  #0
					   "Психоделический рок", #1
					   "Панк-рок",			  #2
					   "Блюз",				  #3
					   "Блюз-рок",			  #4
					   "Рокабилли",			  #5
					   "Кантри",			  #6
					   "Рок-Н-Ролл",		  #7
					   "Джаз",				  #8
					   "Рок",				  #9
					   "Метал",				  #10
					   "Треш метал",		  #11
					   "Хэви метал"]		  #12
		#Инициализация селектора
		self.genres_select = StringVar()
		self.genres_select.set(genres_list[0])
		self.genres_menu = ttk.Combobox(self.genres_frame,
									  	values=genres_list,
										height=10,
										state="readonly",
										width=20,
						  				font=("Arial", 12),
										textvariable=self.genres_select)
		self.genres_menu.pack(side=LEFT, anchor=NW)

	groups_frame = None
	groups_lbl = None
	groups_menu = None
	groups_select = None
	def set_groups(self):
		#Инициализация фрейма "Избранные группы"
		self.groups_frame = Frame(self.info_frame)
		self.groups_frame.pack(anchor=NW)
		self.groups_lbl = Label(self.groups_frame,
								text="Избранные группы: ",
						  		font=("Arial", 12))
		self.groups_lbl.pack(side=LEFT,
							 anchor=S)
		groups_list = ["Accept", "AcϟDc", "Batmobile", "Beatles",
					   "Bee Gees", "Bill Haley", "Black Sabbath", "Blue Cats",
					   "Damage Done By Worms", "Dio", "D.O.A.", "Eden\'s Children",
					   "Elvis Presley", "Ghoultown", "Grateful Dead", "Guns N\' Roses",
					   "Happy Drivers", "Hipster Daddy-O", "Ink Spots", "Iron Maiden",
					   "Jefferson Airplane", "Jimi Hendrix", "Joan Jett And The Blackhearts", "Johnny Cash",
					   "Judas Priest", "King Crimson", "Kiss", "Led Zeppelin",
					   "Leftover Crack", "Louis Armstrong", "Mad Dog Cole", "Mad Heads",
					   "Mad Sin", "Manowar", "Megadeth", "Metallica",
					   "Misfits", "Morphine", "Motorhead", "Nautilus Pompilius",
					   "Nekromantix", "NOFX", "Ozzy Osbourne", "Paul Engemann",
					   "Pentagram", "Phluph", "Pink Floyd", "Pitmen",
					   "P. Paul Fenech", "Queen", "Raygun Cowboys", "Rise Against",
					   "Roy Orbison", "Sex Pistols", "Shakin' Guts", "Skitzo",
					   "Slayer", "Sniff \'n\' The Tears", "STINX", "Stray Cats",
					   "The Art Of Lovin\'", "The Caravans", "The Coffinshakers", "The Cramps",
					   "The Dazzlers", "The Doors", "The Epileptic Hillbilly\'s", "The Hillbilly Moon Explosion",
					   "The Hypnotunez", "The Meteors", "The Moody Blues", "The Moonshine Stalkers",
					   "The Peacocks", "The Radiacs", "The Rolling Stones", "The Sharks",
					   "The Statler Brothers", "The Tony Montanas", "The Troubled", "The Twilighters",

					   "Treat Her Right", "Volbeat", "W.A.S.P.", "WiseGuyz",
					   "Yes", "Виктор Салтыков", "Владимир Высоцкий", "Гражданская Оборона",
					   "ДДТ", "Кино", "Король и Шут", "Крематорий",
					   "Монгол Шуудан", "Сектор Газа", "Тимур Муцураев"
		]
		#Инициализация селектора
		self.groups_select = StringVar()
		self.groups_select.set(groups_list[0])
		self.groups_menu = ttk.Combobox(self.groups_frame,
									  	values=groups_list,
										height=10,
										state="readonly",
										width=20,
										textvariable=self.groups_select,
										font=("Arial", 12))
		self.groups_menu.pack(side=LEFT,
							  anchor=NW,
							  pady=(5, 0))
	
	mid_frame = None
	album_frame  = [None, None, None, None]
	album_photo  = [None, None, None, None]
	album_name   = [None, None, None, None]
	album_artist = [None, None, None, None]
	def set_mid(self):
		self.mid_frame = Frame(self.root)
		self.mid_frame.pack(pady=(5, 0), padx=5)
		photo_path = ["Eden\'s Children - Eden\'s Children.jpg",
					  "Jimi Hendrix - Are You Expirienced.jpg",
					  "The Doors - The Doors.jpg",
					  "Nekromantix - Curse Of The Coffin.jpg"]
		album_padx = [(20, 20), (0, 20), (0, 20), (0, 20)]
		album_pady = [(10, 5), (10, 5), (10, 5), (10, 5)]
		album_name = ["Eden\'s Ch...", "Are You...", "The Doors", "Curse Of..."]
		album_artist = ["Eden\'s Chi...", "Jimi Hendrix", "The Doors", "Nekromantix"]
		for i in range(len(self.album_frame)):
			self.album_frame[i] = Frame(self.mid_frame)
			self.album_frame[i].pack(side=LEFT,
									 anchor=NW,
									 padx=album_padx[i],
									 pady=album_pady[i])

			self.album_photo[i] = Label(self.album_frame[i])
			self.album_photo[i].pack()
			set_image("covers" + slash_path + photo_path[i],
				  	  self.album_photo[i],
				  	  (90, 90))
			#Название альбома
			self.album_name [i]  = Label(self.album_frame[i],
										 text=album_name[i],
										 font=("Arial", 12))
			self.album_name[i].pack()
			#Название исполнителя
			self.album_artist[i] = Label(self.album_frame[i],
										 text=album_artist[i],
										 font=("Arial", 11))
			self.album_artist[i].pack()

	bottom_frame = None
	wrap_bottom_btn = [None, None, None]
	bottom_btn = [None, None, None]
	def set_bot(self):
		self.bottom_frame = Frame(self.root)
		self.bottom_frame.pack(anchor=NE)
		def hover_enter_0(arg):
			self.bottom_btn[0]['bg'] = self.color_scheme["bottom_btn_0"]["activebackground"]
			self.bottom_btn[0]['fg'] = self.color_scheme["bottom_btn_0"]["activeforeground"]
		def hover_enter_1(arg):
			self.bottom_btn[1]['bg'] = self.color_scheme["bottom_btn_1"]["activebackground"]
			self.bottom_btn[1]['fg'] = self.color_scheme["bottom_btn_1"]["activeforeground"]
		def hover_enter_2(arg):
			self.bottom_btn[2]['bg'] = self.color_scheme["bottom_btn_2"]["activebackground"]
			self.bottom_btn[2]['fg'] = self.color_scheme["bottom_btn_2"]["activeforeground"]
		def hover_leave_0(arg):
			self.bottom_btn[0]['bg'] = self.color_scheme["bottom_btn_0"]["bg"]
			self.bottom_btn[0]['fg'] = self.color_scheme["bottom_btn_0"]["fg"]
		def hover_leave_1(arg):
			self.bottom_btn[1]['bg'] = self.color_scheme["bottom_btn_1"]["bg"]
			self.bottom_btn[1]['fg'] = self.color_scheme["bottom_btn_1"]["fg"]
		def hover_leave_2(arg):
			self.bottom_btn[2]['bg'] = self.color_scheme["bottom_btn_2"]["bg"]
			self.bottom_btn[2]['fg'] = self.color_scheme["bottom_btn_2"]["fg"]
		btn_text = ["Применить", "Сохранить", "Отменить"]
		hover_enter = [hover_enter_0,
					   hover_enter_1,
					   hover_enter_2]
		hover_leave = [hover_leave_0,
					   hover_leave_1,
					   hover_leave_2]
		for i in range(len(self.bottom_btn)):
			self.wrap_bottom_btn[i] = Frame(self.bottom_frame)
			self.wrap_bottom_btn[i].pack(side=LEFT)
			self.bottom_btn[i] = Button(self.wrap_bottom_btn[i],
									 	text=btn_text[i],
									 	font=("Arial", 11))
			#бинд на событие наведения на кнопку
			self.bottom_btn[i].bind("<Enter>", hover_enter[i])
			#бинд на событие снятия курсора с кнопки
			self.bottom_btn[i].bind("<Leave>", hover_leave[i])
			self.bottom_btn[i].pack()
		self.bottom_btn[1]["command"] = self.root.destroy

class gui_settings():
	height = (300)
	width  = (480)
	color_scheme = None
	fill_scheme = None

	def __init__(self):
		self.set_ui()

	def set_ui(self):
		self.set_scheme()
		self.set_fill_scheme()
		self.set_window()
		self.set_main_left()
		self.set_main_right()
		self.set_style()
	
	root  = None
	title = ("Настройки")
	def set_window(self):
		self.root = Toplevel()
		self.root.geometry(str(self.width) + "x" + str(self.height))
		self.root.title(self.title)
		self.root.resizable(width=False, height=False)

	def set_scheme(self):
		self.color_scheme = theme.scheme["settings"]

	def set_style(self):
		#см. класс theme, функция set_style насчет fill_scheme и color_scheme
		self.set_fill_scheme()
		theme.set_style(self.fill_scheme, self.color_scheme)

	def set_fill_scheme(self):
		#см. класс theme, функция set_style насчет fill_scheme
		self.fill_scheme = [self.root,
							self.left_master,
							self.itemlist_frame,
							self.itemlist_btn[0],
							self.itemlist_btn[1],
							self.itemlist_btn[2],
							self.item_scrollbar,
							self.itemlist_box,
							self.right_master,
							self.top_frame,
							self.network_frame,
							self.host_entry_frame,
							self.host_entry,
							self.host_label,
							self.port_entry_frame,
							self.port_entry,
							self.port_label,
							self.theme_frame,
							self.theme_scrollbar,
							self.theme_itemlist,
							self.equalizer_frame,
							self.equalizer_top_frame,
							self.equalizer_genres,
							self.equalizer_save_btn_frame,
							self.equalizer_save_btn,
							self.equalizer_bot_frame,
							self.equalizer_scale,
							self.equalizer_scale_lbl,
							self.equalizer_scale_frame,
							self.bottom_frame,
							self.wrap_bottom_bar_btn[0],
							self.bottom_bar_btn[0],
							self.wrap_bottom_bar_btn[1],
							self.bottom_bar_btn[1],
							self.wrap_bottom_bar_btn[2],
							self.bottom_bar_btn[2]
	]

	left_master = None
	def set_main_left(self):
		self.left_master = Frame(self.root,
								 width=200)
		self.left_master.pack(side=LEFT,
							  padx=10,
							  pady=10,
							  fill=Y)
		self.set_itemlist_bar()

	itemlist_frame = None
	itemlist_btn = [None, None, None]
	def set_itemlist_bar(self):
		self.itemlist_switch = IntVar()
		self.itemlist_switch.set(0) #0 is radio
		self.itemlist_frame = Frame(self.left_master,
									width=160,
									height=30)
		self.itemlist_frame.pack_propagate(0)
		self.itemlist_frame.pack()

		btn_text  = (["radio", "web", "locale"])
		btn_width = ([5, 4, 6])
		for i in range(len(btn_text)):
			self.itemlist_btn[i] = Radiobutton(self.itemlist_frame,
							  text=btn_text[i],
							  relief=RIDGE,
						  	  width=btn_width[i],
							  indicatoron=False,
							  font=("Arial", 13),
							  value=i,
							  variable=self.itemlist_switch,
							  command=self.switch_itemlist)
			self.itemlist_btn[i].pack(side=LEFT)
		self.set_scrollbar()

	item_scrollbar = None
	itemlist_box   = [None, None, None]
	def set_scrollbar(self):
		self.item_scrollbar = Scrollbar(self.left_master)
		self.item_scrollbar.pack(side=RIGHT, fill=Y)
		self.set_itemlists()
		self.switch_itemlist()

	radio_itemlist	= ["Горячие клавиши",
		 			   "Стили",
		 			   "Воспроизведение",
		 			   "Эквалайзер",
		 			   "Отображение"
	]
	web_itemlist	= radio_itemlist + ["Сеть"]
	locale_itemlist	= radio_itemlist
	itemlist		= [radio_itemlist,
					   web_itemlist,
					   locale_itemlist]
	def set_itemlists(self):
		for i in range(len(self.itemlist)):
			self.itemlist_box[i] = Listbox(self.left_master,
									   yscrollcommand=self.item_scrollbar.set,
									   height=20,
									   width=23
			)
			#Установка бинда на событие выбора item'a в listbox'e
			self.itemlist_box[i].bind("<<ListboxSelect>>", self.select_item)
		#Заполнение содержимого itemlist'ов
		for i in range(len(self.radio_itemlist)):
			self.itemlist_box[0].insert(END, self.radio_itemlist[i])
		for i in range(len(self.web_itemlist)):
			self.itemlist_box[1].insert(END, self.web_itemlist[i])
		for i in range(len(self.locale_itemlist)):
			self.itemlist_box[2].insert(END, self.locale_itemlist[i])

	itemlist_switch = None
	def switch_itemlist(self):
		tmp = self.itemlist_switch.get()
		self.itemlist_box[tmp].pack(side=LEFT, fill=BOTH)
		self.item_scrollbar.config(command=self.itemlist_box[tmp].yview)
		for i in range(len(self.itemlist)):
			if i != tmp:
				self.itemlist_box[i].pack_forget()

	right_master = None
	def set_main_right(self):
		self.right_master = Frame(self.root)
		self.right_master.pack(side=LEFT,
							   padx=(0,10),
							   pady=10,
							   fill=BOTH)
		self.set_bottom_frame()
		self.set_top_frame()

	top_frame = None
	def set_top_frame(self):
		self.top_frame = Frame(self.right_master)
		self.top_frame.pack(side=TOP, anchor=NW)
	
	network_frame = None
	host_entry_frame = None
	host_entry = None
	host_label = None
	port_entry_frame = None
	port_entry = None
	port_label = None
	def set_network_frame(self):
		self.network_frame = Frame(self.top_frame)
		self.network_frame.pack()
		
		#Инициализация host_entry фрейма
		self.host_entry_frame = Frame(self.network_frame)
		self.host_label = Label(self.host_entry_frame,
								text="Хост:  ")
		self.host_label.pack(side=LEFT)
		self.host_entry = Entry(self.host_entry_frame)
		self.host_entry.pack(side=LEFT)
		self.host_entry_frame.pack(side=TOP)

		#Инициализация port_entry фрейма
		self.port_entry_frame = Frame(self.network_frame)
		self.port_label = Label(self.port_entry_frame,
		 						text="Порт: ")
		self.port_label.pack(side=LEFT)
		self.port_entry = Entry(self.port_entry_frame)
		self.port_entry.pack(side=LEFT)
		self.port_entry_frame.pack(side=TOP)

		#Установка фрейма в фреймлист для его запаковки
		self.frame[1][5] = self.network_frame

	theme_frame = None
	theme_scrollbar = None
	theme_itemlist  = None
	theme_name = None
	def set_theme_frame(self):
		def accept_style():
			#Узнаем какой элемент выбран
			tmp = self.theme_itemlist.curselection()
			#Нужно обрабатывать ситуацию, когда никакой элемент не выбран
			if len(tmp) > 0:
				tmp = tmp[0]
				tmp = self.theme_name[tmp]
			else:
				return
			theme.set_scheme(tmp)
			gui_main.startmenu.set_scheme()
			gui_main.startmenu.set_style()
			self.set_scheme()
			self.set_style()
			gui_main.authorization.set_scheme()
			gui_main.authorization.set_style()
		def accept_style_and_exit():
			#Узнаем какой элемент выбран
			tmp = self.theme_itemlist.curselection()
			#Нужно обрабатывать ситуацию, когда никакой элемент не выбран
			if len(tmp) > 0:
				tmp = tmp[0]
				tmp = self.theme_name[tmp]
			else:
				self.root.destroy()
				return
			theme.set_scheme(tmp)
			gui_main.startmenu.set_scheme()
			gui_main.startmenu.set_style()
			self.set_scheme()
			self.set_style()
			if gui_main.authorization != None:
				gui_main.authorization.set_scheme()
				gui_main.authorization.set_style()
			self.root.destroy()
			gui_main.settings = None
		self.bottom_bar_btn[1].config(command=accept_style_and_exit) #Принять
		self.bottom_bar_btn[2].config(command=accept_style) #Применить
		self.theme_frame = Frame(self.top_frame)
		self.theme_frame.pack(anchor=NW)
		self.theme_itemlist = Listbox(self.theme_frame,
									  font=("Arial", 14))
		#Смотрим список файлов в папке themes, составляем список тем, строим itemlist
		self.theme_name = os.listdir("themes")
		item = []
		#Удаление расширения файла
		for i in range(len(self.theme_name)):
			item.append(self.theme_name[i].split('.')[0])
			self.theme_itemlist.insert(END, str(i + 1) + ". " + item[i])
		self.theme_itemlist.pack(side=LEFT)
		#Создание scrollbar'а
		self.theme_scrollbar = Scrollbar(self.theme_frame)
		self.theme_scrollbar.pack(side=RIGHT, fill=Y)
		self.theme_itemlist.config(yscrollcommand=self.theme_scrollbar.set)
		self.theme_scrollbar.config(command=self.theme_itemlist.yview)
		#Установка фрейма в фреймлист для его запаковки
		for i in range(len(self.frame)):
			self.frame[i][1] = self.theme_frame

	equalizer_frame = None
	equalizer_top_frame = None
	equalizer_genres = None
	equalizer_save_btn_frame = None
	equalizer_save_btn = None
	equalizer_bot_frame = None
	equalizer_scale = [None, None, None, None, None, None]
	equalizer_scale_lbl = [None, None, None, None, None, None]
	equalizer_scale_frame = [None, None, None, None, None, None]
	equalizer_select = None
	def set_equalizer_frame(self):
		self.equalizer_frame = Frame(self.top_frame)
		self.equalizer_frame.pack(side=LEFT, anchor=NW)

		#Инициализация верхнего фрейма
		self.equalizer_top_frame = Frame(self.equalizer_frame,
										 width=666,
										 height=30)
		#Этот фрейм обладает постоянными, неизменяемыми от содержимого размером
		self.equalizer_top_frame.pack_propagate(0)
		self.equalizer_top_frame.pack(anchor=NW)
		genres_list = ["Стандартный",		  #0
					   "Психоделический рок", #1
					   "Панк-рок",			  #2
					   "Блюз",				  #3
					   "Блюз-рок",			  #4
					   "Рокабилли",			  #5
					   "Кантри",			  #6
					   "Сайкобилли",		  #7
					   "Рок-Н-Ролл",		  #8
					   "Джаз",				  #9
					   "Рок",				  #10
					   "Метал",				  #11
					   "Треш метал",		  #12
					   "Хэви метал",		  #13
					   "Пользовательский"]	  #14
		#Инициализация селектора
		self.equalizer_select = StringVar()
		self.equalizer_select.set(genres_list[0])
		self.equalizer_genres = OptionMenu(self.equalizer_top_frame,
										   self.equalizer_select,
										   *genres_list)
		self.equalizer_genres.pack(side=LEFT, anchor=NW)
		#Создание кнопки "Сохранить"
		def hover_enter(arg):
			self.equalizer_save_btn['bg'] = self.color_scheme["equalizer_save_btn"]["activebackground"]
			self.equalizer_save_btn['fg'] = self.color_scheme["equalizer_save_btn"]["activeforeground"]
		def hover_leave(arg):
			self.equalizer_save_btn['bg'] = self.color_scheme["equalizer_save_btn"]["bg"]
			self.equalizer_save_btn['fg'] = self.color_scheme["equalizer_save_btn"]["fg"]
		self.equalizer_save_btn_frame = Frame(self.equalizer_top_frame)
		self.equalizer_save_btn_frame.pack(side=RIGHT, anchor=NE)
		self.equalizer_save_btn = Button(self.equalizer_save_btn_frame,
										 text="Сохранить")
		self.equalizer_save_btn.pack()
		#бинд на событие наведения на кнопку
		self.equalizer_save_btn.bind("<Enter>", hover_enter)
		#бинд на событие снятия курсора с кнопки
		self.equalizer_save_btn.bind("<Leave>", hover_leave)

		#Инициализация нижнего фрейма
		self.equalizer_bot_frame = Frame(self.equalizer_frame)
		self.equalizer_bot_frame.pack(anchor=NW, pady=50, padx=11)
		hz = ["64", "256", "1k", "4k", "16k", "64k"]
		for i in range(len(hz)):
			#Scale и Label хранятся в одном фрейме, которые распологаются слева направо
			self.equalizer_scale_frame[i] = Frame(self.equalizer_bot_frame)
			self.equalizer_scale_frame[i].pack(side=LEFT)
			self.equalizer_scale[i] = Scale(self.equalizer_scale_frame[i])
			self.equalizer_scale[i].pack(side=TOP)
			self.equalizer_scale_lbl[i] = Label(self.equalizer_scale_frame[i], text=hz[i])
			self.equalizer_scale_lbl[i].pack(side=TOP, anchor=NE)
		#Установка фрейма в фреймлист для его запаковки
		for i in range(len(self.frame)):
			self.frame[i][3] = self.equalizer_frame

	
	bottom_frame = None
	wrap_bottom_bar_btn = [None, None, None]
	bottom_bar_btn = [None, None, None]
	def set_bottom_frame(self):
		self.bottom_frame = Frame(self.right_master,
								  height=24,
								  width=500)
		self.bottom_frame.pack(side=BOTTOM)
		self.bottom_frame.pack_propagate(0)
		self.bottom_frame.pack()
		btn_width = [15, 6, 8] #Ширина кнопок в символах
		btn_text  = ["Сбросить настройки", "Принять", "Применить"]
		wrap_btn_style = [self.color_scheme["wrap_bottom_bar_btn_0"],
						  self.color_scheme["wrap_bottom_bar_btn_1"],
						  self.color_scheme["wrap_bottom_bar_btn_2"]]
		btn_style = [self.color_scheme["bottom_bar_btn_0"],
					 self.color_scheme["bottom_bar_btn_1"],
					 self.color_scheme["bottom_bar_btn_2"]]
		def hover_enter_0(arg):
			self.bottom_bar_btn[0]['bg'] = self.color_scheme["bottom_bar_btn_0"]["activebackground"]
			self.bottom_bar_btn[0]['fg'] = self.color_scheme["bottom_bar_btn_0"]["activeforeground"]
		def hover_enter_1(arg):
			self.bottom_bar_btn[1]['bg'] = self.color_scheme["bottom_bar_btn_1"]["activebackground"]
			self.bottom_bar_btn[1]['fg'] = self.color_scheme["bottom_bar_btn_1"]["activeforeground"]
		def hover_enter_2(arg):
			self.bottom_bar_btn[2]['bg'] = self.color_scheme["bottom_bar_btn_2"]["activebackground"]
			self.bottom_bar_btn[2]['fg'] = self.color_scheme["bottom_bar_btn_2"]["activeforeground"]
		def hover_leave_0(arg):
			self.bottom_bar_btn[0]['bg'] = self.color_scheme["bottom_bar_btn_0"]["bg"]
			self.bottom_bar_btn[0]['fg'] = self.color_scheme["bottom_bar_btn_0"]["fg"]
		def hover_leave_1(arg):
			self.bottom_bar_btn[1]['bg'] = self.color_scheme["bottom_bar_btn_1"]["bg"]
			self.bottom_bar_btn[1]['fg'] = self.color_scheme["bottom_bar_btn_1"]["fg"]
		def hover_leave_2(arg):
			self.bottom_bar_btn[2]['bg'] = self.color_scheme["bottom_bar_btn_2"]["bg"]
			self.bottom_bar_btn[2]['fg'] = self.color_scheme["bottom_bar_btn_2"]["fg"]
		hover_enter = [hover_enter_0,
					   hover_enter_1,
					   hover_enter_2]
		hover_leave = [hover_leave_0,
					   hover_leave_1,
					   hover_leave_2]
		for i in range(len(btn_text)):
			self.wrap_bottom_bar_btn[i] = Frame(self.bottom_frame)
			self.wrap_bottom_bar_btn[i].pack(side=LEFT)
			self.bottom_bar_btn[i] = Button(self.wrap_bottom_bar_btn[i],
						 height=2,
						 width=btn_width[i],
						 font=("Arial", 11),
						 text=btn_text[i])
			self.bottom_bar_btn[i].pack(side=LEFT)
			self.bottom_bar_btn[i].bind("<Enter>", hover_enter[i])
			self.bottom_bar_btn[i].bind("<Leave>", hover_leave[i])
		def destroy_window():
			self.root.destroy()
			gui_main.settings = None
		self.bottom_bar_btn[1]["command"] = destroy_window

	def dummy(self):
		#Заполнение пустым фреймом
		for i in range(len(self.frame)):
			self.frame[i][self.current_item] = Frame(self.top_frame)

	func_radio = [dummy,
				  set_theme_frame,
				  dummy,
				  set_equalizer_frame,
				  dummy]

	func_web = func_radio + [set_network_frame]

	func_locale = func_radio

	funclist = [func_radio,
				func_web,
				func_locale]

	frame_radio = [None,
				   theme_frame,
				   None,
				   None,
				   None,
				   None]

	frame_web = frame_radio + [network_frame]

	frame_locale = frame_radio

	frame = [frame_radio,
			 frame_web,
			 frame_locale]
	current_item_frame = None
	current_item = 0
	def select_item(self, event):
		print(self.current_item_frame)
		#Текущий выбранный list (radio, web или locale)
		cur_list = self.itemlist_switch.get()
		#Текущий выбранный item в текущем list'e
		self.current_item = self.itemlist_box[cur_list].curselection()
		#Нужно обрабатывать ситуацию, когда curselection возвращает пустой кортеж
		if len(self.current_item) > 0:
			self.current_item = self.current_item[0]
		else:
			return
		#Фреймы сменяются через pack_forget текущего && pack того который придет ему на смену
		#Если фрейм еще не был выбран, то этот момент пропускается
		if self.current_item_frame != None:
			self.current_item_frame.pack_forget()
		#Текущий фрейм, который должен быть показан
		self.current_item_frame = self.frame[cur_list][self.current_item]
		#Если выбранный фрейм еще не был создан, то перед тем как его запаковать его необходимо создать
		if self.current_item_frame == None:
			self.funclist[cur_list][self.current_item](self)
			self.current_item_frame = self.frame[cur_list][self.current_item]
		self.current_item_frame.pack()
		self.set_style()

class gui_startmenu():
	height = (600)
	width  = (480)
	def __init__(self, root):
		self.set_ui(root)
	root = None
	color_scheme = None
	fill_scheme = None
	def set_ui(self, root):
		self.set_scheme()
		self.set_root(root)
		self.set_bar()
		self.set_main_frame()
		self.set_style()

	def set_scheme(self):
		self.color_scheme = theme.scheme["startmenu"]	

	def set_style(self):
		#см. класс theme, функция set_style насчет fill_scheme и color_scheme
		self.set_fill_scheme()
		theme.set_style(self.fill_scheme, self.color_scheme)
		self.set_locale_switch_image()
		self.set_locale_btn_image()

	def set_fill_scheme(self):
		#см. класс theme, функция set_style насчет fill_scheme
		self.fill_scheme = [self.wrap_bar_btn[0],
					   		self.top_bar_btn[0],
					   		self.wrap_bar_btn[1],
					   		self.top_bar_btn[1],
					   		self.root,
					   		self.main_frame,
							self.top_main_frame,
					   		self.title,
					   		self.text_frame,
					   		self.text_frame_text,
							self.radio_frame,
							self.web_frame,
							self.locale_frame,
							self.locale_top_frame,
							self.locale_cover,
							self.locale_info_frame,
							self.locale_song_name,
							self.locale_control_frame,
							self.locale_wrapper_button[0],
							self.locale_wrapper_button[1],
							self.locale_wrapper_button[2],
							self.locale_wrapper_button[3],
							self.locale_button[0],
							self.locale_button[1],
							self.locale_button[2],
							self.locale_button[3],
							self.locale_song_scale_frame,
							self.locale_song_scale_wrapper,
							self.locale_song_scale,
							self.locale_song_lbl_now,
							self.locale_song_lbl_end,
							self.locale_song_volume_wrapper,
							self.locale_song_volume,
							self.locale_playlist_frame,
							self.locale_itemlist,
							self.locale_itemlist_scrollbar,
					   		self.bottom_bar,
					   		self.wrap_bottom_bar_btn[0],
					   		self.bottom_bar_btn[0],
					   		self.wrap_bottom_bar_btn[1],
					   		self.bottom_bar_btn[1],
					   		self.wrap_bottom_bar_btn[2],
					   		self.bottom_bar_btn[2]
		]

	def set_root(self, root):
		self.root = root
		self.root.geometry(str(self.width) + "x" + str(self.height))
		self.root.title("audio player by re0ah")
		self.root.resizable(width=False, height=False)

	top_bar_btn  = []
	wrap_bar_btn = []
	def set_bar(self):
		btn_text = (["Настройки", "Авторизация"])
		def open_settings():
			if gui_main.settings != None:
				return
			gui_main.settings = gui_settings()
		def open_authorization():
			gui_main.authorization = gui_authorization()

		#Написал, но осуждаю
		#Функции изменяющие стиль при наведении на кнопку и смена стиля соответственно когда курсор убираешь с кнопки
		def hover_settings_enter(arg):
			self.top_bar_btn[0]['bg'] = self.color_scheme["settings_btn"]["activebackground"]
			self.top_bar_btn[0]['fg'] = self.color_scheme["settings_btn"]["activeforeground"]
		def hover_settings_leave(arg):
			self.top_bar_btn[0]['bg'] = self.color_scheme["settings_btn"]["bg"]
			self.top_bar_btn[0]['fg'] = self.color_scheme["settings_btn"]["fg"]
		def hover_authorization_enter(arg):
			self.top_bar_btn[1]['bg'] = self.color_scheme["settings_btn"]["activebackground"]
			self.top_bar_btn[1]['fg'] = self.color_scheme["settings_btn"]["activeforeground"]
		def hover_authorization_leave(arg):
			self.top_bar_btn[1]['bg'] = self.color_scheme["settings_btn"]["bg"]
			self.top_bar_btn[1]['fg'] = self.color_scheme["settings_btn"]["fg"]
		fr = Frame(self.root)
		btn_func  = [open_settings, open_authorization]
		btn_style = [
		 		self.color_scheme["settings_btn"],
				self.color_scheme["authorization_btn"]
		]
		wrap_btn_style = [
		 		self.color_scheme["wrap_settings_btn"],
				self.color_scheme["wrap_authorization_btn"]
		]
		hover_enter = [hover_settings_enter,
					   hover_authorization_enter]
		hover_leave = [hover_settings_leave,
					   hover_authorization_leave]
		for i in range(len(btn_text)):
			btn_fr = Frame(fr)
			btn = Button(btn_fr,
						 font=("Arial", 11),
						 text=btn_text[i],
						 command=btn_func[i])
			#сохранение кнопки и ее обертки в списки для будущего к ним обращения (например при смене стиля)
			btn_fr.pack(side=LEFT)
			btn.pack(side=LEFT)

			self.wrap_bar_btn.append(btn_fr)
			self.top_bar_btn.append(btn)
			#бинд на событие наведения на кнопку
			self.top_bar_btn[i].bind("<Enter>", hover_enter[i])
			#бинд на событие снятия курсора с кнопки
			self.top_bar_btn[i].bind("<Leave>", hover_leave[i])
		fr.pack(side=TOP, anchor=W)
	
	main_frame = None
	top_main_frame = [None, #startmenu
					  None, #radio
					  None, #web
					  None] #locale
	RADIO 	  = 0
	WEB 	  = 1
	LOCALE 	  = 2
	STARTMENU = 3
	def set_main_frame(self):
		self.main_frame = Frame(self.root,
								width=self.width,
								height=self.height)
		#main_frame должен быть статичного размера
		self.main_frame.pack_propagate(0)
		self.main_frame.pack(side=LEFT, padx=10, pady=(15, 10))
		#top main frame будут сменяться при активации одного из режимов
		for i in range(len(self.top_main_frame)):
			self.top_main_frame[i] = Frame(self.main_frame)
			self.top_main_frame[i].pack()
		#Нужно проинициализировать фреймы, чтобы их можно было переключать
		for i in range(len(self.funclist)):
			self.funclist[i](self)
			self.top_main_frame[i].pack_forget()
		#В начале программы включается startmenu фрейм
		self.top_main_frame[self.STARTMENU].pack()
		self.set_bottom_bar()

	def set_startmenu(self):
		self.set_title()
		self.set_text_frame()

	title = None
	def set_title(self):
		self.title = Label(self.top_main_frame[self.STARTMENU],
						   text = "Стартовое меню",
						   font = ("Arial", 25)
		)
		self.title.pack(pady=5)

	text_frame = None
	text_frame_text = None
	def set_text_frame(self):
		self.text_frame = Frame(self.top_main_frame[self.STARTMENU])
		self.text_frame.pack(side=TOP)
		#К сожалению, не нашел способа написать данный фрагмент более изысканно и правильно. Я насчет вручную проставленных переносов строк. Дайте знать, если что, буду благодарен.
		text = ("Этот аудиоплеер поддерживает 3 режима работы:\n1. radio - поиск, прослушивание, добавление интернет\nрадиостанций. Все прослушанные песни сохраняются в\nистории, где после можно будет добавить их в cвой\nсписок аудиозаписей, который можно прослушать в\nрежиме web.\n\n2. web - поиск музыки в сети. Поддерживает составление\nплейлистов, которые будут храниться на сервере.\nПозволяет добавлять музыку, скачивать ее на диск.\n\nПервые 2 режима предназначены для работы с сетью\nинтернет, тогда как 3 режим, locale, предназначен для\nпрослушивания музыки с физического носителя.\n3. locale - создание плейлистов с помощью файлов\nнаходящихся на диске.\n\nВсе режимы поддерживают поиск по исполнителю,\nжанру, названию, году и прочим параметрам, позволяют\nсоставлять плейлисты (кроме radio, там можно составить\nсписок любимых радиостанций).")
		self.text_frame_text = Label(self.text_frame,
						 font=("Arial", 11),
						 justify=LEFT,
						 text=text)
		self.text_frame_text.pack(pady=(5, 48), padx=5)
	
	radio_frame = None
	def set_radio(self):
		self.radio_frame = Frame(self.top_main_frame[self.RADIO])
		self.radio_frame.pack()
		Label(self.radio_frame,
			  text="ТУТ ПУСТО",
			  fg="#FFFFFF",
			  bg="#141414",
			  font=("Arial", 50)).pack()

	web_frame = None
	def set_web(self):
		self.web_frame = Frame(self.top_main_frame[self.WEB])
		self.web_frame.pack()
		Label(self.web_frame,
			  text="И ТУТ ТОЖЕ\nПУСТО",
			  fg="#FFFFFF",
			  bg="#141414",
			  font=("Arial", 50)).pack()

	locale_frame = None
	def set_locale(self):
		self.locale_frame = Frame(self.top_main_frame[self.LOCALE],
								  width=self.width,
								  height=475)
		self.locale_frame.pack_propagate(0)
		self.locale_frame.pack()
		self.set_locale_top()
		self.set_locale_playlist()
	
	locale_top_frame = None
	def set_locale_top(self):
		self.locale_top_frame = Frame(self.locale_frame)
		self.locale_top_frame.pack()
		self.set_locale_cover()
		self.set_locale_info_frame()
		self.set_locale_song_volume()

	locale_cover = None
	def set_locale_cover(self):
		self.locale_cover = Label(self.locale_top_frame)
		self.locale_cover.pack(side=LEFT,
							   anchor=NE,
							   padx=5,
							   pady=5)
		set_image("covers" + slash_path + "Grateful Dead - Grateful Dead.jpg",
				  self.locale_cover,
				  (100, 100))
	
	locale_info_frame = None
	locale_song_name = None
	def set_locale_info_frame(self):
		self.locale_info_frame = Frame(self.locale_top_frame)
		self.locale_info_frame.pack(side=LEFT,
									pady=(5, 0),
									anchor=NW)
		self.locale_song_name = Label(self.locale_info_frame,
									  text="Grateful Dead - The Golden Road",
									  font=("Arial", 12),
									  )
		self.locale_song_name.pack(side=TOP, anchor=NW)
		self.set_locale_control_frame()
		self.set_locale_song_scale()

	locale_control_frame = None
	locale_wrapper_button = [None, None, None, None]
	locale_button = [None, None, None, None]
	locale_play_stop = False
	locale_photo_play_stop = [None, None]
	def set_locale_switch_image(self):
		photo_path = ["play.png", "pause.png"]
		for i in range(2):
			img = Image.open("themes" + slash_path + theme.scheme_dir + slash_path + photo_path[i])
			img = img.resize((25, 25))
			self.locale_photo_play_stop[i] = ImageTk.PhotoImage(img)
	locale_photo_btn = [None, None, None]
	def set_locale_btn_image(self):
		btn_path = ["themes" + slash_path + theme.scheme_dir + slash_path + "previous.png",
					"themes" + slash_path + theme.scheme_dir + slash_path + "play.png",
					"themes" + slash_path + theme.scheme_dir + slash_path + "next.png"]
		for i in range(len(btn_path)):
			img = Image.open(btn_path[i])
			img = img.resize((25, 25))
			self.locale_photo_btn[i] = ImageTk.PhotoImage(img)
			self.locale_button[i].config(image=self.locale_photo_btn[i])
			self.locale_button[i].image=self.locale_photo_btn[i]
	def set_locale_control_frame(self):
		def swap_button_pause_play():
			self.locale_play_stop = not self.locale_play_stop
			self.locale_button[1].config(image=self.locale_photo_play_stop[self.locale_play_stop])
			self.locale_button[1].image=self.locale_photo_play_stop[self.locale_play_stop]
		self.locale_control_frame = Frame(self.locale_info_frame)
		def next_song():
#	#Узнаем какой элемент выбран
#			tmp = self.locale_itemlist.curselection()
#			#Нужно обрабатывать ситуацию, когда никакой элемент не выбран
#			if len(tmp) > 0:
#				tmp = tmp[0]
#				print(tmp)
#				self.locale_itemlist.selection_set(tmp + 1)
#				tmp = self.locale_itemlist.curselection()
#				print(tmp)
#				self.locale_itemlist.event_generate("<<ListboxSelect>>")
#			else:
			return
		def previous_song():
#			#Узнаем какой элемент выбран
#			tmp = self.locale_itemlist.curselection()
#			#Нужно обрабатывать ситуацию, когда никакой элемент не выбран
#			if len(tmp) > 0:
#				tmp = tmp[0]
#				self.locale_itemlist.select_set(tmp - 1)
#			else:
			return
		self.locale_control_frame.pack(side=TOP,
									   anchor=NW,
									   pady=(5, 10))
		btn_command = [previous_song,
					   swap_button_pause_play,
					   next_song]
		btn_padx = [(0, 5), (0, 5), (0, 0)]
		for i in range(len(btn_command)):
			self.locale_wrapper_button[i] = Frame(self.locale_control_frame)
			self.locale_wrapper_button[i].pack(side=LEFT,
											   padx=btn_padx[i],
											   anchor=NW)
			self.locale_button[i] = Button(self.locale_wrapper_button[i],
										   command=btn_command[i])
			self.locale_button[i].pack()

		self.locale_wrapper_button[3] = Frame(self.locale_control_frame,
											  height=30,
											  width=105)
		self.locale_wrapper_button[3].pack_propagate(0)
		self.locale_wrapper_button[3].pack(side=LEFT,
										   padx=(80, 0))
		self.locale_button[3] = Button(self.locale_wrapper_button[3],
									   text="Перемешать",
									   font=("Arial", 12))
		self.locale_button[3].pack()
		def hover_enter_0(arg):
			self.locale_button[0]['bg'] = self.color_scheme["locale_button_0"]["activebackground"]
			self.locale_button[0]['fg'] = self.color_scheme["locale_button_0"]["activeforeground"]
		def hover_enter_1(arg):
			self.locale_button[1]['bg'] = self.color_scheme["locale_button_1"]["activebackground"]
			self.locale_button[1]['fg'] = self.color_scheme["locale_button_1"]["activeforeground"]
		def hover_enter_2(arg):
			self.locale_button[2]['bg'] = self.color_scheme["locale_button_2"]["activebackground"]
			self.locale_button[2]['fg'] = self.color_scheme["locale_button_2"]["activeforeground"]
		def hover_enter_3(arg):
			self.locale_button[3]['bg'] = self.color_scheme["locale_button_3"]["activebackground"]
			self.locale_button[3]['fg'] = self.color_scheme["locale_button_3"]["activeforeground"]
		def hover_leave_0(arg):
			self.locale_button[0]['bg'] = self.color_scheme["locale_button_0"]["bg"]
			self.locale_button[0]['fg'] = self.color_scheme["locale_button_0"]["fg"]
		def hover_leave_1(arg):
			self.locale_button[1]['bg'] = self.color_scheme["locale_button_1"]["bg"]
			self.locale_button[1]['fg'] = self.color_scheme["locale_button_1"]["fg"]
		def hover_leave_2(arg):
			self.locale_button[2]['bg'] = self.color_scheme["locale_button_2"]["bg"]
			self.locale_button[2]['fg'] = self.color_scheme["locale_button_2"]["fg"]
		def hover_leave_3(arg):
			self.locale_button[3]['bg'] = self.color_scheme["locale_button_3"]["bg"]
			self.locale_button[3]['fg'] = self.color_scheme["locale_button_3"]["fg"]
		hover_enter = [hover_enter_0,
					   hover_enter_1,
					   hover_enter_2,
					   hover_enter_3]
		hover_leave = [hover_leave_0,
					   hover_leave_1,
					   hover_leave_2,
					   hover_leave_3]
		for i in range(len(self.locale_button)):
			#бинд на событие наведения на кнопку
			self.locale_button[i].bind("<Enter>", hover_enter[i])
			#бинд на событие снятия курсора с кнопки
			self.locale_button[i].bind("<Leave>", hover_leave[i])

	locale_song_scale_frame = None
	locale_song_scale_wrapper = None
	locale_song_scale = None
	locale_song_lbl_now = None
	locale_song_lbl_end = None
	def set_locale_song_scale(self):
		self.locale_song_scale_frame = Frame(self.locale_info_frame)
		self.locale_song_scale_frame.pack(anchor=NW)
		self.locale_song_scale_wrapper = Frame(self.locale_song_scale_frame,
											 width=285,
											 height=14)
		self.locale_song_scale_wrapper.pack_propagate(0)
		self.locale_song_scale_wrapper.pack(anchor=NW)
		self.locale_song_scale = Scale(self.locale_song_scale_wrapper,
									   orient=HORIZONTAL,
									   showvalue=0)
		self.locale_song_scale.pack(fill=X)
		self.locale_song_lbl_now = Label(self.locale_song_scale_frame,
										 text="1:15",
									  	 font=("Arial", 12))
		self.locale_song_lbl_now.pack(side=LEFT,
									  anchor=NW)
		self.locale_song_lbl_end = Label(self.locale_song_scale_frame,
										 text="2:31",
									  	 font=("Arial", 12))
		self.locale_song_lbl_end.pack(side=RIGHT,
									  anchor=NE)

	locale_song_volume_wrapper = None
	locale_song_volume = None
	def set_locale_song_volume(self):
		self.locale_song_volume_wrapper = Frame(self.locale_top_frame,
												width=40,
												height=100)
		self.locale_song_volume_wrapper.pack_propagate(0)
		self.locale_song_volume_wrapper.pack(side=LEFT,
											 padx=(10, 0),
											 pady=(5, 0),
											 anchor=NE)
		self.locale_song_volume = Scale(self.locale_song_volume_wrapper)
		self.locale_song_volume.pack()
	
	locale_playlist_frame = None
	locale_itemlist = None
	locale_itemlist_scrollbar = None
	playlist = ["The Golden Road",
				"Beat It On Down The Line",
				"Good Morning Little School Girl",
				"Cold Rain and Snow",
				"Sitting on Top of the World",
				"Cream Puff War",
				"Morning Dew",
				"New New Minglewood Blues",
				"Viola Lee Blues"]
	def set_locale_playlist(self):
		self.locale_playlist_frame = Frame(self.locale_frame)
		self.locale_playlist_frame.pack(side=BOTTOM,
										anchor=NW,
										padx=(0, 20))
		self.locale_itemlist_scrollbar = Scrollbar(self.locale_playlist_frame)
		self.locale_itemlist_scrollbar.pack(side=RIGHT, fill=Y)
		self.locale_itemlist = Listbox(self.locale_playlist_frame,
									   yscrollcommand=self.locale_itemlist_scrollbar.set,
									   height=14,
									   font=("Arial", 15),
									   width=100)
		self.locale_itemlist.pack(side=LEFT,
								  anchor=NE,
								  padx=(20, 0))
		#Установка бинда на событие выбора item'a в listbox'e
		#Заполнение содержимого itemlist'ов
		for i in range(len(self.playlist)):
			self.locale_itemlist.insert(END, str(i + 1) + ". " + self.playlist[i])
		self.locale_itemlist.bind("<<ListboxSelect>>", self.locale_select_item)
		self.locale_itemlist.select_set(0)
		self.locale_itemlist.event_generate("<<ListboxSelect>>")

	def locale_select_item(self, event):
		#Узнаем какой элемент выбран
		tmp = self.locale_itemlist.curselection()
		#Нужно обрабатывать ситуацию, когда никакой элемент не выбран
		if len(tmp) > 0:
			tmp = tmp[0]
			text = "Grateful Dead - " + self.playlist[tmp]
			if len(text) > 34:
				text = text[:-(len(text) - 34)] + "..."
			self.locale_song_name["text"] = text
		else:
			return

	itemlist_switch = None
	def switch_itemlist(self):
		tmp = self.itemlist_switch.get()
		self.itemlist_box[tmp].pack(side=LEFT, fill=BOTH)
		self.item_scrollbar.config(command=self.itemlist_box[tmp].yview)

	bottom_bar     		= None
	wrap_bottom_bar_btn = [None, None, None]
	bottom_bar_btn 		= [None, None, None]
	mod_select = None
	def set_bottom_bar(self):
		self.bottom_bar = Frame(self.main_frame,
				   height=50,
				   width=self.width,
				   bg="#141414"
		)
		self.bottom_bar.pack_propagate(0)
		self.bottom_bar.pack(pady=10, side=BOTTOM)
		#Написал, но осуждаю
		#Функции изменяющие стиль при наведении на кнопку и смена стиля соответственно когда курсор убираешь с кнопки
		def hover_radio_enter(arg):
			self.bottom_bar_btn[0]['bg'] = self.color_scheme["btn_radio"]["activebackground"]
			self.bottom_bar_btn[0]['fg'] = self.color_scheme["btn_radio"]["activeforeground"]
		def hover_radio_leave(arg):
			self.bottom_bar_btn[0]['bg'] = self.color_scheme["btn_radio"]["bg"]
			self.bottom_bar_btn[0]['fg'] = self.color_scheme["btn_radio"]["fg"]
		def hover_web_enter(arg):
			self.bottom_bar_btn[1]['bg'] = self.color_scheme["btn_web"]["activebackground"]
			self.bottom_bar_btn[1]['fg'] = self.color_scheme["btn_web"]["activeforeground"]
		def hover_web_leave(arg):
			self.bottom_bar_btn[1]['bg'] = self.color_scheme["btn_web"]["bg"]
			self.bottom_bar_btn[1]['fg'] = self.color_scheme["btn_web"]["fg"]
		def hover_locale_enter(arg):
			self.bottom_bar_btn[2]['bg'] = self.color_scheme["btn_locale"]["activebackground"]
			self.bottom_bar_btn[2]['fg'] = self.color_scheme["btn_locale"]["activeforeground"]
		def hover_locale_leave(arg):
			self.bottom_bar_btn[2]['bg'] = self.color_scheme["btn_locale"]["bg"]
			self.bottom_bar_btn[2]['fg'] = self.color_scheme["btn_locale"]["fg"]
		#2 списка содержащие объявленные выше функции
		hover_enter = [hover_radio_enter,
					   hover_web_enter,
					   hover_locale_enter]
		hover_leave = [hover_radio_leave,
					   hover_web_leave,
					   hover_locale_leave]
		#инициализация селектора
		self.mod_select = IntVar()
		self.mod_select.set(3) #нужно чтобы ни один из режимов не был активирован в самом начале, кнопок 3 и поэтому число 3 подходит, так как не вмещается в диапозон
		btn_padx  = [10, 0, 10]  #Внешние отступы блоков
		btn_width = [10, 10, 11] #Ширина кнопок в символах
		btn_text  = ["Radio mode", "Web mode", "Locale mode"]
		for i in range(len(btn_padx)):
			self.wrap_bottom_bar_btn[i] = Frame(self.bottom_bar)
			self.wrap_bottom_bar_btn[i].pack(side=LEFT,
											 padx=btn_padx[i])
			self.bottom_bar_btn[i] = Radiobutton(self.wrap_bottom_bar_btn[i],
						 	  					 height=2,
						 	  					 width=btn_width[i],
						 	  					 font=("Arial", 17),
						 	  					 text=btn_text[i],
							  					 relief=RIDGE,
							  					 indicatoron=False,
							  					 value=i,
							  					 variable=self.mod_select,
												 command=self.choose_mod)
			self.bottom_bar_btn[i].pack()
			#бинд на событие наведения на кнопку
			self.bottom_bar_btn[i].bind("<Enter>", hover_enter[i])
			#бинд на событие снятия курсора с кнопки
			self.bottom_bar_btn[i].bind("<Leave>", hover_leave[i])

	funclist = [set_startmenu,
				set_radio,
				set_web,
				set_locale]
	def choose_mod(self):
		for i in self.top_main_frame:
			i.pack_forget()
		self.top_main_frame[self.mod_select.get()].pack()

#Класс необходимый для хранения всех остальных классов и обеспечить межклассовое взаимодействие
#Был создан просто чтобы из класса settings иметь доступ к остальным классам для смены их цветовой темы. Ну, может еще для чего-то понадобится
class gui_main():
	root 	  = None
	startmenu = None
	#Все остальные классы присваиваются косвенно в других классах, но этому.
	settings  = None
	authorization = None
	def set(root):
		gui_main.root = root
		scheme = theme.set_default_theme()
		gui_main.startmenu = gui_startmenu(gui_main.root)
		gui_main.root.mainloop()

root = Tk()
gui_main.set(root)
