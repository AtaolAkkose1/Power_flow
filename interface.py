import re
import tkinter as tk
from cmath import *
from tkinter import ttk

j = (-1)**0.5
temel = tk.Tk()
Ana_ekran = tk.Canvas(temel, width=1024, height=768, bg='white')
Ana_ekran.pack()
dugum_nok = []

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

bara_dugum = []
bara = [[0, 0, 0, 0]]
bara_koor = {}
baralar = {}
koor = []
hat_kim = []
hatlar = {}
hat_koor = {}
trafo_koor = [[0,0]]
trafolar = {}
gen = []
gen_koor = [[0,0]]
generator = {}

def Bara():
    def Bara_tanimla(e):

        a = e.x
        b = e.y
        a = a - (a*10)%10
        b = b - (b*10)%10

        class Is_bara:
            def __init__(self):
                self.Bara_ismi = tk.StringVar()
                self.V_pu = tk.StringVar()
                self.Faz_pu = tk.StringVar()
                self.Ref = tk.StringVar()

            def Bara_adi(self):
                tk.Label(temel, text='İsim : \nBirim Vpu : \nFaz Açısı : ', font=(None, 8)).place(x=a-7.5, y=b+10)
                self.ttt = tk.Label(temel, text=f'Bara{len(bara) - 1}\n 1 \n 0 ', font=(None, 8))
                self.ttt.place(x=a+50, y=b + 10)
                baralar.update({f'{a},{b}': [f'Bara{len(bara) - 1}', {f'Bara{len(bara) - 1}'}, 1, 0]})
                print(baralar)

            def Degistir(self):
                global deger_isim, deger_V, deger_faz
                deger_isim, deger_V, deger_faz = self.Bara_ismi.get(), self.V_pu.get(), self.Faz_pu.get()
                self.kkk = tk.Label(temel, text=f'{deger_gen}\n{deger_V}\n{deger_faz}', font=(None, 8)).place(x=a + 50, y=b + 10)
                self.bara_entry.delete(0, tk.END)
                self.V_entry.delete(0, tk.END)
                self.faz_entry.delete(0, tk.END)
                baralar[f'{a},{b}'][1] = deger_isim
                baralar[f'{a},{b}'][2] = deger_V
                baralar[f'{a},{b}'][3] = deger_faz
                print(baralar)
                self.ttt.destroy()

            def Ikinci_ekran(self):
                self.Ikinci_ekran_i = tk.Toplevel(temel)
                self.Ikinci_ekran_i.geometry('200x200')

                tk.Label(self.Ikinci_ekran_i, text='İsim : \n\nBirim Vpu : \n\nFaz Açısı : \n\nReferans : ').place(x=20, y=20)
                self.bara_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.Bara_ismi)
                self.bara_entry.place(x=90, y=23)
                self.V_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.V_pu)
                self.V_entry.place(x=90, y=53)
                self.faz_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.Faz_pu)
                self.faz_entry.place(x=90, y=83)
                tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.Ref).place(x=90, y=113)
                tk.Button(self.Ikinci_ekran_i, text='Değiştir', command=Is_bara.Degistir).place(x=120, y=140)

        k = True
        for i in bara:
            if (i[0] - 8 <= a <= i[0] + 8) and (i[1] - 78 <= b <= i[1] + 78):
                k = False
            else:
                pass

        if a-8 <= 0 or b-78 <= 0 :
            k = False

        if k == True:
            Ana_ekran.create_rectangle(a, b, a - 5, b - 75, fill='black')
            bara.append([a, b, a - 5, b - 75])

            Ana_ekran.create_circle(a - 2.5, b - 37.5, 4)
            Ana_ekran.create_circle(a - 2.5, b, 4)
            Ana_ekran.create_circle(a - 2.5, b - 75, 4)
            dugum_nok.append([a - 2.5, b - 37.5])
            dugum_nok.append([a - 2.5, b])
            dugum_nok.append([a - 2.5, b - 75])
            bara_dugum.append([a - 2.5, b - 37.5])
            bara_dugum.append([a - 2.5, b])
            bara_dugum.append([a - 2.5, b - 75])
            bara_koor.update({f'Bara{len(bara) - 1}':[a - 2.5, b - 37.5, a - 2.5, b, a - 2.5, b - 75]})
            print(bara_dugum)
            Is = Is_bara()
            Is.Bara_adi()
            tk.Button(temel, text='D', command=Is.Ikinci_ekran).place(x=a - 35, y=b + 7)

    Ana_ekran.bind('<ButtonPress-1>', Bara_tanimla)

