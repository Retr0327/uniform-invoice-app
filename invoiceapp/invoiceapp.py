import tkinter as tk
from tkinter import messagebox
from uniforminvoice import UniformInvoice


class InvoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # setup tkinter
        self.title("Receipt")
        self.geometry("800x600")

        # create the gui
        self.wrap_1 = tk.LabelFrame(self, text="本月發票開獎")
        self.wrap_1.place(height=175, width=500, rely=0.1, relx=0.0125)
        self.wrap_2 = tk.LabelFrame(self, text="兌獎")
        self.wrap_2.place(height=300, width=700, rely=0.45, relx=0.0125)
        self.month_label = tk.Label(self, text="請輸入月份：")
        self.month_label.pack(anchor=tk.N, pady=10, padx=10, side=tk.LEFT)
        q = tk.StringVar()
        self.month_entry = tk.Entry(self, textvariable=q)
        self.month_entry.pack(anchor=tk.N, pady=10, side=tk.LEFT)
        self.month_button = tk.Button(self, text="確認")
        self.month_button.pack(anchor=tk.N, pady=8, padx=10, side=tk.LEFT)
        self.show_page = ShowFrame(
            parent=self.wrap_1, month=self.month_entry, click=self.month_button
        )
        self.check_page = CheckFrame(parent=self.wrap_2, month=self.month_entry)


class ShowFrame(tk.LabelFrame):
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


class CheckFrame(tk.LabelFrame):
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


if __name__ == "__main__":
    i = InvoiceApp()
    i.mainloop()
