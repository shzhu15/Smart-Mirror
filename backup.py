#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 05, 2018 07:48:56 PM CST  platform: Windows NT

import sys

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

try:
	import ttk
	py3 = False
except ImportError:
	import tkinter.ttk as ttk
	py3 = True

import unknown_support
import datetime

the_date = ''

def vp_start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = tk.Tk()
	top = GUI (root)
	unknown_support.init(root, top)
	root.mainloop()

w = None
def create_GUI(root, *args, **kwargs):
	'''Starting point when module is imported by another program.'''
	global w, w_win, rt
	rt = root
	w = tk.Toplevel (root)
	top = GUI (w)
	unknown_support.init(w, top, *args, **kwargs)
	return (w, top)

def destroy_GUI():
	global w
	w.destroy()
	w = None

class GUI(tk.Frame):
	def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		font15 = "-family {Segoe UI} -size 18 -weight normal -slant "  \
			"roman -underline 0 -overstrike 0"
		font27 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
			"roman -underline 0 -overstrike 0"
		font28 = "-family {Segoe UI Black} -size 18 -weight bold "  \
			"-slant roman -underline 0 -overstrike 0"
		font29 = "-family {Segoe UI} -size 30 -weight normal -slant "  \
			"roman -underline 0 -overstrike 0"
		font30 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
			"roman -underline 0 -overstrike 0"
		font32 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
			"roman -underline 0 -overstrike 0"

		top.geometry("900x1600+304+0")
		top.title("New Toplevel")
		top.configure(background="#000000")

		self.Time_Time = tk.Label(top)
		self.Time_Time.place(relx=0.744, rely=0.531, height=41, width=230)
		self.Time_Time.configure(activebackground="#000000")
		self.Time_Time.configure(activeforeground="white")
		self.Time_Time.configure(activeforeground="#000000")
		self.Time_Time.configure(background="#000000")
		self.Time_Time.configure(compound="center")
		self.Time_Time.configure(disabledforeground="#000000")
		self.Time_Time.configure(font=font29)
		self.Time_Time.configure(foreground="#ffffff")
		self.Time_Time.configure(highlightbackground="#000000")
		self.Time_Time.configure(highlightcolor="#646464")
		# self.Time_Time.configure(text='''00:00:00 AM''')
		self.Time_Time.configure(width=230)

		self.Time_Date = tk.Label(top)
		self.Time_Date.place(relx=0.756, rely=0.556, height=41, width=210)
		self.Time_Date.configure(activebackground="#000000")
		self.Time_Date.configure(activeforeground="white")
		self.Time_Date.configure(activeforeground="#000000")
		self.Time_Date.configure(background="#000000")
		self.Time_Date.configure(compound="center")
		self.Time_Date.configure(disabledforeground="#000000")
		self.Time_Date.configure(font=font29)
		self.Time_Date.configure(foreground="#ffffff")
		self.Time_Date.configure(highlightbackground="#000000")
		self.Time_Date.configure(highlightcolor="#646464")
		self.Time_Date.configure(text='''12/05/2018''')
		self.Time_Date.configure(width=210)

		self.CalendarDay_1 = tk.Label(top)
		self.CalendarDay_1.place(relx=0.0, rely=0.75, height=41, width=300)
		self.CalendarDay_1.configure(background="#000000")
		self.CalendarDay_1.configure(disabledforeground="#a3a3a3")
		self.CalendarDay_1.configure(font=font28)
		self.CalendarDay_1.configure(foreground="#ffffff")
		self.CalendarDay_1.configure(highlightbackground="#f0f0f0")
		self.CalendarDay_1.configure(text='''Calendar Day 1''')
		self.CalendarDay_1.configure(width=300)

		self.CalendarDay_2 = tk.Label(top)
		self.CalendarDay_2.place(relx=0.333, rely=0.75, height=41, width=300)
		self.CalendarDay_2.configure(activebackground="#f9f9f9")
		self.CalendarDay_2.configure(activeforeground="black")
		self.CalendarDay_2.configure(background="#000000")
		self.CalendarDay_2.configure(disabledforeground="#a3a3a3")
		self.CalendarDay_2.configure(font=font28)
		self.CalendarDay_2.configure(foreground="#ffffff")
		self.CalendarDay_2.configure(highlightbackground="#d9d9d9")
		self.CalendarDay_2.configure(highlightcolor="black")
		self.CalendarDay_2.configure(text='''Calendar Day 2''')
		self.CalendarDay_2.configure(width=300)

		self.CalendarDay_3 = tk.Label(top)
		self.CalendarDay_3.place(relx=0.667, rely=0.75, height=41, width=300)
		self.CalendarDay_3.configure(activebackground="#f9f9f9")
		self.CalendarDay_3.configure(activeforeground="black")
		self.CalendarDay_3.configure(background="#000000")
		self.CalendarDay_3.configure(disabledforeground="#a3a3a3")
		self.CalendarDay_3.configure(font=font28)
		self.CalendarDay_3.configure(foreground="#ffffff")
		self.CalendarDay_3.configure(highlightbackground="#d9d9d9")
		self.CalendarDay_3.configure(highlightcolor="black")
		self.CalendarDay_3.configure(text='''Calendar Day 3''')
		self.CalendarDay_3.configure(width=300)

		self.CalendarDayEvents_1 = tk.Listbox(top)
		self.CalendarDayEvents_1.place(relx=0.0, rely=0.775, relheight=0.226
				, relwidth=0.333)
		self.CalendarDayEvents_1.configure(background="#000000")
		self.CalendarDayEvents_1.configure(disabledforeground="#a3a3a3")
		self.CalendarDayEvents_1.configure(font=font27)
		self.CalendarDayEvents_1.configure(foreground="#ffffff")
		self.CalendarDayEvents_1.configure(relief='flat')
		self.CalendarDayEvents_1.configure(width=300)

		self.CalendarDayEvents_2 = tk.Listbox(top)
		self.CalendarDayEvents_2.place(relx=0.333, rely=0.775, relheight=0.226
				, relwidth=0.333)
		self.CalendarDayEvents_2.configure(background="#000000")
		self.CalendarDayEvents_2.configure(disabledforeground="#a3a3a3")
		self.CalendarDayEvents_2.configure(font=font27)
		self.CalendarDayEvents_2.configure(foreground="#ffffff")
		self.CalendarDayEvents_2.configure(highlightbackground="#d9d9d9")
		self.CalendarDayEvents_2.configure(highlightcolor="black")
		self.CalendarDayEvents_2.configure(relief='flat')
		self.CalendarDayEvents_2.configure(selectbackground="#c4c4c4")
		self.CalendarDayEvents_2.configure(selectforeground="black")
		self.CalendarDayEvents_2.configure(width=300)

		self.CalendarDayEvents_3 = tk.Listbox(top)
		self.CalendarDayEvents_3.place(relx=0.667, rely=0.775, relheight=0.226
				, relwidth=0.333)
		self.CalendarDayEvents_3.configure(background="#000000")
		self.CalendarDayEvents_3.configure(disabledforeground="#a3a3a3")
		self.CalendarDayEvents_3.configure(font=font27)
		self.CalendarDayEvents_3.configure(foreground="#ffffff")
		self.CalendarDayEvents_3.configure(highlightbackground="#d9d9d9")
		self.CalendarDayEvents_3.configure(highlightcolor="black")
		self.CalendarDayEvents_3.configure(relief='flat')
		self.CalendarDayEvents_3.configure(selectbackground="#c4c4c4")
		self.CalendarDayEvents_3.configure(selectforeground="black")
		self.CalendarDayEvents_3.configure(width=300)

		self.News_SectionTitle = tk.Label(top)
		self.News_SectionTitle.place(relx=0.667, rely=0.038, height=31
				, width=304)
		self.News_SectionTitle.configure(background="#000000")
		self.News_SectionTitle.configure(disabledforeground="#a3a3a3")
		self.News_SectionTitle.configure(font=font15)
		self.News_SectionTitle.configure(foreground="#ffffff")
		self.News_SectionTitle.configure(highlightcolor="#ffffff")
		self.News_SectionTitle.configure(highlightthickness="1")
		self.News_SectionTitle.configure(text='''News''')
		self.News_SectionTitle.configure(width=304)

		self.News_Stories = tk.Listbox(top)
		self.News_Stories.place(relx=0.667, rely=0.056, relheight=0.294
				, relwidth=0.333)
		self.News_Stories.configure(background="#000000")
		self.News_Stories.configure(disabledforeground="#a3a3a3")
		self.News_Stories.configure(font=font30)
		self.News_Stories.configure(foreground="#ffffff")
		self.News_Stories.configure(highlightthickness="0")
		self.News_Stories.configure(relief='flat')
		self.News_Stories.configure(width=300)

		self.Weather_Icon = tk.Label(top)
		self.Weather_Icon.place(relx=0.067, rely=0.119, height=51, width=84)
		self.Weather_Icon.configure(background="#000000")
		self.Weather_Icon.configure(disabledforeground="#a3a3a3")
		self.Weather_Icon.configure(foreground="#ffffff")
		self._img1 = tk.PhotoImage(file="./Icons/cloudy.png")
		self.Weather_Icon.configure(image=self._img1)
		self.Weather_Icon.configure(justify='left')
		self.Weather_Icon.configure(text='''Label''')
		self.Weather_Icon.configure(width=84)

		self.Weather_Temperature = tk.Label(top)
		self.Weather_Temperature.place(relx=0.156, rely=0.119, height=51
				, width=79)
		self.Weather_Temperature.configure(background="#000000")
		self.Weather_Temperature.configure(disabledforeground="#a3a3a3")
		self.Weather_Temperature.configure(font=font29)
		self.Weather_Temperature.configure(foreground="#ffffff")
		self.Weather_Temperature.configure(text='''28 F''')
		self.Weather_Temperature.configure(width=79)

		self.Weather_HighLow = tk.Label(top)
		self.Weather_HighLow.place(relx=0.044, rely=0.15, height=21, width=101)
		self.Weather_HighLow.configure(background="#000000")
		self.Weather_HighLow.configure(disabledforeground="#a3a3a3")
		self.Weather_HighLow.configure(font=font32)
		self.Weather_HighLow.configure(foreground="#ffffff")
		self.Weather_HighLow.configure(text='''39  / 18''')
		self.Weather_HighLow.configure(width=74)

		self.Weather_FeelsLike = tk.Label(top)
		self.Weather_FeelsLike.place(relx=0.156, rely=0.15, height=21, width=101)

		self.Weather_FeelsLike.configure(background="#000000")
		self.Weather_FeelsLike.configure(disabledforeground="#a3a3a3")
		self.Weather_FeelsLike.configure(font=font32)
		self.Weather_FeelsLike.configure(foreground="#ffffff")
		self.Weather_FeelsLike.configure(text='''Feels Like 21''')
		self.Weather_FeelsLike.configure(width=101)

		self.create_widgets()

	def create_widgets(self):
		def clock():
			global the_date
			the_date = datetime.datetime.now().strftime("%H:%M:%S")
			self.Time_Time.config(text=the_date)
			self.Time_Time.after(1000, clock)  # run itself again after 1000 ms


if __name__ == '__main__':
	vp_start_gui()





