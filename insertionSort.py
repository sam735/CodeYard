datas = [12, 11, 13, 5, 6]

def insertion_sort():
    for i in range(1,len(datas)):
        key = datas[i]
        j = i-1
        while j>=0 and key<datas[j]:
            datas[j+1] = datas[j] 
            j -= 1
        datas[j+1] = key


if __name__ == "__main__":
    insertion_sort()
    print(datas)
