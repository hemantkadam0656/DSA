def Freq_Of_Words(path, fileName):
    dict = {}

    with open(path + "/" + fileName, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                dict[word] = dict.get(word, 0) + 1    
    return dict 


if __name__ == '__main__':
    path = r'D:\DSA\KrishNaikQuestion.py'
    fileName = r'TestFile.txt'
    obj = Freq_Of_Words(path, fileName)
    print(obj)