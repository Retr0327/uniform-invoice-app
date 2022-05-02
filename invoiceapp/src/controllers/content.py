import tkinter as tk
from ..models import UniformInvoice


class Content(tk.LabelFrame):
    def __init__(self, parent, month, click):
        super().__init__(parent)
        self.month = month
        self.click = click
        self.month.bind("<Return>", self.enter_click)
        self.click.bind("<Button-1>", self.enter_click)
        self.show_list = tk.Listbox(parent, width=70)
        self.show_list.pack(anchor=tk.W, padx=10, pady=10)

    def update(self, src):
        self.show_list.delete(0, tk.END)
        uni_invoice = UniformInvoice(src)
        try:
            content = uni_invoice.show_content().split("\n")
            for i in content:
                self.show_list.insert("end", i)
        except IndexError:
            tk.messagebox.showerror(
                "Information", "The month you have typed is invalid"
            )

    def enter_click(self, event=None):
        self.update(self.month.get())
