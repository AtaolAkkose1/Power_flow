import tkinter as tk
import numpy as np
import math;
import cmath;
import numpy.linalg
import itertools
import warnings
warnings.simplefilter("ignore", np.ComplexWarning)

j = (-1)**0.5
wdt, hgt = 1920, 1080
temel = tk.Tk()
Ana_ekran = tk.Canvas(temel, width=wdt, height=hgt, bg='white')
Ana_ekran.pack()
dugum_nok = []

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

bara_dugum, bara, bara_koor, baralar, bara_baglanti = [], [[0, 0, 0, 0]], {}, {}, {}
koor, hat, hatlar, hat_koor, baglanti, hat_canvas, hat_boy = [], [], {}, {}, {}, [], [0]
trafo, trafo_koor, trafolar, trafo_baglanti = [[0, 0]], {}, {}, {}
gen, gen_koor, genler, generator, gen_baglanti = [[0,0]], {}, {}, {}, {}
yuk_koor, yukler = [], {}

def Bara():
    def Bara_tanimla(e):
        a = e.x
        b = e.y
        a = a - (a*10)%10
        b = b - (b*10)%10

        class Is_bara:
            def __init__(self):
                self.Bara_ismi = tk.StringVar()
                self.Bara_ismi.set(baralar[f'{a},{b}'][1])
                self.V_pu = tk.StringVar()
                self.V_pu.set(baralar[f'{a},{b}'][2])
                self.Faz_pu = tk.StringVar()
                self.Faz_pu.set(baralar[f'{a},{b}'][3])
                self.P_var, self.Q_var, self.V_var, self.F_var = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()

            def Bara_adi(self):
                self.kkk = tk.Label(temel, text='İsim : \nBirim Vpu : \nFaz Açısı : ', font=(None, 8))
                self.ttt = tk.Label(temel, text=f'Bara{len(bara) - 1}\n 1 \n 0 ', font=(None, 8))
                return self.kkk, self.ttt

            def Degistir(self):
                global deger_isim, deger_V, deger_faz, deg_P, deg_Q, deg_V, deg_F
                deger_isim, deger_V, deger_faz = self.Bara_ismi.get(), self.V_pu.get(), self.Faz_pu.get()
                deg_P, deg_Q, deg_V, deg_F = self.P_var.get(), self.Q_var.get(), self.V_var.get(), self.F_var.get()
                baralar[f'{a},{b}'][1] = deger_isim
                baralar[f'{a},{b}'][2] = float(deger_V)
                baralar[f'{a},{b}'][3] = float(deger_faz)
                baralar[f'{a},{b}'][6] = str(deg_P)+str(deg_Q)+str(deg_V)+str(deg_F)
                tk.Label(temel, text=f'{deger_isim}\n{deger_V}\n{deger_faz}', font=(None, 8)).place(x=a + 50, y=b + 10)
                self.ttt.destroy()

            def Ikinci_ekran(self):
                self.Ikinci_ekran_i = tk.Toplevel(temel)
                self.Ikinci_ekran_i.geometry('170x200')

                tk.Label(self.Ikinci_ekran_i, text='İsim : \n\nBirim Vpu : \n\nFaz Açısı : \n\nReferans : ').place(x=20, y=20)
                self.bara_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.Bara_ismi)
                self.bara_entry.place(x=90, y=23)
                self.V_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.V_pu)
                self.V_entry.place(x=90, y=53)
                self.faz_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.Faz_pu)
                self.faz_entry.place(x=90, y=83)

                self.P_var.set(baralar[f'{a},{b}'][6][0])
                self.Q_var.set(baralar[f'{a},{b}'][6][1])
                self.V_var.set(baralar[f'{a},{b}'][6][2])
                self.F_var.set(baralar[f'{a},{b}'][6][3])

                self.chk_1 = tk.Checkbutton(self.Ikinci_ekran_i, text='P', variable=self.P_var, onvalue=1, offvalue=0, height=2)
                self.chk_1.place(x=10, y=133)
                self.chk_2 = tk.Checkbutton(self.Ikinci_ekran_i, text='Q', variable=self.Q_var, onvalue=1, offvalue=0, height=2)
                self.chk_2.place(x=50, y=133)
                self.chk_3 = tk.Checkbutton(self.Ikinci_ekran_i, text='V', variable=self.V_var, onvalue=1, offvalue=0, height=2)
                self.chk_3.place(x=90, y=133)
                self.chk_4 = tk.Checkbutton(self.Ikinci_ekran_i, text='F', variable=self.F_var, onvalue=1, offvalue=0, height=2)
                self.chk_4.place(x=130, y=133)
                tk.Button(self.Ikinci_ekran_i, text='Değiştir', command=self.Degistir).place(x=110, y=170)

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

            Ana_ekran.create_circle(a - 2.5, b - 37.5, 4, fill='gray')
            Ana_ekran.create_circle(a - 2.5, b, 4, fill='gray')
            Ana_ekran.create_circle(a - 2.5, b - 75, 4, fill='gray')
            dugum_nok.append([a - 2.5, b - 37.5])
            dugum_nok.append([a - 2.5, b])
            dugum_nok.append([a - 2.5, b - 75])
            bara_dugum.append([a - 2.5, b - 37.5])
            bara_dugum.append([a - 2.5, b])
            bara_dugum.append([a - 2.5, b - 75])
            bara_koor.update({f'Bara{len(bara) - 1}':[a - 2.5, b - 37.5, a - 2.5, b, a - 2.5, b - 75]})
            baralar.update({f'{a},{b}': [f'Bara{len(bara) - 1}', f'Bara{len(bara) - 1}', 1, 0, 0, 0, '0000']})
            Is = Is_bara()
            Is.Bara_adi()[0].place(x=a-15, y=b + 10)
            Is.Bara_adi()[1].place(x=a+40, y=b+10)
            tk.Button(temel, text='D', command=Is.Ikinci_ekran).place(x=a - 35, y=b + 7)

    Ana_ekran.bind('<ButtonPress-1>', Bara_tanimla)

