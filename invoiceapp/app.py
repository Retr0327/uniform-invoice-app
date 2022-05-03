import tkinter as tk
from src import Content, RedeemFrame


class UniformInvoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Receipt")
        self.geometry("800x600")
        self.wrap_1 = tk.LabelFrame(self, text="本月發票開獎")
        self.wrap_1.place(height=175, width=500, rely=0.1, relx=0.0125)
        self.wrap_2 = tk.LabelFrame(self, text="兌獎")
        self.wrap_2.place(height=300, width=700, rely=0.45, relx=0.0125)
        self.month_label = tk.Label(self, text="請輸入月份：")
        self.month_label.pack(anchor=tk.N, pady=10, padx=10, side=tk.LEFT)
        query_string = tk.StringVar()
        self.month_entry = tk.Entry(self, textvariable=query_string)
        self.month_entry.pack(anchor=tk.N, pady=10, side=tk.LEFT)
        self.month_button = tk.Button(self, text="確認")
        self.month_button.pack(anchor=tk.N, pady=8, padx=10, side=tk.LEFT)
        self.show_page = Content(
            parent=self.wrap_1, month=self.month_entry, click=self.month_button
        )
        self.check_page = RedeemFrame(parent=self.wrap_2, month=self.month_entry)


if __name__ == "__main__":
    app = UniformInvoiceApp()
    app.mainloop()
