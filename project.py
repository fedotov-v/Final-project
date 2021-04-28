from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Тест для ученика")
root.geometry("800x400")

def que_one():
    question = Label(root, text="В алфавите языка племени «тамба-амба» две буквы: Й и Ы.Сколько различных 8-буквенных слов можно образовать в этом языке?")
    answer = Entry()
    btn = Button(root, text="Ответить", command=lambda: game1(que_two))
    question.grid()
    answer.grid()
    btn.grid()

    def game1(que_two):
        if answer.get() == "256":
            que_two()
        else:
            messagebox.showerror("Неправильный ответ", "Попробуй ещё раз!")

def que_two():
    question_2 = Label(root, text="Алфавит языка «амба-карамба» состоит из 2 букв. Сколько различных четырехбуквенных слов можно образовать в этом языке?")
    answer_2 = Entry()
    btn_2 = Button(root, text="Ответить", command=lambda: game2(que_three))
    question_2.grid()
    answer_2.grid()
    btn_2.grid()

    def game2(que_two):
        if answer_2.get() == "16":
          que_three()

def que_three():
    question_3 = Label(root, text="Сколько существует в коде Морзе различных последовательностей из точек и тире, длина которых равна 3 символа?")
    answer_3 = Entry()
    btn_3 = Button(root, text="Ответить", command=lambda: game3(que_three))
    question_3.grid()
    answer_3.grid()
    btn_3.grid()

    def game3(que_three):
        if answer_3.get() == "8":
           messagebox.showinfo("Молодец!", "Ты прошёл тест!")
        else:
            messagebox.showerror("Неправильный ответ", "Попробуй ещё раз!")


que_one()
root.mainloop()
