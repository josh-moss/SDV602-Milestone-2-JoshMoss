import PySimpleGUI as sg
from charts.charts import Charts
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#------------------------------- MAIN WINDOW CLASS -------------------------------

class MainWindow:
    def __init__(self):
        sg.theme("DarkBlue")
        self.layout = [
            [sg.Text("Main Window", font=("Calibri", 24)), sg.Push(), sg.Button("Upload Data", key="-DATA-", size=(10,1)), sg.Button("Login", key="-LOGIN-", size=(10,1))],
            [sg.Canvas(background_color="white", key="-CANVAS-", size=(500, 500)), sg.Multiline(size=(50, 30), key="-CHAT-", disabled=True, autoscroll=True)],
            [sg.Button("Previous Chart", key="-PREV-", size=(20,1)), sg.Button("Next Chart", key="-NEXT", size=(20,1)), sg.Push(), sg.Column([[sg.Input(size=(40, 1), key="-MESSAGE-"), sg.Button("Send", bind_return_key=True, size=(10,1))]])],
            [sg.Column([[sg.Button("Show window 2", key="-SHOW_2-", size=(15,1)), sg.Button("Show Window 3", key="-SHOW_3-", size=(15,1))]]), sg.Push(), sg.Button("Exit", size=(10, 1))]
        ]
        
        self.window = sg.Window("DES App", self.layout, finalize=True)
        self.draw_chart()
    
    #changet his method later, dict indexed charts?
    def draw_chart(self):
        fig = Charts.multiple_plots()
        self.canvas_elem = self.window["-CANVAS-"]
        self.canvas = FigureCanvasTkAgg(fig, self.canvas_elem.Widget)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both')

    def get_window(self):
        return self.window