def most_frequent(strng):
    string=strng.lower()
    freq={}
    count=0
    for char in string:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
            count+=1
    
    for n in range(count):
        max_key=max(freq,key=freq.get)
        print(max_key,"=",freq[max_key])
        freq.pop(max_key)

string=input("Enter a string: ")
most_frequent(string)
            
