nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
#IF mostrado no vídeo:
#   if 7 > média >= 5
#   print('O aluno está em RECUPERAÇÃO.')
if media >= 7:
    print('O aluno está APROVADO.')
elif media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')