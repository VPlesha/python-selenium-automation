



def find_missing_element(arr1:list, arr2:list):

    arr1.sort()
    arr2.sort()
    for i in range(len(arr2) - 1):
        if arr1[i] != arr2[i]:
            print(arr1[i] + 'is the missing element')
            return
    print(str(arr1[-1]) + 'is the missing element')

testlist1 = [1,2,3,4,5,6,7]
testlist2 = [3,4,2,6, 1,7]

find_missing_element(testlist1, testlist2)
