
def el_palindrome(palabra):
    if(palabra == palabra[::-1]):
        print('La palabra', palabra, 'es palindrome')
    else:
        print('La palabra', palabra, 'no es palindrome')

el_palindrome("reconocer")
el_palindrome("arroz")