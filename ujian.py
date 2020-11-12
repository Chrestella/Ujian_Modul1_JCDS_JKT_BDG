# nomor1
angka = input('Input your phone number: ')
if angka.isdigit() == True and (len(angka) == 10):
    print (f'({(angka[:3])}) {(angka[3:6])}-{(angka[6:])}')
elif "-" in angka and (len(angka) == 10): 
    print ("Input only positive number.")
elif angka.isalpha() == True:
    print ("Invalid input. No alphabet.")
elif angka.isdigit() == True and (len(angka) < 10 or len(angka) > 10):
    print ("Digits must be in length of 10, not more or less")
elif angka.isalnum() == True:
    print ("Invalid input. No symbols.")


# nomor2
def moveZeros(s, n):
    last = s.index(n)
    s[-1], s[last] = s[last], s[-1]
    return s

# value = input("Your value here: ")
# list=[ord(ch) for ch in value]
# print(list)
# def moveZeros(s, n):
#     for item in range(s):
#         ord(ch) for ch in value == 48:
#     s[-1], s[last] = s[last], s[-1]
#     return s

print(moveZeros([False, 1, 0, 1, 2, 0, 1, 3, 'a'],0))
print(moveZeros([0, 0, 0, 'Test', 0, 3, 'a', True, False],0))
print(moveZeros([0, True, True, False, 'a', 'b', 1, 1, 1],0))

# nomor3
class Statistics:
    def __init__(self, list):
        self.list = list

    def mean(self):
        sum = 0
        for item in self.list:
            sum+=item
        mean = sum / len(self.list)
        return mean
    
    def median(self):
        self.list.sort()
        if (len(self.list)%2 != 0):
            median = self.list[round(len(self.list))/2]
        else:
            mid1 = self.list[(int(len(self.list)/2))-1]
            mid2 = self.list[(int(len(self.list)/2))]
            median = (mid1+mid2)/2
        return median

    def mode(self):
        countList = []
        #create countList
        for num in self.list:
            check = False
            for list1 in countList:
                if (list1[0] == num):
                    list1[1] += 1
                    check = True
            if(check == False) :
                countList.append([num, 0])
        
        #create list of mode/s
        maxFrequency = 0
        modes = []
        for list1 in countList:
            if (list1[1] > maxFrequency):
                modes = [list1[0]]
                maxFrequency = list1[1]
            elif (list1[1] == maxFrequency):
                modes.append(list1[0])
        
        # if every value appears same amount of times
        if (len(modes) == len(countList)):
            modes = []
        return modes

    def std(self):
        sum = 0
        for item in self.list:
            sum+=item
        std = (sum ** 2 / len(self.list ))
        return std
    
print(Statistics.mean([1,2,3,4,5,'a'])) 
print(Statistics.mean([12,10,10,10,10]))
print(Statistics.mean([4,5,2,1,6,7]))
