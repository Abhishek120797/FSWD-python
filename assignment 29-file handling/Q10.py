import pickle
with open("bookfile",'rb') as f:
    book_dict=pickle.load(f)
    for k in book_dict:
        print(k,"=",book_dict[k])

    
