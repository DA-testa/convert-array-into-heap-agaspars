# python3


def build_heap(data):
    swaps = []
    n = len(data)

    def heap(i):
        min = i
        l = 2 * i + 1 #left child of a parent/root
        r = 2 * i + 2 #right child of a parent/root

        if l < n and data[l] < data[min]: #check if left child exist and is less than min element
            min = l 

        if r < n and data[r] < data[min]: #check if right child exist and is less than min element
            min = r

        if i != min:
            swaps.append((i, min)) #if i is not the min yet => swap values and call heap function again
            temp = data[i]
            data[i]=data[min]
            data[min]=temp

            heap(min)

    for i in reversed(range(n // 2)):   #iterate from (n//2)-1 to 0
                                        # if n=5 => loop counts from 1 to 0, calling heap function for each i (1 and 0)
        heap(i)

    return swaps


def main():
    #input from keyboard
    # for i in reversed(range(5 // 2)): #iterate from (n/2)-1 to 0
    #     print(i)
    # print(7//3)
    n = int(input())
    data = list(map(int, input().split()))

    swaps = build_heap(data)

    #swap amount
    print(len(swaps))

    #result swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