def Hat():
    hat_i = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
    cizgi = []
    def Hat_dugum(e):
        hat_i['x1'] = e.x
        hat_i['y1'] = e.y
        hat_i['x1'] = hat_i['x1'] - (hat_i['x1']*10)%10
        hat_i['y1'] = hat_i['y1'] - (hat_i['y1']*10)%10
        for i in bara_dugum:
            if i[0]-5 <= hat_i['x1'] <= i[0]+5:
                hat_i['x1'] = i[0]
            if i[1]-5 <= hat_i['y1'] <= i[1]+5:
                hat_i['y1'] = i[1]
        cizgi.append(Ana_ekran.create_line(hat_i['x1'], hat_i['y1'], hat_i['x1'], hat_i['y1'], fill='orange', width=2))
        koor.append([hat_i['x1'], hat_i['y1']])

    def Surukle(e):
        hat_i['x2'] = e.x
        hat_i['y2'] = e.y
        Ana_ekran.coords(cizgi[-1], hat_i['x1'], hat_i['y1'], hat_i['x2'], hat_i['y2'])
        koor.append([hat_i['x2'], hat_i['y2']])

    def Olustur(e):
        a = e.x
        b = e.y
        class Is_hat:
            def __init__(self):
                self.hat_ismi = tk.StringVar(value=hatlar[f'{xn1}, {yn1}'][1])
                self.emp = tk.IntVar()
                self.z_reel, self.z_imag = tk.StringVar(), tk.StringVar()
                self.y_reel, self.y_imag = tk.StringVar(), tk.StringVar()

            def Hat_adi(self):
                self.ttt = tk.Label(temel, text=f'İsim :\nZ ohm :\nY mho :')
                self.ppp = tk.Label(temel, text=f'Hat{len(hat)}\n0\nsonsuz')
                return self.ttt, self.ppp

            def Degistir(self):
                global hat_i, z_reel_i, y_reel_i, z_im_i, y_im_i
                hat_i, z_reel_i, y_reel_i, z_im_i, y_im_i = self.hat_ismi.get(), self.z_reel.get(), self.y_reel.get(), self.z_imag.get(), self.y_imag.get()

                if self.emp.get() != 1:
                    Z_ri = round(float(z_reel_i), 3) + j * round(float(z_im_i), 3)
                    Y_ri = complex(1 / Z_ri)
                    Y_ri = round(Y_ri.real, 3) + j * round(Y_ri.imag, 3)
                else:
                    Y_ri = round(float(y_reel_i), 3) + j * round(float(y_im_i), 3)
                    Z_ri = complex(1 / Y_ri)
                    Z_ri = round(Z_ri.real, 3) + j * round(Z_ri.imag, 3)
                hatlar[f'{xn1}, {yn1}'][1] = hat_i
                hatlar[f'{xn1}, {yn1}'][2] = Z_ri
                hatlar[f'{xn1}, {yn1}'][3] = Y_ri
                tk.Label(temel, text=f'{hat_i}\n{Z_ri}\n{Y_ri}').place(x=xn1 + 45, y=yn1)
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

                tk.Button(self.ikinci_ekran, text='Değiştir', command=self.Degistir).place(x=115, y=140)

        global place_n
        xn1, xn2, yn1, yn2 = [0, 0, 0, 0]
        for i in cizgi:
            Ana_ekran.delete(i)
        for i in dugum_nok:
            if i[0] - 5 >= koor[1][0] or koor[1][0] >= i[0] + 5:
                pass
            else:
                xn1 = i[0]
            if i[1] - 5 >= koor[1][1] or koor[1][1] >= i[1] + 5:
                pass
            else:
                yn1 = i[1]
            if i[0] - 5 >= koor[len(koor) - 1][0] or koor[len(koor) - 1][0] >= i[0] + 5:
                pass
            else:
                xn2 = i[0]
            if i[1] - 5 >= koor[len(koor) - 1][1] or koor[len(koor) - 1][1] >= i[1] + 5:
                pass
            else:
                yn2 = i[1]
        koor.clear()

        if abs(xn1 - xn2) > abs(yn1 - yn2):
            Ana_ekran.create_line(xn1, yn1, xn1+(abs(xn1-xn2)/2), yn1, fill='black', width=1)
            Ana_ekran.create_line(xn1+(abs(xn1-xn2)/2), yn1, xn1 + (abs(xn1 - xn2) / 2), yn2, fill='black', width=1)
            Ana_ekran.create_line(xn1+(abs(xn1-xn2)/2), yn2, xn2, yn2, fill='black', width=1)
            place_n = [xn1+(abs(xn1 - xn2)/2)-10, (yn1+yn2)/2]

        if abs(xn1 - xn2) < abs(yn1 - yn2):
            Ana_ekran.create_line(xn1, yn1, xn1, yn1+(abs(yn1-yn2)/2), fill='black', width=1)
            Ana_ekran.create_line(xn1, yn1+(abs(yn1-yn2)/2), xn2, yn1+(abs(yn1-yn2)/2), fill='black', width=1)
            Ana_ekran.create_line(xn2, yn1+(abs(yn1-yn2)/2), xn2, yn2, fill='black', width=1)
            place_n = [(xn1+xn2)/2, yn1 + (abs(yn1 - yn2)/2)-10]
        baglanti.update({f'{xn1}, {yn1}':[xn1, yn1, xn2, yn2, 0, 0]})

        if [xn1, yn1] in bara_dugum:
            if [xn2, yn2] in bara_dugum:
                hat.append([xn1, yn1, xn2, yn2])
                hat_koor.update({f'Hat{len(hat)}': [xn1, yn1, xn2, yn2]})
                hatlar.update({f'{xn1}, {yn1}': [f'Hat{len(hat)}',f'Hat{len(hat)}', 0, 0, 0, 0]})
                Is_hat = Is_hat()
                Is_hat.Hat_adi()[0].place(x=place_n[0], y=place_n[1])
                Is_hat.Hat_adi()[1].place(x=place_n[0] + 45, y=place_n[1])
                tk.Button(temel, text='D', command=Is_hat.Ikinci_ekran).place(x=place_n[0] - 25, y=place_n[1])
                for i, k in itertools.product(bara_koor.keys(), hat_koor.keys()):
                    if bara_koor[i][0] == hat_koor[k][0] and bara_koor[i][1] == hat_koor[k][1]:
                        hatlar[f'{hat_koor[k][0]}, {hat_koor[k][1]}'][4] = i
                    if bara_koor[i][0] == hat_koor[k][2] and bara_koor[i][1] == hat_koor[k][3]:
                        hatlar[f'{hat_koor[k][0]}, {hat_koor[k][1]}'][5] = i
                    if bara_koor[i][2] == hat_koor[k][0] and bara_koor[i][3] == hat_koor[k][1]:
                        hatlar[f'{hat_koor[k][0]}, {hat_koor[k][1]}'][4] = i
                    if bara_koor[i][2] == hat_koor[k][2] and bara_koor[i][3] == hat_koor[k][3]:
                        hatlar[f'{hat_koor[k][0]}, {hat_koor[k][1]}'][5] = i
                    if bara_koor[i][4] == hat_koor[k][0] and bara_koor[i][5] == hat_koor[k][1]:
                        hatlar[f'{hat_koor[k][0]}, {hat_koor[k][1]}'][4] = i
                    if bara_koor[i][4] == hat_koor[k][2] and bara_koor[i][5] == hat_koor[k][3]:
                        hatlar[f'{hat_koor[k][0]}, {hat_koor[k][1]}'][5] = i

        for i, k in itertools.product(bara_koor.keys(), baglanti.keys()):
            if bara_koor[i][0] == baglanti[k][0] and bara_koor[i][1] == baglanti[k][1]:
                bara_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
            if bara_koor[i][0] == baglanti[k][2] and bara_koor[i][1] == baglanti[k][3]:
                bara_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
            if bara_koor[i][2] == baglanti[k][0] and bara_koor[i][3] == baglanti[k][1]:
                bara_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
            if bara_koor[i][2] == baglanti[k][2] and bara_koor[i][3] == baglanti[k][3]:
                bara_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
            if bara_koor[i][4] == baglanti[k][0] and bara_koor[i][5] == baglanti[k][1]:
                bara_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}': i})
            if bara_koor[i][4] == baglanti[k][2] and bara_koor[i][5] == baglanti[k][3]:
                bara_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
        for i, k in itertools.product(trafo_koor.keys(), baglanti.keys()):
            if trafo_koor[i][0] == baglanti[k][0] and trafo_koor[i][1] == baglanti[k][1]:
                trafo_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
            if trafo_koor[i][0] == baglanti[k][2] and trafo_koor[i][1] == baglanti[k][3]:
                trafo_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
            if trafo_koor[i][2] == baglanti[k][0] and trafo_koor[i][3] == baglanti[k][1]:
                trafo_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
            if trafo_koor[i][2] == baglanti[k][2] and trafo_koor[i][3] == baglanti[k][3]:
                trafo_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}':i})
        for i, k in itertools.product(gen_koor.keys(), baglanti.keys()):
            if gen_koor[i][0] == baglanti[k][0] and gen_koor[i][1] == baglanti[k][1]:
                gen_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}': i})
            if gen_koor[i][0] == baglanti[k][2] and gen_koor[i][1] == baglanti[k][3]:
                gen_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}': i})
            if gen_koor[i][2] == baglanti[k][0] and gen_koor[i][1] == baglanti[k][1]:
                gen_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}': i})
            if gen_koor[i][2] == baglanti[k][2] and gen_koor[i][1] == baglanti[k][3]:
                gen_baglanti.update({f'{baglanti[k][0]}, {baglanti[k][1]}': i})

    Ana_ekran.bind('<ButtonPress-1>', Hat_dugum)
    Ana_ekran.bind('<B1-Motion>', Surukle)
    Ana_ekran.bind('<ButtonRelease-1>', Olustur)

