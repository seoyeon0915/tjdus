import tkinter as tk
import sqlite3

con = sqlite3.connect("md+202310630.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS userData (
                사용자ID TEXT,
                사용자이름 TEXT,
                이메일 TEXT,
                출생연도 INTEGER)''')  # "출생연도" 열 추가
con.commit()

def insert_data():
    사용자ID = entry_사용자ID.get()
    사용자이름 = entry_사용자이름.get()
    이메일 = entry_이메일.get()
    출생연도 = entry_출생연도.get()

    cur.execute("INSERT INTO userData (사용자ID, 사용자이름, 이메일, 출생연도) VALUES (?, ?, ?, ?)",
                (사용자ID, 사용자이름, 이메일, 출생연도))
    con.commit()

def fetch_data():
    입력된_사용자ID = entry_사용자ID.get()
    cur.execute("SELECT * FROM userData WHERE 사용자ID=?", (입력된_사용자ID,))
    row = cur.fetchone()

    result_text.delete(1.0, tk.END)  # 이전 내용을 지웁니다.

    if row:
        result_text.insert(tk.END, "사용자ID\t 사용자이름\t 이메일\t 출생연도\n")
        result_text.insert(tk.END, "-"*40 + "\n")
        result_text.insert(tk.END, f"{row[0]}\t {row[1]}\t {row[2]}\t {row[3]}\n")
    else:
        result_text.insert(tk.END, "데이터가 없습니다.")

window = tk.Tk()
window.title("사용자 정보 입력 및 조회")
window.geometry("600x400")

frame_input = tk.Frame(window)
frame_input.pack(pady=20)
frame_input.grid_columnconfigure(0, weight=1)

entry_사용자ID = tk.Entry(frame_input, width=10)
entry_사용자ID.grid(row=0, column=0, padx=10)
entry_사용자이름 = tk.Entry(frame_input, width=20)
entry_사용자이름.grid(row=0, column=1, padx=10)
entry_이메일 = tk.Entry(frame_input, width=10)
entry_이메일.grid(row=0, column=2, padx=10)
entry_출생연도 = tk.Entry(frame_input, width=10)
entry_출생연도.grid(row=0, column=3, padx=10)

button_insert = tk.Button(frame_input, text="입력", command=insert_data)
button_insert.grid(row=0, column=4, padx=10)
button_fetch = tk.Button(frame_input, text="조회", command=fetch_data)
button_fetch.grid(row=0, column=5, padx=10)

frame_buttons = tk.Frame(window)
frame_buttons.pack()

result_text = tk.Text(window, height=10, width=40)
result_text.pack()

window.mainloop()

con.close()
