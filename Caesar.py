from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ctypes import *


fun = CDLL("C:\\Users\\Hiho0\\Downloads\\src\\libfun.dll")

fun.encryption.argtypes = [c_char_p, c_int]
fun.encryption.restype = c_char_p
fun.decryption.argtypes = [c_char_p, c_int]
fun.decryption.restype = c_char_p


def encrypt_msg():
    key = int(key_entry.get())
    msg = msg_entry.get()
    if not msg:
        messagebox.showerror("Error", "Please enter a message to encrypt")
    else:
        encrypted_msg = fun.encryption(msg.encode('utf-8'), key).decode('utf-8')
        result_entry.delete(0, END)
        result_entry.insert(0, encrypted_msg)


def decrypt_msg():
    key = int(key_entry.get())
    msg = msg_entry.get()
    if not msg:
        messagebox.showerror("Error", "Please enter a message to decrypt")
    else:
        decrypted_msg = fun.decryption(msg.encode('utf-8'), key).decode('utf-8')
        result_entry.delete(0, END)
        result_entry.insert(0, decrypted_msg)


root = Tk()
root.title("Encryption/Decryption Tool")


style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f0f0f0")
style.configure("TEntry", background="#fff", padding=5, font=("Helvetica", 12))
style.configure("TButton", background="#4CAF50", foreground="#fff", padding=10, font=("Helvetica", 12))
style.map("TButton", background=[("active", "#3e8e41")])


msg_label = ttk.Label(root, text="Message:")
msg_label.grid(row=0, column=0, padx=10, pady=10)

msg_entry = ttk.Entry(root, width=40)
msg_entry.grid(row=0, column=1, padx=10, pady=10)

key_label = ttk.Label(root, text="Key:")
key_label.grid(row=1, column=0, padx=10, pady=10)

key_entry = ttk.Entry(root, width=40)
key_entry.grid(row=1, column=1, padx=10, pady=10)

result_label = ttk.Label(root, text="Result:")
result_label.grid(row=2, column=0, padx=10, pady=10)

result_entry = ttk.Entry(root, width=40)
result_entry.grid(row=2, column=1, padx=10, pady=10)


encrypt_btn = ttk.Button(root, text="Encrypt", command=encrypt_msg)
encrypt_btn.grid(row=3, column=0, padx=10, pady=10)

decrypt_btn = ttk.Button(root, text="Decrypt", command=decrypt_msg)
decrypt_btn.grid(row=3, column=1, padx=10, pady=10)


root.mainloop()
