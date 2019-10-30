print('Пожалуйста, введите пароль!')
n=len(input())
if n<6:
    print('low')
elif 5<n<10:
    print('medium')
else:
    print('high')