def Trafo():
    def Trafo_tanimla(e):
        a = e.x
        b = e.y
        a = a - (a*10)%10
        b = b - (a*10)%10
        class Is_trafo:
            def __init__(self):
                self.trafo_ismi = tk.StringVar()
                self.emp = tk.IntVar()
                self.z_reel, self.z_imag = tk.IntVar(), tk.IntVar()
                self.y_reel, self.y_imag = tk.IntVar(), tk.IntVar()

            def Trafo_adi(self):
                self.ppp = tk.Label(temel, text='İsim : \nZ ohm_pu : \nY mho_pu : ', font=(None, 8))
                self.ttt = tk.Label(temel, text=f'Tr{len(trafo)}\n0 \nsonsuz ', font=(None, 8))
                return self.ppp, self.ttt

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
                trafolar[f'{a},{b}'][1] = tr_i
                trafolar[f'{a},{b}'][2] = Z_ri
                trafolar[f'{a},{b}'][3] = Y_ri

                for i in trafo_baglanti.keys():
                    if trafolar[f'{a},{b}'][0] == trafo_baglanti[i]:
                        if trafolar[f'{a},{b}'][4] == 0:
                            trafolar[f'{a},{b}'][4] = bara_baglanti[i]
                        else:
                            trafolar[f'{a},{b}'][5] = bara_baglanti[i]
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

                tk.Button(self.ikinci_ekran, text='Değiştir', command=self.Degistir).place(x=115, y=140)

        k = False
        for i in trafo:
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
            Is_trafo.Trafo_adi()[0].place(x=a-5, y=b+10)
            Is_trafo.Trafo_adi()[1].place(x=a+50, y=b + 10)
            trafo.append([a, b])
            trafo_koor.update({f'Tr{len(trafo)-1}':[a - 55, b - 25, a + 20, b - 25]})
            dugum_nok.append([a - 55, b - 25])
            dugum_nok.append([a + 20, b - 25])
            trafolar.update({f'{a},{b}':[f'Tr{len(trafo)-1}', f'Tr{len(trafo)-1}', 1, 0, 0, 0]})

            tk.Button(temel, text='D', command=Is_trafo.Ikinci_ekran).place(x=a - 25, y=b)
    Ana_ekran.bind('<ButtonPress-1>', Trafo_tanimla)

