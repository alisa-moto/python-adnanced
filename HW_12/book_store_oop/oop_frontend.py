from tkinter import *

from HW_12.book_store_oop.сonfig_reader import ConfigReader
from oop_backend import Database
from base_frontend import Front
from HW_12.book_store_oop.libs.constants import TitlesAndLabels, DBname, Reader, Buttons

"""
This program stores book information as follows:
Title, Author, Year, ISBN

User can perform the next activities:
- View all records
- Search an entry
- Add entry
- Delete items
- Close the program
"""

database = Database(DBname.DB_NAME)
front = Front()
config_reader = ConfigReader(Reader.JSON_INI_FILE_NAME)


def view_command():
    main_list.delete(0, END)
    for row in database.view():
        main_list.insert(END, row)


def search_command():
    main_list.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        main_list.insert(END, row)


def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def delete_command():
    database.delete(selected_tuple[0])


def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def close_command():
    close = front.window.destroy
    return close


def get_selected_row(event):
    try:
        global selected_tuple
        if main_list.curselection():
            index = main_list.curselection()[0]
            selected_tuple = main_list.get(index)
            title_entry.delete(0, END)
            title_entry.insert(END, selected_tuple[1])
            author_entry.delete(0, END)
            author_entry.insert(END, selected_tuple[2])
            year_entry.delete(0, END)
            year_entry.insert(END, selected_tuple[3])
            isbn_entry.delete(0, END)
            isbn_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass


front.window.wm_title(TitlesAndLabels.MAIN_TITLE)  # refactor as it has to be a normal str

title_label = front.create_front_lable(config_reader, TitlesAndLabels.TITLE_LABEL)
author_label = front.create_front_lable(config_reader, TitlesAndLabels.AUTHOR_LABEL)
year_label = front.create_front_lable(config_reader, TitlesAndLabels.YEAR_LABEL)
isbn_label = front.create_front_lable(config_reader, TitlesAndLabels.ISBN_LABEL)

title_text = StringVar()
title_entry = Entry(front.window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(front.window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(front.window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(front.window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

main_list = front.create_list_field(6, 40, 2, 0, 6, 2)

ml_scroll_bar = Scrollbar(front.window)
ml_scroll_bar.grid(row=2, column=2, rowspan=6)

main_list.configure(yscrollcommand=ml_scroll_bar.set)
ml_scroll_bar.configure(command=main_list.yview)

main_list.bind('<<ListboxSelect>>', get_selected_row)

view_button = front.create_front_button(config_reader, Buttons.VIEW_BUTTON, view_command)
search_button = front.create_front_button(config_reader, Buttons.SEARCH_BUTTON, search_command)
add_button = front.create_front_button(config_reader, Buttons.ADD_BUTTON, add_command)
update_button = front.create_front_button(config_reader, Buttons.UPDATE_BUTTON, update_command)
delete_button = front.create_front_button(config_reader, Buttons.DELETE_BUTTON, delete_command)
# close_button = front.create_front_button(config_reader, Buttons.CLOSE_BUTTON, close_command)


if __name__ == '__main__':
    front.window.mainloop()
