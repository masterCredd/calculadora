from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import color, width
"""_summary_
    import the package

"""

cor_preta = "#1e1f1e"
cor_branca = "#feffff"
cor_azul = "#38576b"
cor_cinza = "#ECEFF1"
cor_laranja = "#FFAB40"
"""_summary_
    define colors
    black
    white
    blue
    gray
    orange
"""

# windrows begin
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(
    bg=cor_preta
)
# end

# frame tela begin
frame_tela = Frame(
    janela,
    width=235,
    height=50,
    bg=cor_azul

)
frame_tela.grid(
    row=0,
    column=0
)
# end

# frama corpo begin
frame_corpo = Frame(
    janela,
    width=235,
    height=268
)
frame_corpo.grid(
    row=1,
    column=0
)
# end

# valores begin

valores = ''
valor_txt = StringVar()


def valores_entr(event):
    global valores
    valores += str(event)

    valor_txt.set(valores)


def calcular():
    global valores
    resultado = eval(valores)
    valor_txt.set(str(resultado))
# end


def limpar():
    global valores
    valores = ""
    valor_txt.set("")


# create label begin
app_lb = Label(
    frame_tela,
    textvariable=valor_txt,
    width=16,
    height=2,
    padx=7,
    relief=FLAT,
    anchor="e",
    justify=RIGHT,
    font=('Ivy 18'),
    bg=cor_azul
)
app_lb.place(
    x=0,
    y=0
)
# end

# create buttons begin

bnt_1_C = Button(
    frame_corpo,
    command=limpar,
    text="C",
    width=11,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_1_C.place(
    x=0,
    y=0
)

bnt_2_MD = Button(
    frame_corpo,
    command=lambda: valores_entr("%"),
    text="%",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_2_MD.place(
    x=118,
    y=0,
)

bnt_3_DV = Button(
    frame_corpo,
    command=lambda: valores_entr("/"),
    text="/",
    width=5,
    height=2,
    bg=cor_laranja,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_3_DV.place(
    x=177,
    y=0
)


bnt_4_n_7 = Button(
    frame_corpo,
    command=lambda: valores_entr("7"),
    text="7",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_4_n_7.place(
    x=0,
    y=52,
)

bnt_5_n_8 = Button(
    frame_corpo,
    command=lambda: valores_entr("8"),
    text="8",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_5_n_8.place(
    x=59,
    y=52,
)

bnt_6_n_9 = Button(
    frame_corpo,
    command=lambda: valores_entr("9"),
    text="9",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_6_n_9.place(
    x=118,
    y=52,
)


bnt_7_MT = Button(
    frame_corpo,
    command=lambda: valores_entr("*"),
    text="*",
    width=5,
    height=2,
    bg=cor_laranja,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_7_MT.place(
    x=177,
    y=52
)

bnt_8_n_4 = Button(
    frame_corpo,
    command=lambda: valores_entr("4"),
    text="4",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_8_n_4.place(
    x=0,
    y=104,
)

bnt_9_n_5 = Button(
    frame_corpo,
    command=lambda: valores_entr("5"),
    text="5",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_9_n_5.place(
    x=59,
    y=104,
)

bnt_10_n_6 = Button(
    frame_corpo,
    command=lambda: valores_entr("6"),
    text="6",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_10_n_6.place(
    x=118,
    y=104,
)

bnt_11_MS = Button(
    frame_corpo,
    command=lambda: valores_entr("-"),
    text="-",
    width=5,
    height=2,
    bg=cor_laranja,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_11_MS.place(
    x=177,
    y=104
)

bnt_12_n_1 = Button(
    frame_corpo,
    command=lambda: valores_entr("1"),
    text="1",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_12_n_1.place(
    x=0,
    y=156,
)

bnt_13_n_2 = Button(
    frame_corpo,
    command=lambda: valores_entr("2"),
    text="2",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_13_n_2.place(
    x=59,
    y=156,
)

bnt_14_n_3 = Button(
    frame_corpo,
    command=lambda: valores_entr("3"),
    text="3",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_14_n_3.place(
    x=118,
    y=156,
)

bnt_15_MSS = Button(
    frame_corpo,
    command=lambda: valores_entr("+"),
    text="+",
    width=5,
    height=2,
    bg=cor_laranja,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_15_MSS.place(
    x=177,
    y=156
)

bnt_16_0 = Button(
    frame_corpo,
    command=lambda: valores_entr("0"),
    text="0",
    width=11,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_16_0.place(
    x=0,
    y=208
)

bnt_17_n_VL = Button(
    frame_corpo,
    command=lambda: valores_entr("."),
    text=".",
    width=5,
    height=2,
    bg=cor_cinza,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_17_n_VL.place(
    x=118,
    y=208,
)

bnt_18_IG = Button(
    frame_corpo,
    command=calcular,
    text="=",
    width=5,
    height=2,
    bg=cor_laranja,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE
)
bnt_18_IG.place(
    x=177,
    y=208
)
# end


janela.mainloop()
