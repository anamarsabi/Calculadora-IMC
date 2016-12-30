#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = raw_input("cuántos años tienes?")
height = float(raw_input("cuánto mides(en metros)?"))
weight = float(raw_input("cuánto pesas?"))

print "so, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
imc = weight / height**2
print "tu índice de masa corporal es %r" % (imc)

if imc <= 18.0:
    print "a comé"
elif imc <=24.9:
    print "ole ese cuerpo serrano"
elif imc <=30.0:
    print "a lechuga y agua"
elif imc > 45.0:
    print "te vas a caer por los dos laos de la cama"
