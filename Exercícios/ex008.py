print('Forma que eu fiz: ')
m = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a '.format(m))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m*0.001, m*0.01, m*0.1, m*10, m*100, m*1000))

print('\nOutra forma do programa: ')
medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(km, hm, dam, dm, cm, mm))