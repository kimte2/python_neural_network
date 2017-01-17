#coding: UTF-8
#ニューロン
class Neuron:
    input_sum = 0.0 #入力値格納の為の変数。

    def setInput(self, inp):　#メソッド。クラスが持つ関数はメソッドと呼ぶ。第一引数は自分のインスタンスを指定。

        self.input_sum += inp
        print self.input_sum

