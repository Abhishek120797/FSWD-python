import pickle
book_dict={'science':100,'maths':80,'marathi':90,'English':200}
with open("bookfile",'wb') as f:
    pickle.dump(book_dict,f)
