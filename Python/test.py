def partitionArray(k, numbers):

    store_unique = set()

    for i in range(len(numbers)):

        if(k>1):
            for m in range(i+1, len(numbers), k-1):
                temp = numbers[m:m+k-1]
                temp.append(numbers[i])

                if ( (len(temp) == len(set(temp))) and (len(temp) == k ) ) :
                    temp.sort()
                    store_unique.add(tuple(temp))

    return 'Yes' if len(store_unique)>=k else 'No'


