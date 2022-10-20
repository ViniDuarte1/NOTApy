from cProfile import label
from tkinter import *


janela = Tk()      # cria objeto visual
janela.title("NOTA")
janela.geometry('300x300')
janela.configure(bg='#7FFFD4') # cor da janela

def calcula():
    vnota = float(nota.get())
    vfaltas = float(faltas.get())

    if(vnota <= 10 and vfaltas <= 20):
        if(vnota < 4 and vfaltas > 5):
            l_frase['text']='Reprovado por FALTAS e NOTA'
        elif(vfaltas > 5):
            l_frase['text']='Reprovado por FALTAS'
        elif(vnota < 4):
            l_frase['text']='Reprovado por NOTA'
        elif(vnota >= 4 and vnota < 6):
            l_frase['text']='RECUPERAÇÃO'
        elif(vnota >= 6):
            l_frase['text']='APROVADO'
    else:
        l_frase['text']='VALORES INCORRETOS'
        
        
        
    
# muda cor de uma parte em cima
frame_cima = Frame(janela, width=300,height=50, bg='#008080')
frame_cima.grid(row=0,column=0)
#mesma coisa ai de cima oh muda a cor pra ver
frame_baixo = Frame(janela, width=300,height=250, bg='#7FFFD4')
frame_baixo.grid(row=1,column=0)

app_name = Label(frame_cima,text="VERIFICADOR", width=25, height=2, bg='#008080', fg='black', font='times')
app_name.place(x=0,y=0)


f_nota = Label(frame_baixo,text="Digite a nota:    ")
f_nota.place(x=0,y=0)
nota = Entry(frame_baixo, width=20) # como se fosse input, recebe o valor da variavel
nota.place(x=87,y=0) # informa local da frase

f_faltas = Label(frame_baixo,text="Digite as faltas: ") # exibe a frase
f_faltas.place(x=0,y=20) 
faltas = Entry(frame_baixo, width=20)
faltas.place(x=87,y=20)



l_frase = Label(frame_baixo, text='', width=30, height=1, font='Ivy 12 bold', bg='yellow')
l_frase.place(x=0, y=120)

#button
bcalcular = Button(frame_baixo,  text="RESULTADO", command=calcula)
# posição do button
bcalcular.place(x=115,y=50)



# fixa a janela
janela.mainloop()