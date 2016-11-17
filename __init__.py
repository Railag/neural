import tkinter as tk
from tkinter import ttk

import matplotlib

from neural.config import Config
from neural.network import Network

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

LARGE_FONT = ("Verdana", 12)
y = [2.0053, 2.0053, 2.0053, 2.0053, 1.9979, 2.0048, 2.0159, 2.0121, 2.0124, 2.0124, 2.0124, 2.0120, 2.0043, 2.0046,
     1.9940, 1.9828, 1.9828, 1.9828, 1.9824, 1.9776]

network = Network()

class Neural(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Neural")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (ChartPage, ChartPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ChartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class ChartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Временные ряды BYN & USD", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(ChartPage))
        button1.pack()

        labels = ['01.07', '02.07', '03.07', '04.07', '05.07', '06.07', '07.07', '08.07', '09.07', '10.07', '11.07',
                  '12.07', '13.07', '14.07', '15.07', '16.07', '17.07', '18.07', '19.07', '20.07']

        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        plt.xticks(x, labels)

        f, a = plt.subplots()
        a.plot(x, y)

        #f = Figure(figsize=(5, 5), dpi=100)

        # 14.11
        # .2016

        # , 1.9807,
        # 1.9780, 1.9850, 1.9850, 1.9850, 1.9897, 1.9953, 1.9943, 1.9889
        # 1, 9958
        # 1, 9958
        # 1, 9958
        # 1, 9799
        # 1, 9916
        # 1, 9928
        # 1, 9926
        # 1, 9777
        # 1, 9777
        # 1, 9777
        # 1, 9662
        # 1, 9658
        # 1, 9652
        # 1, 9648
        # 1, 9555
        # 1, 9555
        # 1, 9555
        # 1, 9482
        # 1, 9393
        # 1, 9388
        # 1, 9288
        # 1, 9288
        # 1, 9288
        # 1, 9288
        # 1, 9354
        # 1, 9421
        # 1, 9522
        # 1, 9571
        # 1, 9511
        # 1, 9511
        # 1, 9511
        # 1, 9574
        # 1, 9578
        # 1, 9605
        # 1, 9613
        # 1, 9692
        # 1, 9692
        # 1, 9692
        # 1, 9585
        # 1, 9612
        # 1, 9536
        # 1, 9472
        # 1, 9477
        # 1, 9477
        # 1, 9477
        # 1, 9577
        # 1, 9563
        # 1, 9560
        # 1, 9574
        # 1, 9524
        # 1, 9524
        # 1, 9524
        # 1, 9511
        # 1, 9481
        # 1, 9457
        # 1, 9334
        # 1, 9322
        # 1, 9322
        # 1, 9322
        # 1, 9336
        # 1, 9281
        # 1, 9330
        # 1, 9264
        # 1, 9268
        # 1, 9268
        # 1, 9268
        # 1, 9159
        # 1, 9178
        # 1, 9176
        # 1, 9156
        # 1, 9149
        # 1, 9149
        # 1, 9149
        # 1, 9137
        # 1, 9130
        # 1, 9189
        # 1, 9305
        # 1, 9251
        # 1, 9251
        # 1, 9251
        # 1, 9248
        # 1, 9185
        # 1, 9113
        # 1, 9064
        # 1, 9048
        # 1, 9048
        # 1, 9048
        # 1, 9023
        # 1, 9004
        # 1, 9017
        # 1, 9101
        # 1, 9065
        # 1, 9065
        # 1, 9065
        # 1, 9054
        # 1, 9040
        # 1, 9042
        # 1, 9039
        # 1, 9052
        # 1, 9052
        # 1, 9052
        # 1, 9052
        # 1, 9062
        # 1, 9083
        # 1, 9109
        # 1, 9433
        # 1, 9433
        # 1, 9433

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        teach()

def teach():
    answer = network.teach(y)

app = Neural()
app.mainloop()
