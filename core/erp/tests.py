
# en shell exec(open('core/erp/tests.py').read())

from core.erp.models import Type, Employee

""" 
# Agregar
try:
  t = Type()
  t.name = 'Agencia'
  t.save()
except Exception as e:
  print(e)

# Actualizar
try:
  t = Type.objects.get(id=4)
  t.name = 'Agencia'
  t.save()
except Exception as e:
  print(e)

# Eliminar
try:
  t = Type.objects.get(id=5)
  t.delete()
except Exception as e:
  print(e)
"""
# Employee.objects.filter(names__


for i in  Type.objects.filter(name__startswith='A')[:5]:
  print(i.name)