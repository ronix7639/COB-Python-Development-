def countuniquewords(fname):
    wc={} #wordcount
    with open(fname,'r') as file: #Opens file and reads it
        for line in file:
            words=line.split()
            for word in words:
                word=word.strip('.,!?\'"').lower() #Removes punctuation and converts to lowercase
                if word:
                    wc[word] = wc.get(word,0) + 1
    return wc

def main():
    fname=input("Enter the file path from your local desktop : ")
    try:
        wc=countuniquewords(fname)
        print("\nUnique words and their occurences : ") #Displays the words and their occurences
        for word,count in wc.items():
            print(f"{word}:{count}")
    except FileNotFoundError:
        print(f"File '{fname}' not found in the given location.")
        
if __name__=="__main__":
    main()