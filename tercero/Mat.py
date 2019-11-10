class Operaciones:
    
    
    def suma(self, pol_a,pol_b):
        pass
    
    def resta(self,pol_a,pol_b):
        pass

    def multiplicacion(self,pol_a,pol_b):
        pass

    def multiplicaEscalar(self,escala,pol):    
        pass
    
    def evaluar(self,x,pol):
        pass

class OpPolinomial(Operaciones):
    
    def suma(self, pol_a,pol_b):
        g_max = max(pol_a.grado,pol_b.grado)
        g_min = min(pol_a.grado,pol_b.grado)
        pol_c = Polinomio(grado=g_max)
        for i in range(g_max):
            if g_max == pol_a.grado:
                pol_c.coeficiente.append(pol_a.coeficiente[i])
            else:
                pol_c.coeficiente.append(pol_b.coeficiente[i])
        for i in range(g_min):
            if g_min == pol_a.grado:
                pol_c.coeficiente[i] += pol_a.coeficiente[i] 
            else:
                pol_c.coeficiente[i] += pol_b.coeficiente[i] 
        return pol_c
       
    def resta(self,pol_a,pol_b):
        g_max = max(pol_a.grado,pol_b.grado)
        g_min = min(pol_a.grado,pol_b.grado)
        pol_c = Polinomio(grado=g_max)
        for i in range(g_max):
            if g_max == pol_a.grado:
                pol_c.coeficiente.append(pol_a.coeficiente[i])
            else:
                pol_c.coeficiente.append(pol_b.coeficiente[i])
        for i in range(g_min):
            if g_min == pol_a.grado:
                pol_c.coeficiente[i] -= pol_a.coeficiente[i] 
            else:
                pol_c.coeficiente[i] -= pol_b.coeficiente[i] 
        return pol_c

    def multiplicacion(self,pol_a,pol_b):
        g = pol_a.grado*pol_b.grado
        pol_c = Polinomio(grado=g)
        for i in range(pol_a.grado):            
            for j in range(pol_b.grado):
                pol_c.coeficiente.append(pol_a.coeficiente[i] * pol_b.coeficiente[j])
        return pol_c

    def multiplicaEscalar(self,escala,pol):          
        pol_x = pol
        for i in range(pol.grado): 
            pol_x.coeficiente[i] *= escala
        return pol_x

    def evaluar(self,x,pol):
        valor = 0
        for i in range(pol.grado):
            valor = pol.coeficiente[i] +(x * valor)
        return valor

class Polinomio():
    def __init__(self,coef=[],grado=0):        
        self._coeficiente = []
        self._grado = 0
        self.coeficiente = coef
        self.grado = grado

    @property
    def coeficiente(self):
        return self._coeficiente

    @coeficiente.setter
    def coeficiente(self,list_c):
        lista = []
        if self.grado <= 0:            
            lista[0] = 0
        else:
            for i in range(self.grado):
                lista.append(list_c[i])
        self._coeficiente = lista   

    @property
    def grado(self):
        return self._grado

    @grado.setter
    def grado(self,g):
        if self.grado <= 0:   
            self.grado = 0
        else:
            self.grado = g
   

class ObjAlgrebraico:

    def __init__(self, op_polinomial):
        self.operaciones = op_polinomial

    def suma(self, pol_a,pol_b):
        self.operaciones.suma(pol_a,pol_b)
    
    def resta(self,pol_a,pol_b):
        self.operaciones.resta(pol_a,pol_b)

    def multiplicacion(self,pol_a,pol_b):
        self.operaciones.multiplicacion(pol_a,pol_b)

    def multiplicaEscalar(self,escala,pol):    
        self.operaciones.multiplicaEscalar(escala,pol)
    
    def evaluar(self,x,pol):
        self.operaciones.multiplicaEscalar(x,pol)

pro = OpPolinomial()
obj = ObjAlgrebraico(pro)
pol_a = Polinomio([1, 2, 3],2)
pol_b = Polinomio([3, 2, 1],3)
print(pro.suma(pol_a,pol_b).coeficiente)
print(pro.resta(pol_a,pol_b).coeficiente)
print(pro.multiplicacion(pol_a,pol_b).coeficiente)
print(pro.multiplicaEscalar(10,pol_b).coeficiente)
print(pro.evaluar(10,pol_b))