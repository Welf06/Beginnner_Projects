import tkinter as tk
import stories as st
window = tk.Tk()
window.geometry('900x600')
window.title('Madlibs generator')
tk.Label(window, text='Madlibs Generator \n:D', font='aerial 30 bold').pack()
tk.Label(window, text = 'Choose any one story:', font='aerial 20 bold').place(x=50, y=125)
tk.Button(window, text = 'The Magic Book', font = 'ariel 20', command=st.story1, bg = 'grey').place(x= 50, y = 200 )
tk.Button(window, text= 'The butterfly', font = 'areiel 20', command=st.story2, bg='grey').place(x=50, y=300)
tk.Button(window, text= 'Apple and apple', font = 'aerial 20', command=st.story3, bg='grey').place(x=50, y=400)
window.mainloop()
 