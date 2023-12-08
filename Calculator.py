import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
      def __init__(self):
          super().__init__()
          self.title("Calculator")
          self.geometry("300x400")

          # Entry to display current operation
          self.current_operation = tk.StringVar()
          self.entry = ttk.Entry(self, textvariable=self.current_operation, font=('Arial', 18), justify='right')
          self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

          # Buttons
          buttons = [
              '7', '8', '9', '/',
              '4', '5', '6', '*',
              '1', '2', '3', '-',
              'C', '0', '=', '+'
          ]

          row = 1
          col = 0
          for button in buttons:
              ttk.Button(self, text=button, command=lambda b=button: self.button_click(b), width=5).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
              col += 1
              if col > 3:
                  col = 0
                  row += 1

          # Making rows and columns expandable
          for i in range(4):
              self.grid_rowconfigure(i+1, weight=1)
              self.grid_columnconfigure(i, weight=1)

      def button_click(self, char):
          current_text = self.current_operation.get()
          if char == 'C':
              self.current_operation.set('')
          elif char == '=':
              try:
                  result = eval(current_text)
                  self.current_operation.set(result)
              except Exception as e:
                  self.current_operation.set("Error")
          else:
              self.current_operation.set(current_text + char)

if __name__ == "__main__":
      app = Calculator()
      app.mainloop()
