#

from multiprocessing import Pipe, Process

class BiConn(object):
    def __init__(self,left,right,timeout=None):
        """
        left : a função que vai ligar ao lado esquerdo do Pipe
        right: a função que vai ligar ao outro lado
        timeout: (opcional) numero de segundos que aguarda pela terminação do processo
        """
        left_end, right_end = Pipe()
        self.timeout=timeout
        self.lproc = Process(target=left, args=(left_end,))       # os processos ligados ao Pipe
        self.rproc = Process(target=right, args=(right_end,))
        self.left  = lambda : left(left_end)                       # as funções ligadas já ao Pipe
        self.right = lambda : right(right_end)
    
    def auto(self, proc=None):
        if proc == None:             # corre os dois processos independentes
            self.lproc.start()
            self.rproc.start()  
            self.lproc.join(self.timeout)
            self.rproc.join(self.timeout)
        else:                        # corre só o processo passado como parâmetro
            proc.start(); proc.join()
    
    def manual(self):   #  corre as duas funções no contexto de um mesmo processo Python
        self.left()
        self.right()
    