def Hat():
    hat = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
    cizgi = []
    def Hat_dugum(e):
        hat['x1'] = e.x
        hat['y1'] = e.y
        hat['x1'] = hat['x1'] - (hat['x1']*10)%10
        hat['y1'] = hat['y1'] - (hat['y1']*10)%10
        cizgi.append(Ana_ekran.create_line(hat['x1'], hat['y1'], hat['x1'], hat['y1'], fill='orange', width=2))
        koor.append([hat['x1'], hat['y1']])

    def Surukle(e):
        hat['x2'] = e.x
        hat['y2'] = e.y
        Ana_ekran.coords(cizgi[-1], hat['x1'], hat['y1'], hat['x2'], hat['y2'])
        koor.append([hat['x2'], hat['y2']])

    def Olustur(e):
        a = e.x
        b = e.y
        class Is_hat:
            def __init__(self):
                self.hat_ismi = tk.StringVar()
                self.Z_pu = tk.StringVar()
                self.Y_pu = tk.StringVar()
                self.emp = tk.IntVar()
                self.z_reel, self.z_imag = tk.IntVar(), tk.IntVar()
                self.y_reel, self.y_imag = tk.IntVar(), tk.IntVar()

            def Hat_adi(self):
                self.ttt = tk.Label(temel, text=f'İsim :\nZ ohm :\nY mho :')
                self.ppp = tk.Label(temel, text=f'Hat{len(hat_kim)}\n0\nsonsuz')
                return self.ttt, self.ppp

            def Degistir(self):
                global hat_i, z_reel_i, y_reel_i, z_im_i, y_im_i
                hat_i, z_reel_i, y_reel_i, z_im_i, y_im_i = self.hat_ismi.get(), self.z_reel.get(), self.y_reel.get(), self.z_imag.get(), self.y_imag.get()
                if self.emp.get() != 1:
                    Z_ri = round(z_reel_i, 3) + j * round(z_im_i, 3)
                    Y_ri = complex(1 / Z_ri)
                    Y_ri = round(Y_ri.real, 3) + j * round(Y_ri.imag, 3)
                else:
                    Y_ri = round(y_reel_i, 3) + j * round(y_im_i, 3)
                    Z_ri = complex(1 / Y_ri)
                    Z_ri = round(Z_ri.real, 3) + j * round(Z_ri.imag, 3)

                tk.Label(temel, text=f'{hat_i}\n{Z_ri}\n{Y_ri}').place(x=a + 45, y=b)
                self.ppp.destroy()

            def empedans(self):
                if self.emp.get() != 1:
                    self.Y_entry_reel.configure(state='disabled')
                    self.Y_entry_imaj.configure(state='disabled')
                    self.Z_entry_reel.configure(state='normal')
                    self.Z_entry_imaj.configure(state='normal')
                else:
                    self.Y_entry_reel.configure(state='normal')
                    self.Y_entry_imaj.configure(state='normal')
                    self.Z_entry_reel.configure(state='disabled')
                    self.Z_entry_imaj.configure(state='disabled')

            def Ikinci_ekran(self):
                self.ikinci_ekran = tk.Toplevel(temel)
                self.ikinci_ekran.geometry('210x175')

                tk.Label(self.ikinci_ekran, text='Hat İsmi').place(x=10, y=20)
                self.hat_entry = tk.Entry(self.ikinci_ekran, textvariable=self.hat_ismi, width=17)
                self.hat_entry.place(x=60, y=20)

                tk.Label(self.ikinci_ekran, text='Re').place(x=15, y=80)
                tk.Label(self.ikinci_ekran, text='Im').place(x=15, y=110)
                self.Z_entry_reel = tk.Entry(self.ikinci_ekran, textvariable=self.z_reel, width=8)
                self.Z_entry_reel.place(x=40, y=80)
                self.Z_entry_imaj = tk.Entry(self.ikinci_ekran, textvariable=self.z_imag, width=8)
                self.Z_entry_imaj.place(x=40, y=110)
                self.Y_entry_reel = tk.Entry(self.ikinci_ekran, textvariable=self.y_reel, width=8)
                self.Y_entry_reel.place(x=135, y=80)
                self.Y_entry_imaj = tk.Entry(self.ikinci_ekran, textvariable=self.y_imag, width=8)
                self.Y_entry_imaj.place(x=135, y=110)
                self.Y_entry_reel.configure(state='disabled')
                self.Y_entry_imaj.configure(state='disabled')

                tk.Radiobutton(self.ikinci_ekran, text='Z ohm', variable=self.emp, value=0,
                               command=Is_hat.empedans).place(x=35, y=50)
                tk.Radiobutton(self.ikinci_ekran, text='Y mho', variable=self.emp, value=1,
                               command=Is_hat.empedans).place(x=130, y=50)

                tk.Button(self.ikinci_ekran, text='Değiştir', command=Is_hat.Degistir).place(x=115, y=140)

        global place_n
        xn1, xn2, yn1, yn2 = [0, 0, 0, 0]
        for i in cizgi:
            Ana_ekran.delete(i)
        for i in dugum_nok:
            if i[0] - 5 <= koor[0][0] <= i[0] + 5:
                xn1 = i[0]
            if i[1] - 5 <= koor[0][1] <= i[1] + 5:
                yn1 = i[1]
            if i[0] - 5 <= koor[len(koor) - 1][0] <= i[0] + 5:
                xn2 = i[0]
            if i[1] - 5 <= koor[len(koor) - 1][1] <= i[1] + 5:
                yn2 = i[1]

        if abs(xn1 - xn2) > abs(yn1 - yn2):
            Ana_ekran.create_line(xn1, yn1, xn1+(abs(xn1-xn2)/2), yn1, fill='black', width=1)
            Ana_ekran.create_line(xn1+(abs(xn1-xn2)/2), yn1, xn1 + (abs(xn1 - xn2) / 2), yn2, fill='black', width=1)
            Ana_ekran.create_line(xn1+(abs(xn1-xn2)/2), yn2, xn2, yn2, fill='black', width=1)
            print(xn1, yn1, xn2, yn2)
            place_n = [xn1+(abs(xn1 - xn2)/2)-10, (yn1+yn2)/2]

        if abs(xn1 - xn2) < abs(yn1 - yn2):
            Ana_ekran.create_line(xn1, yn1, xn1, yn1+(abs(yn1-yn2)/2), fill='black', width=1)
            Ana_ekran.create_line(xn1, yn1+(abs(yn1-yn2)/2), xn2, yn1+(abs(yn1-yn2)/2), fill='black', width=1)
            Ana_ekran.create_line(xn2, yn1+(abs(yn1-yn2)/2), xn2, yn2, fill='black', width=1)
            place_n = [(xn1+xn2)/2, yn1 + (abs(yn1 - yn2)/2)-10]
        koor.clear()

        hat_kim.append([xn1, yn1, xn2, yn2])
        print(hat_kim)
        hatlar.update({f'Hat{len(hat_kim)}': [f'Hat{len(hat_kim)}', 0, 0]})
        hat_koor.update({f'Hat{len(hat_kim)}': [xn1, yn1, xn2, yn2]})
        Is_hat = Is_hat()
        Is_hat.Hat_adi()[0].place(x=place_n[0], y=place_n[1])
        Is_hat.Hat_adi()[1].place(x=place_n[0] + 45, y=place_n[1])

        for i in bara_koor.keys():
            for k in hat_koor.keys():
                if bara_koor[i][0] == hat_koor[k][0] and bara_koor[i][1] == hat_koor[k][1]:
                    hatlar[k][1] = i
                if bara_koor[i][0] == hat_koor[k][2] and bara_koor[i][1] == hat_koor[k][3]:
                    hatlar[k][2] = i
                if bara_koor[i][2] == hat_koor[k][0] and bara_koor[i][3] == hat_koor[k][1]:
                    hatlar[k][1] = i
                if bara_koor[i][2] == hat_koor[k][2] and bara_koor[i][3] == hat_koor[k][3]:
                    hatlar[k][2] = i
                if bara_koor[i][4] == hat_koor[k][0] and bara_koor[i][5] == hat_koor[k][1]:
                    hatlar[k][1] = i
                if bara_koor[i][4] == hat_koor[k][2] and bara_koor[i][5] == hat_koor[k][3]:
                    hatlar[k][2] = i
        tk.Button(temel,text='D', command=Is_hat.Ikinci_ekran).place(x=place_n[0] - 25, y=place_n[1])

    Ana_ekran.bind('<ButtonPress-1>', Hat_dugum)
    Ana_ekran.bind('<B1-Motion>', Surukle)
    Ana_ekran.bind('<ButtonRelease-1>', Olustur)

