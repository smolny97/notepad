from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def chenge_theme(theme):
	t_fild['bg'] = v_color[theme]['text_bg']
	t_fild['fg'] = v_color[theme]['text_fg']
	t_fild['insertbackground'] = v_color[theme]['cursor']
	t_fild['selectbackground'] = v_color[theme]['select_bg']

def chenge_fonts(fontss):
	t_fild['font'] = fonts[fontss]['font']

def notepad_exit():
	answer = messagebox.askokcancel('Выход','Вы точно хотите выйти?')
	if answer:
		root.destroy()

def open_file():
	f_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)','(*.txt)'),('Все файлы','*.*')))
	if f_path:
		t_fild.delete('1.0',END)
		t_fild.insert('1.0',open(f_path,encoding='utf-8').read())

def save_file():
	f_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)','(*.txt)'),('Все файлы','*.*')))
	f = open(f_path,'w',encoding='utf-8')
	text = t_fild.get('1.0',END)
	f.write(text)
	f.close()

root = Tk()
root.title("блокнот")
root.geometry('1920x1080')

m_menu = Menu(root)

f_menu = Menu(m_menu,tearoff=0)
f_menu.add_command(label='Открыть',command=open_file)
f_menu.add_command(label='Сохранить',command=save_file)
f_menu.add_separator()
f_menu.add_command(label='Закрыть',command=notepad_exit)
root.config(menu=f_menu)

v_menu = Menu(m_menu,tearoff=0)
v_menu_sub = Menu(v_menu,tearoff=0)
f_menu_sub = Menu(v_menu,tearoff=0)
v_menu_sub.add_command(label='Темная',command=lambda: chenge_theme('dark'))
v_menu_sub.add_command(label='Светлая',command=lambda: chenge_theme('light'))
v_menu.add_cascade(label='Тема', menu = v_menu_sub)

f_menu_sub.add_command(label='Arial',command=lambda: chenge_fonts('Arial'))
f_menu_sub.add_command(label='Times New Roman',command=lambda: chenge_fonts('TNR'))
f_menu_sub.add_command(label='Comic Sans MS',command=lambda: chenge_fonts('CMS'))
v_menu.add_cascade(label='Шрифт...', menu = f_menu_sub)
root.config(menu=v_menu)

m_menu.add_cascade(label='Файл', menu=f_menu)
m_menu.add_cascade(label='Вид', menu=v_menu)
root.config(menu=m_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH,expand=1)

v_color = {
	'dark':{
		'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
	},
	'light':{
		'text_bg': 'white', 'text_fg': 'black', 'cursor': 'black', 'select_bg': '#ccc'
	}
}

fonts = {
	'Arial':{
		'font': ('Arial',14)
	},
	'CMS':{
		'font': ('Comic Sans MS',14)
	},
	'TNR':{
		'font': ('Times New Roman',14)
	}
}

t_fild = Text(f_text,
	bg='white',
	fg='black',
	padx=10,
	pady=10,
	wrap=WORD,
	insertbackground='black',
	selectbackground='#ccc',
	spacing3=3,
	width=30,
	font='Arial 14'
	)

t_fild.pack(expand=1,fill=BOTH,side=LEFT)

scroll = Scrollbar(f_text,command=t_fild.yview)
scroll.pack(side=LEFT,fill=Y)
t_fild.config(yscrollcommand=scroll.set)

root.mainloop()
