#Example of while loop

attempt = int(input("Your Next attempt:"))

while attempt <= 10:
    print('Attemps left:', attempt)
    
    attempt += 1

print("No more attemts left")