def Trafo():
    def Trafo_tanimla(e):
        a = e.x
        b = e.y
        class Is_trafo:
            def __init__(self):
                self.trafo_ismi = tk.StringVar()
                self.Z_pu = tk.StringVar()
                self.Y_pu = tk.StringVar()
                self.emp = tk.IntVar()
                self.z_reel, self.z_imag = tk.IntVar(), tk.IntVar()
                self.y_reel, self.y_imag = tk.IntVar(), tk.IntVar()

            def Trafo_adi(self):
                tk.Label(temel, text='İsim : \nZ ohm_pu : \nY mho_pu : ', font=(None, 8)).place(x=a-5, y=b+10)
                self.ttt = tk.Label(temel, text=f'Tr{len(trafo_koor) - 1}\n0 \nsonsuz ', font=(None, 8))
                self.ttt.place(x=a+50, y=b + 10)
                trafolar.update({f'{a},{b}': [f'Tr{len(trafo_koor) - 1}', {f'Tr{len(trafo_koor) - 1}'}, 1, 0]})
                print(trafolar)

            def Degistir(self):
                global tr_i, z_reel_i, y_reel_i, z_im_i, y_im_i
                tr_i, z_reel_i, y_reel_i, z_im_i, y_im_i = self.trafo_ismi.get(), self.z_reel.get(), self.y_reel.get(), self.z_imag.get(), self.y_imag.get()
                if self.emp.get() != 1:
                    Z_ri = round(z_reel_i, 3) + j * round(z_im_i, 3)
                    Y_ri = complex(1 / Z_ri)
                    Y_ri = round(Y_ri.real, 3) + j * round(Y_ri.imag, 3)
                else:
                    Y_ri = round(y_reel_i, 3) + j * round(y_im_i, 3)
                    Z_ri = complex(1 / Y_ri)
                    Z_ri = round(Z_ri.real, 3) + j * round(Z_ri.imag, 3)

                tk.Label(temel, text=f'{tr_i}\n{Z_ri}\n{Y_ri}').place(x=a+50, y=b + 10)
                self.ttt.destroy()

            def empedans(self):
                if self.emp.get() != 1:
                    self.Y_entry_reel.configure(state='disabled')
                    self.Y_entry_imaj.configure(state='disabled')
                    self.Z_entry_reel.configure(state='normal')
                    self.Z_entry_imaj.configure(state='normal')
                else:
                    self.Y_entry_reel.configure(state='normal')
                    self.Y_entry_imaj.configure(state='normal')
                    self.Z_entry_reel.configure(state='disabled')
                    self.Z_entry_imaj.configure(state='disabled')

            def Ikinci_ekran(self):
                self.ikinci_ekran = tk.Toplevel(temel)
                self.ikinci_ekran.geometry('210x175')

                tk.Label(self.ikinci_ekran, text='Hat İsmi').place(x=10, y=20)
                self.hat_entry = tk.Entry(self.ikinci_ekran, textvariable=self.trafo_ismi, width=17)
                self.hat_entry.place(x=60, y=20)

                tk.Label(self.ikinci_ekran, text='Re').place(x=15, y=80)
                tk.Label(self.ikinci_ekran, text='Im').place(x=15, y=110)
                self.Z_entry_reel = tk.Entry(self.ikinci_ekran, textvariable=self.z_reel, width=8)
                self.Z_entry_reel.place(x=40, y=80)
                self.Z_entry_imaj = tk.Entry(self.ikinci_ekran, textvariable=self.z_imag, width=8)
                self.Z_entry_imaj.place(x=40, y=110)
                self.Y_entry_reel = tk.Entry(self.ikinci_ekran, textvariable=self.y_reel, width=8)
                self.Y_entry_reel.place(x=135, y=80)
                self.Y_entry_imaj = tk.Entry(self.ikinci_ekran, textvariable=self.y_imag, width=8)
                self.Y_entry_imaj.place(x=135, y=110)
                self.Y_entry_reel.configure(state='disabled')
                self.Y_entry_imaj.configure(state='disabled')

                tk.Radiobutton(self.ikinci_ekran, text='Z ohm', variable=self.emp, value=0,
                               command=Is_trafo.empedans).place(x=35, y=50)
                tk.Radiobutton(self.ikinci_ekran, text='Y mho', variable=self.emp, value=1,
                               command=Is_trafo.empedans).place(x=130, y=50)

                tk.Button(self.ikinci_ekran, text='Değiştir', command=Is_trafo.Degistir).place(x=115, y=140)

        k = False
        for i in trafo_koor:
            if i[0]-70<= a <= i[0]+70 and i[1]-70<= b <= i[1]+70:
                k = False
            else:
                k = True
        if k == True:
            Ana_ekran.create_line(a - 45, b - 50, a - 35, b - 50, width=2)
            Ana_ekran.create_line(a - 45, b, a - 35, b, width=2)
            Ana_ekran.create_line(a - 35, b - 50, a - 35, b, width=2)
            Ana_ekran.create_line(a, b - 50, a + 10, b - 50, width=2)
            Ana_ekran.create_line(a, b, a + 10, b, width=2)
            Ana_ekran.create_line(a, b - 50, a, b, width=2)
            Ana_ekran.create_line(a - 43, b - 47, a - 60, b - 37, a + 25, b - 37, a + 7, b - 27, smooth=1, width=2)
            Ana_ekran.create_line(a - 43, b - 35, a - 60, b - 25, a + 25, b - 25, a + 7, b - 15, smooth=1, width=2)
            Ana_ekran.create_line(a - 43, b - 23, a - 60, b - 13, a + 25, b - 13, a + 7, b - 3, smooth=1, width=2)
            Ana_ekran.create_circle(a - 55, b - 25, 3)
            Ana_ekran.create_circle(a + 20, b - 25, 3)

            Is_trafo = Is_trafo()
            Is_trafo.Trafo_adi()
            trafo_koor.append([a, b])
            dugum_nok.append([a - 55, b - 25])
            dugum_nok.append([a + 20, b - 25])
            trafo_bag = dugum_nok
            trafolar.update({f'Trafo{len(trafo_koor)-1}':[f'Trafo{len(trafo_koor)-1}', trafo_koor[0], trafo_koor[1], ]})
            tk.Button(temel, text='D', command=Is_trafo.Ikinci_ekran).place(x=a - 25, y=b)

    Ana_ekran.bind('<ButtonPress-1>', Trafo_tanimla)

