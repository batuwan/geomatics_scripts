#This is a GUI experiment that calculates the distance between two points.

from tkinter import *
import tkinter.messagebox

class Distance:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.mid_frame1 = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.botbot_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame,
                   text='Enter X coordinate of 1st point:')
        self.x1_entry = tkinter.Entry(self.top_frame,
                                     width=10)
        self.prompt1_label = tkinter.Label(self.mid_frame,
                                              text='Enter Y coordinate of 1st point:')
        self.y1_entry = tkinter.Entry(self.mid_frame,
                                          width=10)
        self.prompt2_label = tkinter.Label(self.mid_frame1,
                                               text='Enter X coordinate of 2nd point:')
        self.x2_entry = tkinter.Entry(self.mid_frame1,
                                          width=10)
        self.prompt3_label = tkinter.Label(self.bottom_frame,
                                               text='Enter Y coordinate of 2nd point:')
        self.y2_entry = tkinter.Entry(self.bottom_frame,
                                          width=10)
        self.prompt_label.pack(side='left')
        self.x1_entry.pack(side='right')
        self.prompt1_label.pack(side='left')
        self.y1_entry.pack(side='right')
        self.prompt2_label.pack(side='left')
        self.x2_entry.pack(side='right')
        self.prompt3_label.pack(side='left')
        self.y2_entry.pack(side='right')
        self.descr_label = tkinter.Label(self.botbot_frame,
                                      text='Distance:')


        self.value = tkinter.StringVar()


        self.distance_label = tkinter.Label(self.botbot_frame,
                          textvariable=self.value)

        self.descr_label.pack(side='left')
        self.distance_label.pack(side='left')

        self.calc_button = tkinter.Button(self.botbot_frame,
                                       text='Convert',
                                       command=self.convert)
        self.quit_button = tkinter.Button(self.botbot_frame,
                                       text='Quit',
                                       command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.mid_frame1.pack()
        self.bottom_frame.pack()
        self.botbot_frame.pack()

        tkinter.mainloop()



    def convert(self):

        x1 = float(self.x1_entry.get())
        y1 = float(self.y1_entry.get())
        x2 = float(self.x2_entry.get())
        y2 = float(self.y2_entry.get())
        
        distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

        
        self.value.set(distance)


dist = Distance()
