import pytest
from cobertura import ParImpar

def  test_add():
    objeto = ParImpar([1])
    assert len(objeto.ArrayNumeros)==1
    objeto.add(2)
    assert len(objeto.ArrayNumeros)==2

def test_sumaPar():
    objeto = ParImpar([1])
    assert len(objeto.ArrayNumeros)==1
    objeto.add(1)
    objeto.add(2)
    objeto.add(3)
    assert len(objeto.ArrayNumeros)==4
    assert objeto.sumaPar() ==2

def test_sumaImpar():
    objeto = ParImpar([1,2,3])
    assert len(objeto.ArrayNumeros)== 3
    assert objeto.sumaImpar()==4   

def test_cuadradoLista():
    objeto = ParImpar([1,2,3,4])
    assert len(objeto.ArrayNumeros)==4
    assert objeto.cuadradoLista()== [1,4,9,16]
      