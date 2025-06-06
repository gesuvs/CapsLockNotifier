import tkinter as tk
import threading

class ToastNotifier:
  def __init__(self, message: str, duration: int = 1500):
    self.message = message
    self.duration = duration
  
  def show(self):
    threading.Thread(target=self._toast, daemon=True).start()
    
  def _toast(self):
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    screen_width = root.winfo_screenwidth()
    width, height = 300, 50
    x = (screen_width - width) // 2
    y = 100  # margem do topo

    toast = tk.Toplevel(root)
    toast.overrideredirect(True)
    toast.geometry(f"{width}x{height}+{x}+{y}")
    toast.configure(bg="#333333")
    toast.attributes("-topmost", True)

    label = tk.Label(toast, text=self.message, fg="white", bg="#333333", font=("Segoe UI", 12))
    label.pack(expand=True, fill='both')

    toast.after(self.duration, toast.destroy)
    root.after(self.duration + 200, root.destroy)  # Garante o fechamento da janela principal
    root.mainloop()

# def show_notification(message: str, duration: int = 430):
#   def _toast():
#     root = tk.Tk()
#     root.overrideredirect(True)
#     root.attributes("-topmost", True)
#     root.withdraw()
    

#     # root.attributes("-alpha", 0.9)
    
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenmmheight()
    
#     width, height = 200, 50
    
#     x = int((screen_width / 2) - (width / 2))
#     y = 50
#     root.geometry(f"{width}x{height}+{x}+{y}")
    
#     frame = tk.Frame(root,bg="#333",bd=1)
#     frame.pack(expand=True, fill="both")
    
#     label = tk.Label(frame,
#      text=message,
#       fg="white",
#       bg="#333", 
#       font=("Segoe UI", 12))
    
#     label.pack(expand=True)
    
#     root.after(duration, root.destroy)
#     root.mainloop()
  
#       # Executa em thread separada para não travar a execução principal
#   threading.Thread(target=run, daemon=True).start()