def Generator():
    def Generator_tanimla(e):
        a = e.x
        b = e.y
        a = a - (a * 10) % 10
        b = b - (a * 10) % 10
        class Is_gen:
            def __init__(self):
                self.gen_ismi = tk.StringVar()
                self.S_pu = tk.StringVar()
                self.P_pu, self.Q_pu, self.V_pu, self.F_pu = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
                self.ref_P, self.ref_Q, self.ref_V, self.ref_F = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()

            def Gen_adi(self):
                self.ppp = tk.Label(temel, text='İsim : \nBirim Spu : ', font=(None, 8))
                self.ttt = tk.Label(temel, text=f'G{len(gen)-1}\n 1 ', font=(None, 8))
                return self.ppp, self.ttt

            def Degistir(self):
                global deger_gen, deger_S
                deger_gen, deger_S = self.gen_ismi.get(), self.S_pu.get()
                self.kkk = tk.Label(temel, text=f'{deger_gen}\n{deger_S}', font=(None, 8)).place(x=a + 50, y=b + 10)
                self.gen_entry.delete(0, tk.END)
                self.S_entry.delete(0, tk.END)
                generator[f'{a},{b}'][1] = deger_gen
                generator[f'{a},{b}'][2] = float(deger_S)

                for i, k in itertools.product(bara_baglanti.keys(), gen_baglanti.keys()):
                    if i == k:
                        x_i = str(bara_koor[bara_baglanti[i]][2]+2.5).replace('.0', '')
                        y_i = bara_koor[bara_baglanti[i]][3]
                        baralar[f'{x_i},{y_i}'][6] = str(self.ref_P.get())+str(self.ref_Q.get())+str(self.ref_V.get())+str(self.ref_F.get())
                        if self.P_pu.get() != '':
                            baralar[f'{x_i},{y_i}'][4] = float(self.P_pu.get())
                            baralar[f'{x_i},{y_i}'][6][0] = str(1)
                        if self.Q_pu.get() != '':
                            baralar[f'{x_i},{y_i}'][5] = float(self.Q_pu.get())
                            baralar[f'{x_i},{y_i}'][6][1] = str(1)
                        if self.V_pu.get() != '':
                            baralar[f'{x_i},{y_i}'][2] = float(self.V_pu.get())
                            baralar[f'{x_i},{y_i}'][6][2] = str(1)
                        if self.F_pu.get() != '':
                            baralar[f'{x_i},{y_i}'][3] = float(self.F_pu.get())
                            baralar[f'{x_i},{y_i}'][6][3] = str(1)
                self.ttt.destroy()

            def Ref(self):
                if self.ref_P.get() == 1:
                    self.P_entry.configure(state='normal')
                else:
                    self.P_entry.configure(state='disabled')
                if self.ref_Q.get() == 1:
                    self.Q_entry.configure(state='normal')
                else:
                    self.Q_entry.configure(state='disabled')
                if self.ref_V.get() == 1:
                    self.V_entry.configure(state='normal')
                else:
                    self.V_entry.configure(state='disabled')
                if self.ref_F.get() == 1:
                    self.F_entry.configure(state='normal')
                else:
                    self.F_entry.configure(state='disabled')

            def Ikinci_ekran(self):
                self.Ikinci_ekran_i = tk.Toplevel(temel)
                self.Ikinci_ekran_i.geometry('200x240')

                tk.Label(self.Ikinci_ekran_i, text='İsim : \n\nS Vpu : ').place(x=20, y=20)
                self.gen_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.gen_ismi)
                self.gen_entry.place(x=90, y=23)
                self.S_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.S_pu)
                self.S_entry.place(x=90, y=53)

                self.P_entry = tk.Entry(self.Ikinci_ekran_i, textvariable=self.P_pu, width=8)
                self.P_entry.place(x=90, y=83)
                self.Q_entry = tk.Entry(self.Ikinci_ekran_i, textvariable=self.Q_pu, width=8)
                self.Q_entry.place(x=90, y=113)
                self.V_entry = tk.Entry(self.Ikinci_ekran_i, textvariable=self.V_pu, width=8)
                self.V_entry.place(x=90, y=143)
                self.F_entry = tk.Entry(self.Ikinci_ekran_i, textvariable=self.F_pu, width=8)
                self.F_entry.place(x=90, y=173)
                self.P_entry.configure(state='disabled')
                self.Q_entry.configure(state='disabled')
                self.V_entry.configure(state='disabled')
                self.F_entry.configure(state='disabled')

                tk.Checkbutton(self.Ikinci_ekran_i, text='P', variable=self.ref_P, offvalue=0, onvalue=1, command=self.Ref).place(x=20, y=83)
                tk.Checkbutton(self.Ikinci_ekran_i, text='Q', variable=self.ref_Q, offvalue=0, onvalue=1, command=self.Ref).place(x=20, y=113)
                tk.Checkbutton(self.Ikinci_ekran_i, text='V', variable=self.ref_V, offvalue=0, onvalue=1, command=self.Ref).place(x=20, y=143)
                tk.Checkbutton(self.Ikinci_ekran_i, text='F', variable=self.ref_F, offvalue=0, onvalue=1, command=self.Ref).place(x=20, y=173)
                tk.Button(self.Ikinci_ekran_i, text='Değiştir', command=self.Degistir).place(x=120, y=205)

        k = False
        for i in gen:
            if i[0] - 90 <= a <= i[0] + 90 and i[1] - 90 <= b <= i[1] + 90:
                k = False
            else:
                k = True
        if k == True:

            Ana_ekran.create_circle(a, b, 35, width=2)
            Ana_ekran.create_circle(a + 35, b, 3)
            Ana_ekran.create_circle(a - 35, b, 3)
            Ana_ekran.create_line(a - 20, b + 7, a - 10, b - 15, a + 10, b + 15, a + 20, b - 7, smooth=1, width=2)
            gen.append([a,b])
            gen_koor.update({f'G{len(gen)-1}':[a + 35, b, a - 35]})
            genler.update({f'{a},{b}':[a + 35, b, a - 35, 0, 0, 0]})
            generator.update({f'{a},{b}':[f'G{len(gen)-1}', f'G{len(gen)-1}', 0, 0, 0]})
            dugum_nok.append([a+35, b])
            dugum_nok.append([a-35, b])
            Gen = Is_gen()
            Gen.Gen_adi()[0].place(x=a-25, y=b+40)
            Gen.Gen_adi()[1].place(x=a+30, y=b + 40)
            tk.Button(temel, text='D', command=Gen.Ikinci_ekran).place(x=a-50, y=b+45)

    Ana_ekran.bind('<ButtonPress-1>', Generator_tanimla)

