#  [print(' '*s + '*'*t) for s, t in zip(range(int(input('какая высота елки? = '))-1, 0, -1), range(1, int(input('сколько рядов у елки? = '))*2, 2))]

 SPACE = ' '
 STRAR = '*'

 if __name__ == "__main__":
     rows = int(input('сколько рядов у елки? '))
     spaces = rows-1
     stars = 1

     for i in range(rows):
         print(
             (SPACE*spaces) +
             (STRAR*stars) +
             (SPACE*spaces)
         )
         stars += 2
         spaces -= 1