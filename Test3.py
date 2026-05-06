n=int(input("Enter number of games u want to play: "))
for i in range(n):
    print("Game ",i+1)
    a=int(input("Enter number of coins: "))
    if a%2==0:
        print("Player 1 wins")
    else:
        print("Player 2 wins")