def Yuk():
    def Yuk_tanimla(e):
        a = e.x
        b = e.y
        a = a - (a * 10) % 10
        b = b - (a * 10) % 10
        class Is_yuk:
            def __init__(self):
                self.yuk_ismi = tk.StringVar()
                self.P_pu = tk.StringVar()
                self.Q_pu = tk.StringVar()

            def Yuk_adi(self):
                self.ppp = tk.Label(temel, text='İsim : \nBirim Ppu : \nBirim Qpu :', font=(None, 8))
                self.ttt = tk.Label(temel, text=f'Y{len(yuk_koor) - 1}\n 1 \n 1 ', font=(None, 8))
                return self.ppp, self.ttt

            def Degistir(self):
                global deger_yuk, deger_P, deger_Q
                deger_yuk, deger_P, deger_Q = self.yuk_ismi.get(), self.P_pu.get(), self.Q_pu.get()
                self.kkk = tk.Label(temel, text=f'{deger_yuk}\n{deger_P}\n{deger_Q}', font=(None, 8)).place(x=xn, y=yn)
                self.yuk_entry.delete(0, tk.END)
                self.P_entry.delete(0, tk.END)
                self.Q_entry.delete(0, tk.END)
                yukler[f'{a},{b}'][1] = deger_yuk
                yukler[f'{a},{b}'][2] = float(deger_P)
                yukler[f'{a},{b}'][3] = float(deger_Q)
                st_b = [b, b + 37.5, b + 75]
                st_a = str(a + 2.5).replace('.0', '')
                for i in st_b:
                    try:
                        baralar[f'{st_a},{i}'][4] = -float(deger_P)
                        baralar[f'{st_a},{i}'][5] = -float(deger_Q)
                    except KeyError:
                        pass
                self.ttt.destroy()

            def Ikinci_ekran(self):
                self.Ikinci_ekran_i = tk.Toplevel(temel)
                self.Ikinci_ekran_i.geometry('200x200')

                tk.Label(self.Ikinci_ekran_i, text='İsim : \n\nP pu : \n\nQ pu :').place(x=20, y=20)
                self.yuk_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.yuk_ismi)
                self.yuk_entry.place(x=90, y=23)
                self.P_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.P_pu)
                self.P_entry.place(x=90, y=53)
                self.Q_entry = tk.Entry(self.Ikinci_ekran_i, width=10, textvariable=self.Q_pu)
                self.Q_entry.place(x=90, y=83)
                tk.Button(self.Ikinci_ekran_i, text='Değiştir', command=self.Degistir).place(x=120, y=140)

        for i in bara_dugum:
            if i[0]-5 <= a <= i[0]+5:
                a = i[0]
            if i[1]-5 <= b <= i[1]+5:
                b = i[1]
                st_b = [b, b+37.5, b+75]
        st_a = str(a+2.5).replace('.0', '')
        for i in st_b:
            try:
                baralar[f'{st_a},{i}'][6] = '1100'
            except KeyError:
                pass
        if a > wdt/2:
            xn, yn = a+120, b-60
            Ana_ekran.create_line(a, b, a+50, b, width=2)
            Ana_ekran.create_polygon(a+50,b, a+40,b-10, a+40,b+10, fill='black')
            Is_yuk = Is_yuk()
            Is_yuk.Yuk_adi()[0].place(x=a+25, y=b-60)
            Is_yuk.Yuk_adi()[1].place(x=a+80, y=b-60)
            tk.Button(temel, text='D', command=Is_yuk.Ikinci_ekran).place(x=a+120, y=b-60)
        else:
            xn, yn = a - 35, b - 60
            Ana_ekran.create_line(a, b, a - 50, b, width=2)
            Ana_ekran.create_polygon(a + 50, b, a - 40, b - 10, a - 40, b + 10, fill='black')
            Is_yuk = Is_yuk()
            Is_yuk.Yuk_adi()[0].place(x=a - 90, y=b - 60)
            Is_yuk.Yuk_adi()[1].place(x=a - 35, y=b - 60)
            tk.Button(temel, text='D', command=Is_yuk.Ikinci_ekran).place(x=a - 120, y=b - 60)
        yuk_koor.append([a, b])
        yukler.update({f'{a},{b}':[f'Y{len(yuk_koor)}',f'Y{len(yuk_koor)}', 0, 0]})
    Ana_ekran.bind('<ButtonPress-1>', Yuk_tanimla)

