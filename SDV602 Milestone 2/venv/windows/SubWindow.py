import PySimpleGUI as sg
from charts.charts import Charts
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#------------------------------- SUBWINDOW CLASS -------------------------------

class SubWindow:
    def __init__(self, title):
        sg.theme("DarkBlue")
        self.title = title
        self.layout = [
            [sg.Text(f"{self.title}")],
            [sg.Canvas(background_color="red", key="-CANVAS-", size=(500, 500)), sg.Multiline(size=(50, 31), key="-CHAT-", disabled=True, autoscroll=True)],
            [sg.Button("Previous Chart", key="-PREV-", size=(20,1)), sg.Button("Next Chart", key="-NEXT-", size=(20,1)), sg.Push(), sg.Column([[sg.Input(size=(40, 1), key="-MESSAGE-"), sg.Button("Send", bind_return_key=True, size=(10,1))]])],
            [sg.Push(), sg.Button("Hide", key="-HIDE-", size=(10,1))]
        ]
        
        self.window = sg.Window("DES App", self.layout, finalize=True)
        self.window.hide()
        self.canvas = None

#------------------------------- CLASS METHODS -------------------------------

    def get_window(self):
        return self.window
    
    def draw_chart(self):
        fig = Charts.multiple_plots()
        self.canvas_elem = self.window["-CANVAS-"]
        self.canvas = FigureCanvasTkAgg(fig, self.canvas_elem.Widget)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    def toggle_visibility(self, state):
        if state["hidden"]:
            self.window.un_hide()
            self.draw_chart()
        else:
            self.window.hide()
            if self.canvas:
                self.canvas.get_tk_widget().destroy()
                self.canvas = None
        state["hidden"] = not state["hidden"]