SeriesofNumbers=raw_input(" Enter numbers separated by space ")
sum=0
for numbers in SeriesofNumbers:
    numbers=numbers.split()
    for n in numbers:
        n=int(n)
        sum=sum + n
print("The sum is",sum)