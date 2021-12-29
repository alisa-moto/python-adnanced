from tkinter import *

from HW_12.book_store_oop.libs.constants import Parameters


class Front:
    def __init__(self):
        self.window = Tk()

    def __create_label(self, lable_text, lable_row=0, lable_column=0):
        new_label = Label(self.window, text=lable_text)
        new_label.grid(row=lable_row, column=lable_column)

    def create_front_lable(self, config_read, key):
        name = config_read.read_param(key, key)
        row = config_read.read_param(key, Parameters.ROW)
        column = config_read.read_param(key, Parameters.COLUMN)
        return self.__create_label(name, row, column)

    def create_entry(self, entry_row=0, entry_column=0):
        entry_text = StringVar()
        new_entry = Entry(self.window, textvariable=entry_text)
        new_entry.grid(row=entry_row, column=entry_column)

    def create_list_field(self, l_height=0, l_width=0, l_row=0, l_column=0, l_rowspan=0, l_columnspan=0):
        new_list = Listbox(self.window, height=l_height, width=l_width)
        new_list.grid(row=l_row, column=l_column, rowspan=l_rowspan, columnspan=l_columnspan)
        return new_list

    def create_button(self, button_text, button_width, command, button_row, button_column):
        new_button = Button(self.window, text=button_text, width=button_width, command=command)
        new_button.grid(row=button_row, column=button_column)

    def create_front_button(self, config_read, key=None, command=None):
        name = config_read.read_param(key, key)
        width = config_read.read_param(key, Parameters.WIDTH)
        row = config_read.read_param(key, Parameters.ROW)
        column = config_read.read_param(key, Parameters.COLUMN)
        return self.create_button(name, width, command, row, column)
