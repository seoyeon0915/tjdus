"""import tkinter as tk
from tkinter import messagebox

animal_images = {
    "강아지": "C:\sy\jpeg파일\dog.gif",
    "고양이": "C:\sy\jpeg파일\cat.gif",
    "토끼": "C:\sy\jpeg파일\rabbit.gif"
}

def show_image():
    selected_animal = animal_var.get()
    if selected_animal in animal_images:
        image_path = animal_images[selected_animal]
        image_label.config(image=tk.PhotoImage(file="C:\sy\jpeg파일\dog.gif"))
    else:
        messagebox.showerror("에러", "선택한 동물의 이미지를 찾을 수 없습니다.")

root = tk.Tk()
root.title("좋아하는 동물 투표")

animal_var = tk.StringVar()

label = tk.Label(root, text="좋아하는 동물을 선택하세요:")
label.pack()

for animal in animal_images.keys():
    tk.Radiobutton(root, text=animal, variable=animal_var, value=animal).pack()

show_button = tk.Button(root, text="사진 보기", command=show_image)
show_button.pack()

image_label = tk.Label(root)
image_label.pack()

root.mainloop()"""

"""import tkinter as tk

text_list = [
    "jeju1.gif",
    "jeju2.gif",
    "jeju3.gif",
    "jeju4.gif",
    "jeju5.gif",
    "jeju6.gif",
    "jeju7.gif",
    "jeju8.gif",
    "jeju9.gif"
]


current_index = 0

def update_text():
    global current_index
    text = text_list[current_index]
    text_label.config(text=text)


def previous_text():
    global current_index
    current_index -= 1
    if current_index < 0:
        current_index = len(text_list) - 1
    update_text()


def next_text():
    global current_index
    current_index += 1
    if current_index >= len(text_list):
        current_index = 0
    update_text()


window = tk.Tk()
window.title("텍스트 뷰어")


text_label = tk.Label(window, text="")
text_label.pack()

previous_button = tk.Button(window, text="<이전", command=previous_text)
previous_button.pack(side="left")


next_button = tk.Button(window, text="다음>", command=next_text)
next_button.pack(side="right")


update_text()

window.mainloop()"""


"""import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("경고", "할 일을 입력하세요!")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

window = tk.Tk()
window.title("To-Do 리스트 관리 프로그램")

task_entry = tk.Entry(window, width=30)
task_entry.pack()

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(window, width=30)
task_listbox.pack()


delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

window.mainloop()"""
