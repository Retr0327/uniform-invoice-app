import tkinter as tk
from ..models import UniformInvoice


class RedeemFrame(tk.LabelFrame):
    def __init__(self, parent, month):
        super().__init__(parent)
        self.month = month
        check_q = tk.StringVar()
        self.check_scrollbar = tk.Scrollbar(parent, orient=tk.VERTICAL)
        self.check_label = tk.Label(parent, text="請輸入發票號碼：")
        self.check_label.pack(anchor=tk.N, pady=10, padx=10, side=tk.LEFT)
        self.check_entry = tk.Entry(parent, textvariable=check_q)
        self.check_entry.pack(anchor=tk.N, pady=10, side=tk.LEFT)
        self.check_list = tk.Listbox(
            parent, width=50, yscrollcommand=self.check_scrollbar.set
        )
        self.check_scrollbar.config(command=self.check_list.yview)
        self.check_scrollbar.pack(side="right", fill="y")
        self.check_entry.bind("<Return>", self.check_click)
        self.check_but = tk.Button(parent, text="確認")
        self.check_but.pack(anchor=tk.N, pady=8, padx=10, side=tk.LEFT)
        self.check_but.bind("<Button-1>", self.check_click)
        self.check_list.pack(anchor=tk.NW, pady=8, padx=10, side=tk.LEFT, fill="both")

    def check_update(self, src):
        self.check_entry.delete(0, tk.END)
        try:
            invoice_check = UniformInvoice(self.month.get()).check(src)
            self.check_list.insert("end", f"{src}\t {invoice_check}")
            if invoice_check != "沒有中獎":
                tk.messagebox.showinfo("Congratulations", invoice_check)
        except IndexError:
            tk.messagebox.showerror("Information", "Select month first!")

    def check_click(self, event=None):
        self.check_update(self.check_entry.get())