def Cozum():

    Toplam_Bara, Bilinmeyen_Bara, Referans_bara, Baglantilar = ({}, {}, {}, {})
    Bara_Adi, Hatlar, Trafolar, Fonksiyonlar_matrisi, Bilinmeyenler_matrisi, Gucler = ([], [], [], [], [], [])

    for i in baralar.values():
        Bara_Adi.append(i[0])
        Toplam_Bara.update({i[0]:[i[2], i[3], 0, i[4], i[5], i[6]]})
        Baglantilar.update({f'{i[0]}-{i[0]}': 0})
        if (i[6][2] != str(0) or i[6][3] != str(0)):
            Referans_bara.update({i[0]:[i[2], i[3], 0, i[4], i[5], i[6]]})
        else:
            Bilinmeyen_Bara.update({i[0]:[i[2], i[3], 0, i[4], i[5], i[6]]})

    for i in hatlar.values():
        Hatlar.append([i[4], i[5], complex(i[3])])
        Baglantilar.update({f'{i[4]}-{i[5]}': complex(i[3])})
        Baglantilar.update({f'{i[5]}-{i[4]}': complex(i[3])})


    for i in trafolar.values():
        Trafolar.append([i[4], i[5], complex(i[2])])
        Baglantilar.update({f'{i[4]}-{i[5]}': complex(i[3])})
        Baglantilar.update({f'{i[5]}-{i[4]}': complex(i[3])})

    S_Taban = 100
    Epsilon = 0.00025

    Y = np.zeros((len(Toplam_Bara), len(Toplam_Bara)), dtype="complex_")
    ik, ii = (0, 0)
    for i, k in itertools.product(range(1, len(Toplam_Bara) + 1), range(1, len(Toplam_Bara) + 1)):
        a = i
        if (f'Bara{i}-Bara{k}' in Baglantilar):
            try:
                ik += Baglantilar[f'Bara{i}-Bara{k}']
            except ZeroDivisionError:
                ik += 0
        Y[(i - 1), (k - 1)] += -ik
        Y[(i - 1), (i - 1)] += ik
        ik = 0

    for i in Bilinmeyen_Bara.keys():
        i = i.replace('Bara', '')
        Bilinmeyenler_matrisi.append([f'V{i}', f'V{i}rad'])
        Fonksiyonlar_matrisi.append([f'P{i}', f'Q{i}'])
    for i in Referans_bara.keys():
        a = i.replace('Bara', '')
        if (Referans_bara[i][5] == '1010'):
            Bilinmeyenler_matrisi.append([f'V{a}rad'])
            Fonksiyonlar_matrisi.append([f'P{a}'])
        if (Referans_bara[i][5] == '1001'):
            Bilinmeyenler_matrisi.append([f'V{a}'])
            Fonksiyonlar_matrisi.append([f'P{a}'])
        if (Referans_bara[i][5] == '0110'):
            Bilinmeyenler_matrisi.append([f'V{a}rad'])
            Fonksiyonlar_matrisi.append([f'Q{a}'])
        if (Referans_bara[i][5] == '0101'):
            Bilinmeyenler_matrisi.append([f'V{a}'])
            Fonksiyonlar_matrisi.append([f'Q{a}'])
        if (Referans_bara[i][5] == '1100'):
            Fonksiyonlar_matrisi.append([f'P{a}'])
            Fonksiyonlar_matrisi.append([f'Q{a}'])

    Fonksiyonlar_matrisi.sort()
    Bilinmeyenler_matrisi.sort()
    F_m, B_m = (list(itertools.chain.from_iterable(Fonksiyonlar_matrisi)),
                list(itertools.chain.from_iterable(Bilinmeyenler_matrisi)))
    B_m_dic, F_m_dic = ({}, {})
    for i in range(len(B_m)):
        B_m_dic.update({B_m[i]: i})
    for i in range(len(F_m)):
        F_m_dic.update({F_m[i]: i})

    C = np.zeros((len(F_m), 1), dtype="complex_")
    for i in range(1, len(Toplam_Bara) + 1):
        if (f'P{i}' in F_m):
            C[F_m_dic[f'P{i}']] = (Toplam_Bara[f'Bara{i}'][3])
        if (f'Q{i}' in F_m):
            C[F_m_dic[f'Q{i}']] = (Toplam_Bara[f'Bara{i}'][4])
    C = np.array(C).reshape(-1, 1)
    
    dongu = 0
    while dongu != len(B_m):
        dongu = 0
        Fonksiyon, Jakobiyen = (
        np.zeros((len(F_m), 1), dtype='complex_'), np.zeros((len(F_m), len(B_m)), dtype='complex_'))
        for i, k in itertools.product(range(1, len(Toplam_Bara) + 1), range(1, len(Toplam_Bara) + 1)):
            if (f'Bara{i}-Bara{k}' in Baglantilar):
                (x1, x1rad, x2, x2rad) = (
                Toplam_Bara[f'Bara{i}'][0], Toplam_Bara[f'Bara{i}'][1], Toplam_Bara[f'Bara{k}'][0],
                Toplam_Bara[f'Bara{k}'][1])
                if (f'P{i}' in F_m):
                    if (i == k):
                        Fonksiyon[F_m_dic[f'P{i}'], 0] += (abs(x1 * x1 * Y[i - 1, k - 1]) * math.cos(
                            cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    else:
                        Fonksiyon[F_m_dic[f'P{i}'], 0] += (abs(x1 * x2 * Y[i - 1, k - 1]) * math.cos(
                            cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                if (f'Q{i}' in F_m):
                    if (i == k):
                        Fonksiyon[F_m_dic[f'Q{i}'], 0] += -(abs(x1 * x1 * Y[i - 1, k - 1]) * math.sin(
                            cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    else:
                        Fonksiyon[F_m_dic[f'Q{i}'], 0] += -(abs(x1 * x2 * Y[i - 1, k - 1]) * math.sin(
                            cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
        Delta_C = C - Fonksiyon

        X = np.zeros((len(F_m), 1), dtype="complex_")
        for i in range(1, len(Toplam_Bara) + 1):
            if (f'V{i}' in B_m):
                X[B_m_dic[f'V{i}']] = (Toplam_Bara[f'Bara{i}'][0])
            if (f'V{i}rad' in B_m):
                X[B_m_dic[f'V{i}rad']] = (Toplam_Bara[f'Bara{i}'][1])
        X = np.array(X).reshape(-1, 1)

        for i, k in itertools.product(range(1, len(Toplam_Bara) + 1), range(1, len(Toplam_Bara) + 1)):
            if ((f'V{i}' in B_m or f'V{i}rad' in B_m) and f'Bara{i}-Bara{k}' in Baglantilar):
                (x1, x1rad, x2, x2rad) = (
                Toplam_Bara[f'Bara{i}'][0], Toplam_Bara[f'Bara{i}'][1], Toplam_Bara[f'Bara{k}'][0],
                Toplam_Bara[f'Bara{k}'][1])
                if (f'P{i}' in F_m):
                    if (f'V{i}' in B_m):
                        if (i == k):
                            Jakobiyen[F_m_dic[f'P{i}'], B_m_dic[f'V{i}']] += (abs(2 * x1 * Y[i - 1, k - 1]) * math.cos(
                                cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        else:
                            Jakobiyen[F_m_dic[f'P{i}'], B_m_dic[f'V{i}']] += (abs(x2 * Y[i - 1, k - 1]) * math.cos(
                                cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    if (i != k and f'V{i}rad' in B_m):
                        Jakobiyen[F_m_dic[f'P{i}'], B_m_dic[f'V{i}rad']] += (abs(x1 * x2 * Y[i - 1, k - 1]) * math.sin(
                            cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    if (i != k and f'V{k}' in B_m):
                        Jakobiyen[F_m_dic[f'P{i}'], B_m_dic[f'V{k}']] += (
                                    abs(x1 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    if (i != k and f'V{k}rad' in B_m):
                        Jakobiyen[F_m_dic[f'P{i}'], B_m_dic[f'V{k}rad']] += -(abs(x1 * x2 * Y[i - 1, k - 1]) * math.sin(
                            cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                if (f'Q{i}' in F_m):
                    if (f'V{i}' in B_m):
                        if (i == k):
                            Jakobiyen[F_m_dic[f'Q{i}'], B_m_dic[f'V{i}']] += -(abs(2 * x1 * Y[i - 1, k - 1]) * math.sin(
                                cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        else:
                            Jakobiyen[F_m_dic[f'Q{i}'], B_m_dic[f'V{i}']] += -(abs(x2 * Y[i - 1, k - 1]) * math.sin(
                                cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    if (i != k and f'V{i}rad' in B_m):
                        Jakobiyen[F_m_dic[f'Q{i}'], B_m_dic[f'V{i}rad']] += (abs(x1 * x2 * Y[i - 1, k - 1]) * math.cos(
                            cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    if (i != k and f'V{k}' in B_m):
                        Jakobiyen[F_m_dic[f'Q{i}'], B_m_dic[f'V{k}']] += -(
                                    abs(x1 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    if (i != k and f'V{k}rad' in B_m):
                        Jakobiyen[F_m_dic[f'Q{i}'], B_m_dic[f'V{k}rad']] += -(abs(x1 * x2 * Y[i - 1, k - 1]) * math.cos(
                            cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))

        Inv_Jakobiyen = numpy.linalg.inv(Jakobiyen)
        Delta_X = np.zeros((len(Delta_C), len(Delta_C[0])))
        for i, t, k in itertools.product(range(len(Inv_Jakobiyen)), range(len(Delta_C[0])), range(len(Delta_C))):
            Delta_X[i][t] += Inv_Jakobiyen[i][k] * Delta_C[k][t]
        X = X + Delta_X

        X_dic = {B_m[i]: X[i] for i in range(len(X))}
        for i in range(1, len(Toplam_Bara) + 1):
            if (f'V{i}' in B_m):
                Toplam_Bara[f'Bara{i}'][0] = X_dic[f'V{i}'][0]
            if (f'V{i}rad' in B_m):
                Toplam_Bara[f'Bara{i}'][1] = X_dic[f'V{i}rad'][0]
        for i in Delta_C:
            if abs(i) <= Epsilon:
                dongu += 1

    P, Q = (np.zeros((len(Toplam_Bara), 1)), np.zeros((len(Toplam_Bara), 1)))
    for i, k in itertools.product(range(1, len(Toplam_Bara) + 1), range(1, len(Toplam_Bara) + 1)):
        if (f'Bara{i}-Bara{k}' in Baglantilar):
            (x1, x1rad, x2, x2rad) = (
            Toplam_Bara[f'Bara{i}'][0], Toplam_Bara[f'Bara{i}'][1], Toplam_Bara[f'Bara{k}'][0],
            Toplam_Bara[f'Bara{k}'][1])
            if (i == k):
                P[i - 1, 0] += abs(x1 * x1 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]))
                Q[i - 1, 0] += -(abs(x1 * x1 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1])))
            else:
                P[i - 1, 0] += abs(x1 * x2 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad)
                Q[i - 1, 0] += -(
                            abs(x1 * x2 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))

    S, I = (np.zeros((len(Toplam_Bara), len(Toplam_Bara)), dtype='complex_'),
            np.zeros((len(Toplam_Bara), len(Toplam_Bara)), dtype='complex_'))
    for i in range(len(Toplam_Bara)):
        print(f"P{i + 1} = {P[i]} pu.")
        print(f"Q{i + 1} = {Q[i]} pu.")
    for i in range(1, len(Toplam_Bara) + 1):
        Toplam_Bara[f'Bara{i}'][0] = Toplam_Bara[f'Bara{i}'][0] * (
                    math.cos(Toplam_Bara[f'Bara{i}'][1]) + math.sin(Toplam_Bara[f'Bara{i}'][1]) * (-1) ** 0.5)
        print(f'V{i} = ', Toplam_Bara[f'Bara{i}'][0])
    for i, k in itertools.product(range(1, len(Toplam_Bara) + 1), range(1, len(Toplam_Bara) + 1)):
        if (f'Bara{i}-Bara{k}' in Baglantilar):
            I[i - 1][k - 1] = (Toplam_Bara[f'Bara{i}'][0] - Toplam_Bara[f'Bara{k}'][0]) * Y[i - 1][k - 1]
            S[i - 1][k - 1] = (Toplam_Bara[f'Bara{i}'][0] * (I[i - 1][k - 1].conjugate())) * S_Taban
            print(f'I{i}{k} = ', I[i - 1][k - 1])
            print(f'S{i}{k} = ', S[i - 1][k - 1])
    Kayıplar = np.zeros((len(Toplam_Bara), len(Toplam_Bara)), dtype='complex_')
    for i, k in itertools.product(range(1, len(Toplam_Bara) + 1), range(1, len(Toplam_Bara) + 1)):
        if (f'Bara{i}-Bara{k}' in Baglantilar):
            Kayıplar[i - 1][k - 1] = S[i - 1][k - 1] + S[k - 1][i - 1]
            print(f'Kayıp{i}-{k}', Kayıplar[i - 1][k - 1])

bara_button = tk.Button(temel, text='Bara', command=Bara).place(x=15, y =15)

hat_button = tk.Button(temel, text='Hat', command=Hat).place(x=48, y =15)

cozum_button = tk.Button(temel,text='Çözüm', command=Cozum).place(x=77, y =15)

gen_button = tk.Button(temel, text='Generator', command=Generator).place(x=125, y=15)

trafo_button = tk.Button(temel, text='Trafo', command=Trafo).place(x=187, y=15)

yuk_button = tk.Button(temel, text='Yük', command=Yuk).place(x=225, y=15)

temel.mainloop()
