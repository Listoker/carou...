from tkinter import *
import json

current_question = 0


def otkritie():
    # открытие json файла
    with open('json.json', encoding='UTF-8') as cat_file:
        question = json.load(cat_file)
    # определите список ответов
    ans = ['Пекин', 'Каспийское море', 'Россия', 'Ватикан', 'Канада']
    print(question)

    class Igra:
        def start_quiz(self):
            start_button.forget()
            next_button.pack()
            self.name = text.get()
            text.destroy()
            self.next_question()

        def next_question(self):
            global current_question
            if current_question < len(question):
                # получите ключ или вопрос, которые необходимо распечатать
                check_ans()
                user_ans.set('None')
                c_question = list(question.keys())[current_question]
                # четкие рамки для обновления его содержимого
                clear_frame()
                # вопрос о печати
                Label(f1, text=f"Вопрос: {c_question}", padx=15,
                      font="calibre 12 normal").pack(anchor=NW)
                # параметры печати
                for option in question[c_question]:
                    Radiobutton(f1, text=option, variable=user_ans,
                                value=option, padx=28).pack(anchor=NW)
                current_question += 1
            else:
                current_question = 0
                next_button.forget()
                check_ans()
                clear_frame()
                with open('ttt.txt', 'r') as ff:
                    textt = ff.read().split()[3]
                if textt != '0':
                    output = f"{self.name}, твой результат {user_score.get()} из {len(question)}, а прошлый {textt}"
                else:
                    output = f"{self.name}, твой результат {user_score.get()} из {len(question)}"
                Label(f1, text=output, font="calibre 25 bold").pack()
                Label(f1, text="Спасибо за участие",
                      font="calibre 18 bold").pack()

                new = Button(root, text="Начать заново",
                             command=self.uuu,
                             font="calibre 17 bold")
                new.pack()
                root.mainloop()

        def uuu(self):
            root.destroy()
            # сохранение результата
            with open('ttt.txt', 'w') as f:
                f.write(f"{self.name}, твой результат {user_score.get()} из {len(question)}")
            return otkritie()

    def check_ans():
        temp_ans = user_ans.get()
        if temp_ans != 'None' and temp_ans == ans[current_question - 1]:
            user_score.set(user_score.get() + 1)

    def clear_frame():
        for widget in f1.winfo_children():
            widget.destroy()

    root = Tk()
    # основное окно настройки
    root.title("GFG QUIZ APP")
    root.geometry("850x520")
    root.minsize(800, 400)

    text = Entry(root, width=50)
    text.pack()

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    a = Igra()

    Label(root, text="Викторина",
          font="calibre 40 bold",
          relief=SUNKEN, background="yellow",
          padx=10, pady=9).pack()
    Label(root, text="", font="calibre 10 bold").pack()
    start_button = Button(root,
                          text="Начать",
                          command=a.start_quiz,
                          font="calibre 17 bold")
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Следующий вопрос",
                         command=a.next_question,
                         font="calibre 17 bold")

    root.mainloop()


otkritie()
