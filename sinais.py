import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


class Signal():
    def __init__(self, funcoes_intervalos):
        self.t = sp.symbols('t')
        self.expressoes = []


        for funcao in funcoes_intervalos:
            if funcao[0] == '0':
                self.expressoes.append([0, True])
            else:
                inicio, fim = funcao[1]
                expressao = funcao[0].simplify()
                self.expressoes.append((expressao, (self.t >= inicio) & (self.t < fim)))

        self.formula = sp.Piecewise(*self.expressoes)
        print(self.formula)


    def time_scaling(self, scaling_factor):
        scaled_signal = self.formula.subs(self.t, scaling_factor * self.t)
        return scaled_signal

    def time_shifting(self, shift_amount):
        shifted_signal = self.formula.subs(self.t, self.t - shift_amount)
        return shifted_signal

    def reflection(self):
        reflected_signal = self.formula.subs(self.t, -self.t)
        return reflected_signal

    def plot(self, save_file=None):
        t_values = np.linspace(0, 40, 400)
        original_signal_func = sp.lambdify(self.t, self.formula, 'numpy')

        plt.plot(t_values, original_signal_func(t_values), label='Sinal')
        plt.xlabel('t')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title('Sinal Original')

        if save_file:
            plt.savefig("output/" + save_file)
            plt.close()
        else:
            plt.show()

    def plot_comparison(self, transformed_signal, operation_name, save_file=None):
        t_values = np.linspace(-40, 40, 400)
        original_signal_func = sp.lambdify(self.t, self.formula, 'numpy')
        transformed_signal_func = sp.lambdify(self.t, transformed_signal, 'numpy')

        plt.plot(t_values, original_signal_func(t_values), label='Sinal Original')
        plt.plot(t_values, transformed_signal_func(t_values), label='Sinal ' + operation_name)
        plt.xlabel('t')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title(operation_name)

        if save_file:
            plt.savefig("output/" + save_file)
            plt.close()
        else:
            plt.show()