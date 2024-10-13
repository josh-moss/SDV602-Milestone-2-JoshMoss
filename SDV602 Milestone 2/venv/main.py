import PySimpleGUI as sg
from windows.MainWindow import MainWindow
from windows.SubWindow import SubWindow

#-------------------------------        TODO            -------------------------------
#-------------------------------  CREATE LOGIN WINDOW   -------------------------------
#------------------------------- DERIVED SIGNUP WINDOW  -------------------------------
#-------------------------------    CHART DICTONARY     -------------------------------
#-------------------------------      CSV READER        -------------------------------
#-------------------------------    Error Handling      -------------------------------
#-------------------------------   GUI Button Events    -------------------------------
#-------------------------------   Login Validation?    -------------------------------
#-------------------------------    Tweak UI Layout     -------------------------------




#------------------------------- MAIN CLASS FOR DES APP -------------------------------

class Main:
    def __init__(self):
        self.main_window = MainWindow()
        self.window_2 = SubWindow("Window 2")
        self.window_3 = SubWindow("Window 3")
        
        self.windows = {
            "main_window": {"window": self.main_window.get_window(), "hidden": False},
            "window_2": {"window": self.window_2.get_window(), "hidden": True},
            "window_3": {"window": self.window_3.get_window(), "hidden": True}
        }
        
        self.charts = {
            #future dict to track charts? can use this to enumerate though each chart index using next and previous evennt clicks?
        }
    
        self.chat_history = []
        

#------------------------------- CLASS METHODS -------------------------------

    #rhis method concatenates the chat history stored in the list and updates the chat display in alll windows that are NOT hidden
    def update_chat(self):
        display_chat = ''.join(self.chat_history)
        
        for key, value in self.windows.items():
            
            #check the windows hidden state
            if not value["hidden"]:
                value["window"]["-CHAT-"].update(display_chat)
        
        
#------------------------------- EVENTS -------------------------------

    def DesApp(self):
        while True:
            window, event, values = sg.read_all_windows()
            
            if event in (sg.WIN_CLOSED, "Exit"):
                break

            if event == "Send":
                message = values["-MESSAGE-"].strip()
                self.chat_history.append(f"User: {message}\n")
                self.update_chat()
                
            if event == "-SHOW_2-":
                self.window_2.toggle_visibility(self.windows["window_2"])
                
            elif event == "-SHOW_3-":
                self.window_3.toggle_visibility(self.windows["window_3"])
                
            elif event == "-HIDE-":
                if window == self.window_2.get_window():
                    self.window_2.toggle_visibility(self.windows["window_2"])
                    
                elif window == self.window_3.get_window():
                    self.window_3.toggle_visibility(self.windows["window_3"])
                    
                    
        self.main_window.get_window().close()
        
if __name__ == "__main__":
    DESAPP = Main()
    DESAPP.DesApp()
