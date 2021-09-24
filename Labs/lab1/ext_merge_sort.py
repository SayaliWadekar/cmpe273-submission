import os
import time

path = r"/home/sayali/Documents/cmpe273-submission/Labs/lab1/input"

outputpath = r"/home/sayali/Documents/cmpe273-submission/Labs/lab1/output"


def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]

        R = arr[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# sort the numbers
def sort():
    start = time.time()
    print("Sorting.....")
    os.chdir(path)
    resultList = []
    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        time.sleep(0.1)
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            f = open(file_path)
            contents = f.readlines()
            for line in contents:
                resultList.append(int(line))
            f.close()
    mergeSort(resultList)

    if  not os.path.exists(outputpath):
        os.mkdir(outputpath)

    textfile = open(f"{outputpath}/sorted.txt", "w")
    for element in resultList:
        textfile.write(str(element) + "\n")
    textfile.close()
    end = time.time()
    print(f"Total execution time is {end - start}")


if __name__ == "__main__":
    sort()
