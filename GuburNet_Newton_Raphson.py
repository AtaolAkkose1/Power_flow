import numpy as np
import math;
import cmath;
import numpy.linalg
import itertools
import warnings
warnings.simplefilter("ignore", np.ComplexWarning)

j = (-1)**0.5
Total_Bus, Unknown_Bus, Reference_Bus, Connections  = ({}, {}, {}, {})
Bus_name, Lines, Trafo, Func_matrix, Unknown_matrix, Powers = ([], [], [], [], [], [])

class Guburcuk:
    def __init__(self, S_Base_MVA = 100, V_Base_kV = 154, Epsilon=0.00025):
        self.S_Base_MVA = S_Base_MVA
        self.V_Base_kV = V_Base_kV
        self.Epsilon = Epsilon
        self.Z_Base = self.V_Base_kV**2 / self.S_Base_MVA
        self.I_Base = self.S_Base_MVA / self.V_Base_kV

    def Def_Bus(self, bus_name=None, unit_Vpu=1.0, phase_diff=(0, 'R'), impedance=(0, 'pu'), active_power_P=(0, 'MW'), reactive_power_Q=(0, 'MVar'), bus_type=None, references=None):
        Bus_name.append(bus_name)
        if phase_diff[1] == 'd' or 'D':
            phase_diff = math.radians(phase_diff[0])
        else:
            phase_diff = phase_diff[0]
        if active_power_P[1] == 'pu':
            active_power_P = active_power_P[0]
        else:
            active_power_P = active_power_P[0] / self.S_Base_MVA
        if reactive_power_Q[1] == 'pu':
            reactive_power_Q = reactive_power_Q[0]
        else:
            reactive_power_Q = reactive_power_Q[0] / self.S_Base_MVA
        if impedance[1] == 'pu':
            impedance = impedance[0] * 100 / self.S_Base_MVA
        else:
            impedance = impedance[0] / self.Z_Base
        if (bus_type == None or bus_type == 'Load Bus'):
            active_power_P, reactive_power_Q = (active_power_P * -1, reactive_power_Q * -1)
        Total_Bus.update({bus_name: [unit_Vpu, phase_diff, complex(impedance), active_power_P, reactive_power_Q, [references]]})
        Connections.update({f'{bus_name}-{bus_name}': complex(impedance)})
        if (bus_type == 'Slack Bus' or bus_type == 'Generator Bus'):
            Reference_Bus.update({bus_name: [unit_Vpu, phase_diff, complex(impedance), active_power_P, reactive_power_Q, references]})
        else:
            Unknown_Bus.update({bus_name: [unit_Vpu, phase_diff, complex(impedance), active_power_P, reactive_power_Q]})

    def Def_Line(self, from_bus=None, to_bus=None, impedance=(0, 'pu')):
        if impedance[1] == 'pu':
            impedance = impedance[0] * 100 / self.S_Base_MVA
        else:
            impedance = impedance[0] / self.Z_Base
        Lines.append([from_bus, to_bus, complex(impedance)])
        Connections.update({f'{from_bus}-{to_bus}': complex(impedance)})
        Connections.update({f'{to_bus}-{from_bus}': complex(impedance)})

    def Def_Trafo(self, from_bus=None, to_bus=None, impedance=(0, 'pu'), high_vol=0, low_vol=0, apparent_power_S=0):
        if impedance[1] == 'pu':
            impedance = impedance[0] * 100 / self.S_Base_MVA
        else:
            impedance = impedance[0] / self.Z_Base
        Trafo.append([from_bus, to_bus, complex(impedance), high_vol, low_vol, apparent_power_S])
        Connections.update({f'{from_bus}-{to_bus}': complex(impedance)})
        Connections.update({f'{to_bus}-{from_bus}': complex(impedance)})

    def Solution(self):

        Y = np.zeros((len(Total_Bus), len(Total_Bus)), dtype="complex_")
        ik, ii = (0, 0)
        for i, k in itertools.product(range(1, len(Total_Bus) + 1), range(1, len(Total_Bus) + 1)):
            a = i
            if (f'Bus{i}-Bus{k}' in Connections):
                try:
                    ik += 1 / Connections[f'Bus{i}-Bus{k}']
                except ZeroDivisionError:
                    ik += 0
            Y[(i - 1), (k - 1)] += -ik
            Y[(i - 1), (i - 1)] += ik
            ik = 0

        for i in Unknown_Bus.keys():
            i = i.replace('Bus', '')
            Unknown_matrix.append([f'V{i}', f'V{i}rad'])
            Func_matrix.append([f'P{i}', f'Q{i}'])
        for i in Reference_Bus.keys():
            i = i.replace('Bus', '')
            for k in Total_Bus[f'Bus{i}'][5]:
                if ((k == 'P,V') or (k == 'Q,V') or (k == 'V,P') or (k == 'V,Q')):
                    Unknown_matrix.append([f'V{i}rad'])
                    for k in k.split(','):
                        if (k == 'P'):
                            Func_matrix.append([f'P{i}'])
                        elif (k == 'Q'):
                            Func_matrix.append([f'Q{i}'])
                elif ((k == 'P,Vrad') or (k == 'Q,Vrad') or (k == 'Vrad,P') or (k == 'Vrad,P')):
                    Unknown_matrix.append([f'V{i}'])
                    for k in k.split(','):
                        if (k == 'P'):
                            Func_matrix.append([f'P{i}'])
                        elif (k == 'Q'):
                            Func_matrix.append([f'Q{i}'])
        Func_matrix.sort()
        Unknown_matrix.sort()
        F_m, B_m = (list(itertools.chain.from_iterable(Func_matrix)), list(itertools.chain.from_iterable(Unknown_matrix)))
        B_m_dic, F_m_dic = ({}, {})
        for i in range(len(B_m)):
            B_m_i = {B_m[i]:i}
            B_m_dic.update(B_m_i)
        for i in range(len(F_m)):
            F_m_i = {F_m[i]:i}
            F_m_dic.update(F_m_i)

        C = np.zeros((len(F_m), 1), dtype="complex_")
        for i in range(1, len(Total_Bus) + 1):
            if (f'P{i}' in F_m):
                C[F_m_dic[f'P{i}']] = (Total_Bus[f'Bus{i}'][3])
            if (f'Q{i}' in F_m):
                C[F_m_dic[f'Q{i}']] = (Total_Bus[f'Bus{i}'][4])
        C = np.array(C).reshape(-1, 1)

        loop = 0
        while loop != len(B_m):
            loop = 0
            Function, Jacobi = (np.zeros((len(F_m), 1), dtype='complex_'), np.zeros((len(F_m), len(B_m)), dtype='complex_'))
            for i, k in itertools.product(range(1, len(Total_Bus) + 1), range(1, len(Total_Bus) + 1)):
                if (f'Bus{i}-Bus{k}' in Connections):
                    (x1, x1rad, x2, x2rad) = (Total_Bus[f'Bus{i}'][0], Total_Bus[f'Bus{i}'][1], Total_Bus[f'Bus{k}'][0], Total_Bus[f'Bus{k}'][1])
                    if (f'P{i}' in F_m):
                        if (i == k):
                            Function[F_m_dic[f'P{i}'], 0] += (abs(x1 * x1 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        else:
                            Function[F_m_dic[f'P{i}'], 0] += (abs(x1 * x2 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    if (f'Q{i}' in F_m):
                        if (i == k):
                            Function[F_m_dic[f'Q{i}'], 0] += -(abs(x1 * x1 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        else:
                            Function[F_m_dic[f'Q{i}'], 0] += -(abs(x1 * x2 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
            Delta_C = C - Function

            X = np.zeros((len(F_m), 1), dtype="complex_")
            for i in range(1, len(Total_Bus) + 1):
                if (f'V{i}' in B_m):
                    X[B_m_dic[f'V{i}']] = (Total_Bus[f'Bus{i}'][0])
                if (f'V{i}rad' in B_m):
                    X[B_m_dic[f'V{i}rad']] = (Total_Bus[f'Bus{i}'][1])
            X = np.array(X).reshape(-1, 1)

            for i, k in itertools.product(range(1, len(Total_Bus) + 1), range(1, len(Total_Bus) + 1)):
                if ((f'V{i}' in B_m or f'V{i}rad' in B_m) and f'Bus{i}-Bus{k}' in Connections):
                    (x1, x1rad, x2, x2rad) = (Total_Bus[f'Bus{i}'][0], Total_Bus[f'Bus{i}'][1], Total_Bus[f'Bus{k}'][0], Total_Bus[f'Bus{k}'][1])
                    if (f'P{i}' in F_m):
                        if (f'V{i}' in B_m):
                            if (i == k):
                                Jacobi[F_m_dic[f'P{i}'], B_m_dic[f'V{i}']] += (abs(2 * x1 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                            else:
                                Jacobi[F_m_dic[f'P{i}'], B_m_dic[f'V{i}']] += (abs(x2 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        if (i != k and f'V{i}rad' in B_m):
                            Jacobi[F_m_dic[f'P{i}'], B_m_dic[f'V{i}rad']] += (abs(x1 * x2 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        if (i != k and f'V{k}' in B_m):
                            Jacobi[F_m_dic[f'P{i}'], B_m_dic[f'V{k}']] += (abs(x1 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        if (i != k and f'V{k}rad' in B_m):
                            Jacobi[F_m_dic[f'P{i}'], B_m_dic[f'V{k}rad']] += -(abs(x1 * x2 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                    if (f'Q{i}' in F_m):
                        if (f'V{i}' in B_m):
                            if (i == k):
                                Jacobi[F_m_dic[f'Q{i}'], B_m_dic[f'V{i}']] += -(abs(2 * x1 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                            else:
                                Jacobi[F_m_dic[f'Q{i}'], B_m_dic[f'V{i}']] += -(abs(x2 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        if (i != k and f'V{i}rad' in B_m):
                            Jacobi[F_m_dic[f'Q{i}'], B_m_dic[f'V{i}rad']] += (abs(x1 * x2 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        if (i != k and f'V{k}' in B_m):
                            Jacobi[F_m_dic[f'Q{i}'], B_m_dic[f'V{k}']] += -(abs(x1 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))
                        if (i != k and f'V{k}rad' in B_m):
                            Jacobi[F_m_dic[f'Q{i}'], B_m_dic[f'V{k}rad']] += -(abs(x1 * x2 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))

            Inv_Jacobi = numpy.linalg.inv(Jacobi)
            Delta_X = np.zeros((len(Delta_C), len(Delta_C[0])))
            for i, t, k in itertools.product(range(len(Inv_Jacobi)), range(len(Delta_C[0])), range(len(Delta_C))):
                Delta_X[i][t] += Inv_Jacobi[i][k] * Delta_C[k][t]
            X = X + Delta_X

            X_dic = {B_m[i] : X[i] for i in range(len(X))}
            for i in range(1, len(Total_Bus) + 1):
                if (f'V{i}' in B_m):
                    Total_Bus[f'Bus{i}'][0] = X_dic[f'V{i}'][0]
                if (f'V{i}rad' in B_m):
                    Total_Bus[f'Bus{i}'][1] = X_dic[f'V{i}rad'][0]
            for i in Delta_C:
                if abs(i) <= self.Epsilon:
                    loop += 1

        P, Q = (np.zeros((len(Total_Bus), 1)), np.zeros((len(Total_Bus), 1)))
        for i, k in itertools.product(range(1, len(Total_Bus) + 1), range(1, len(Total_Bus) + 1)):
            if (f'Bus{i}-Bus{k}' in Connections):
                (x1, x1rad, x2, x2rad) = (Total_Bus[f'Bus{i}'][0], Total_Bus[f'Bus{i}'][1], Total_Bus[f'Bus{k}'][0], Total_Bus[f'Bus{k}'][1])
                if (i == k):
                    P[i - 1, 0] += abs(x1 * x1 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]))
                    Q[i - 1, 0] += -(abs(x1 * x1 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1])))
                else:
                    P[i - 1, 0] += abs(x1 * x2 * Y[i - 1, k - 1]) * math.cos(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad)
                    Q[i - 1, 0] += -(abs(x1 * x2 * Y[i - 1, k - 1]) * math.sin(cmath.phase(Y[i - 1, k - 1]) - x1rad + x2rad))

        S, I = (np.zeros((len(Total_Bus), len(Total_Bus)), dtype='complex_'), np.zeros((len(Total_Bus), len(Total_Bus)), dtype='complex_'))
        for i in range(len(Total_Bus)):
            print(f"P{i + 1} = {P[i].round(3)} pu.")
            print(f"Q{i + 1} = {Q[i].round(3)} pu.")
        for i in range(1, len(Total_Bus) + 1):
            Total_Bus[f'Bus{i}'][0] = Total_Bus[f'Bus{i}'][0] * (math.cos(Total_Bus[f'Bus{i}'][1]) + math.sin(Total_Bus[f'Bus{i}'][1]) * (-1) ** 0.5)
            a = complex(round(Total_Bus[f'Bus{i}'][0].real, 3) + round(Total_Bus[f'Bus{i}'][0].imag, 3))
            print(f'V{i} = {a}, V1deg = {math.degrees(cmath.phase(a))}')
        for i, k in itertools.product(range(1, len(Total_Bus) + 1), range(1, len(Total_Bus) + 1)):
            if (f'Bus{i}-Bus{k}' in Connections):
                I[i-1][k-1] = (Total_Bus[f'Bus{i}'][0] - Total_Bus[f'Bus{k}'][0]) * Y[i - 1][k - 1]
                S[i-1][k-1] = (Total_Bus[f'Bus{i}'][0] * (I[i - 1][k - 1].conjugate())) * self.S_Base_MVA
                print(f'I{i}{k} = ', I[i-1][k-1].round(3))
                print(f'S{i}{k} = ', S[i - 1][k - 1].round(3))
        Losses = np.zeros((len(Total_Bus), len(Total_Bus)), dtype='complex_')
        for i, k in itertools.product(range(1, len(Total_Bus) + 1), range(1, len(Total_Bus) + 1)):
            if (f'Bus{i}-Bus{k}' in Connections):
                Losses[i-1][k-1] = S[i-1][k-1] + S[k-1][i-1]
                print(f'Loss{i}-{k}', Losses[i-1][k-1].round(3))


GbNet = Guburcuk()
GbNet.Def_Bus('Bus1', unit_Vpu=1.01, active_power_P=(43, 'MW'), bus_type='Generator Bus', references='P,V')
GbNet.Def_Bus('Bus2')
GbNet.Def_Bus('Bus3', active_power_P=(70, 'MW'), reactive_power_Q=(20, 'MVar'))
GbNet.Def_Bus('Bus4')
GbNet.Def_Bus('Bus5', unit_Vpu=1.01, phase_diff=(0.1, 'd'), bus_type='Slack Bus', references='V,Vrad')

GbNet.Def_Line('Bus2', 'Bus3', (0.15*j, 'pu'))
GbNet.Def_Line('Bus2', 'Bus4', (0.03*j, 'pu'))
GbNet.Def_Line('Bus3', 'Bus4', (0.17*j, 'pu'))

GbNet.Def_Trafo('Bus1', 'Bus2', impedance=(0.085*j, 'pu'))
GbNet.Def_Trafo('Bus4', 'Bus5', impedance=(0.08*j, 'pu'))

GbNet.Solution()
