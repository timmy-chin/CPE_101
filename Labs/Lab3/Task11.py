def getKthDigit(n,k):
    if k > len(n)-1 or n[-1-k] == '-':
        return 0
    else:
        return n[-1-k]

print(getKthDigit(input('n: '),int(input('k:'))))