def Generator():
    def Generator_tanimla(e):
        a = e.x
        b = e.y
        class Is_gen:
            def __init__(self):
                self.gen_ismi = tk.StringVar()
                self.S_pu = tk.IntVar()

            def Gen_adi(self):
                tk.Label(temel, text='İsim : \nBirim Spu : ', font=(None, 8)).place(x=a-25, y=b+40)
                self.ttt = tk.Label(temel, text=f'G{len(gen_koor) - 1}\n 1 ', font=(None, 8))
                self.ttt.place(x=a+30, y=b + 40)
                generator.update({f'{a},{b}': [f'G{len(gen_koor) - 1}', {f'G{len(gen_koor) - 1}'}, 1, 0]})
                print(generator)

            def Degistir(self):
                global deger_gen, deger_S
                deger_gen, deger_S = self.gen_ismi.get(), self.S_pu.get()
                self.kkk = tk.Label(temel, text=f'{deger_gen}\n{deger_S}\n{deger_faz}', font=(None, 8)).place(x=a + 50, y=b + 10)
                self.gen_entry.delete(0, tk.END)
                self.S_entry.delete(0, tk.END)
                generator[f'{a},{b}'][1] = deger_gen
                generator[f'{a},{b}'][2] = deger_S
                print(generator)
                self.ttt.destroy()

            def Ikinci_ekran(self):
                self.Ikinci_ekran_i = tk.Toplevel(temel)
                self.Ikinci_ekran_i.geometry('200x200')

                tk.Label(self.Ikinci_ekran_i, text='İsim : \n\nS Vpu : ').place(x=20, y=20)
                self.gen_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.gen_ismi)
                self.gen_entry.place(x=90, y=23)
                self.S_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.S_pu)
                self.S_entry.place(x=90, y=53)
                tk.Button(self.Ikinci_ekran_i, text='Değiştir', command=Is_gen.Degistir).place(x=120, y=140)

        k = False
        for i in gen_koor:
            if i[0] - 90 <= a <= i[0] + 90 and i[1] - 90 <= b <= i[1] + 90:
                k = False
            else:
                k = True
        if k == True:
            Ana_ekran.create_circle(a, b, 35, width=2)
            Ana_ekran.create_circle(a + 35, b, 3)
            Ana_ekran.create_circle(a - 35, b, 3)
            Ana_ekran.create_line(a - 20, b + 7, a - 10, b - 15, a + 10, b + 15, a + 20, b - 7, smooth=1, width=2)
            gen_koor.append([a,b])
            Gen = Is_gen()
            Gen.Gen_adi()

    Ana_ekran.bind('<ButtonPress-1>', Generator_tanimla)

def Cozum():
    print(deger_gen, deger_S)


tk.Button(temel, text='Bara', command=Bara).place(x=15, y =30)

tk.Button(temel, text='Hat', command=Hat).place(x=15, y =60)

tk.Button(temel,text='Çözüm', command=Cozum).place(x=15, y =90)

tk.Button(temel, text='Generator', command=Generator).place(x=15, y=120)

tk.Button(temel, text='Trafo', command=Trafo).place(x=15, y=150)




temel.mainloop()
