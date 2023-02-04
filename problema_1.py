# Aluno: Akenathon Jamisse Barros Furtado

from sys import stdin
from sys import exit

def triangular(n):
  if n == 1 or n == 0:
    return True

  t_sum = 0
  M_c = 0
  for x in range(n):
    M_c += 1
    t_sum += x
    if t_sum == n:
      return True, M_c - 1
      
    if x == n:
      return False

def main():
#  stdin = open('entrada.in','r')
  
  n = int(stdin.readline().strip())
  line = stdin.readline().strip()

  num_list = line.split(' ')
  M_counter = 0

  if triangular(n):
    if n == 1:
      M_counter += 1
    else:
      a,b = triangular(n)

      y = 1
      while y <= b:
        if int(num_list[0]) % 2 == 0:
          odd_even = 2
          i = 0
          x = 1
          c = 0
          if odd_even % 2 == 0:
            for num in num_list[i:i+x]:
              if int(num) % 2 == 0:
                c += 1
                if c == x:
                  M_counter += 1
                  odd_even += 1
          i += x
          x += 1
          y += 1
        else:
          odd_even = 1
          i = 0
          x = 1
          c = 0
          if odd_even % 2 != 0:
            for num in num_list[i:i+x]:
              if int(num) % 2 != 0:
                c += 1
                if c == x:
                  M_counter += 1
                  odd_even += 1
          i += x
          x += 1
          y += 1

  else:
    print('NAO')
    print('%')
    exit()

  print(M_counter)
  print("%")

if __name__ == '__main__':
  main()