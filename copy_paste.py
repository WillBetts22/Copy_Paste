import tkinter as tk
import pyperclip
import threading
import time

class ClipboardManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Manager")
        self.history = []

        # Using a Text widget for easier copy-paste interaction
        self.text = tk.Text(root, wrap='word')
        self.text.pack(fill=tk.BOTH, expand=True)

        self.monitor_clipboard()

    def monitor_clipboard(self):
        def check_clipboard():
            previous_text = ""
            while True:
                try:
                    current_text = pyperclip.paste()
                    if current_text != previous_text and current_text:
                        previous_text = current_text
                        self.add_to_history(current_text)
                    time.sleep(1)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break

        threading.Thread(target=check_clipboard, daemon=True).start()

    def add_to_history(self, text):
        if text not in self.history:
            self.history.append(text)
            self.text.insert(tk.END, text + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardManager(root)
    root.mainloop()
