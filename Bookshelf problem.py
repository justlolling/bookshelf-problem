#the bookshelf problem
file=open("bookshelfinput.txt","r")

#sort shelves by size order
sorted_shelves=[]
line=file.readline()
sorted_shelves=line.strip( )
sorted_shelves=line.split()
sorted_shelves=[int(numeric_string) for numeric_string in sorted_shelves]
sorted_shelves.sort(reverse=True)


#sort books by size order
sorted_books=[]
for line in file:
    component=line.strip(' ')
    component=line.split()
    component=[int(component[0]),str(component[1])]
    sorted_books.append(component)
sorted_books.sort(reverse=True)



#loop and fill shelves

while ((sorted_shelves != []) and (sorted_books != [])):
    current_shelf=[sorted_shelves[0]]
    i=0
    while (i<(len(sorted_books))):
        if (current_shelf[0]-sorted_books[i][0]) > 0:                  
            current_shelf[0]=current_shelf[0]-sorted_books[i][0]
            current_shelf.append(sorted_books[i])
            sorted_books.remove(sorted_books[i])
        else:#don't need to add 1 for index to the other as item is removed
            i=i+1

    print("\nInitial space in shelf: "+str(sorted_shelves[0]))
    print("Space remaining: " +str(current_shelf[0]))
    print("Books in shelf: " + str(current_shelf[1:]))
    sorted_shelves.remove(sorted_shelves[0])

                       
#see what is remaining
if sorted_shelves == []:
    print("\nThe following books were unable to be sorted: " + str(sorted_books))

if sorted_books == []:
    print("\nThe following shelves were not needed: " + str(sorted_shelves))

    

