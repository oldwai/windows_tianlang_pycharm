#coding:utf-8


from pywinauto.application import Application
# Run a target application
app = Application().start("notepad2.exe")
# Select a menu item
app.UntitledNotepad.menu_select("?->About")
# Click on a button
app.AboutNotepad.OK.click()
# Type a text string
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
