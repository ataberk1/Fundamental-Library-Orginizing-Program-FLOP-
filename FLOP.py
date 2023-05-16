data= []
def addbook():
    info = input('''"book's name", "book's number", "book's category", "book's placement", "book's author", "book's publishment year"''')
    info = info.split(",")
    if len(info) < 6:
        print("Can not add book to the system. Missing parameter(s).")
        return
    bookname = info[0].strip()
    booknum = info[1].strip()
    category = info[2].strip()
    placement = info[3].strip()
    author = info[4].strip()
    year = info[5].strip()
    if booknum.isnumeric() == False or year.isnumeric() == False:
        print("Can not add book to the system. Improper parameter(s).")
        return

    book = {"Status":"book has not taken" , "Name":bookname , "Number":booknum , "Category":category ,
            "Placement":placement , "Author":author , "Year":year , "ID":""}
    data.append(book)
    print(bookname,"has added to the system")

def findbook():
    control = 0
    find = input('''"book’s name" / "book’s number"''')
    if len(find) == 0:
        print("Can not find book. Missing parameter(s).")
        return
    find = find.split(",")
    locallist = []
    for i in data:
        if i["Name"] == find[0] or i["Number"] == find[0]:
            for values in i.values():
                locallist.append(values)
            locallist.remove(locallist[7])
            print(*locallist)
            control = 1
            break
    if control == 0:
        print("Can not find book. There is no book like this in this system.")
    else:
        pass

def listauthor():
    control = 0
    find = input('''"author's name?"''')
    if len(find) == 0:
        print("Can not list book(s). Missing parameter(s).")
        return
    for i in data:
        if i["Author"] == find:
            print(i['Name'] , i['Number'])
            control = 1
    if control == 0:
        print("There are no books by this author in this system.")
    else:
        pass

def takebook():
    control = 0
    x = input('''"book's name"/ "book's number", "id of the people who take it"''')
    x = x.split(",")
    if len(x) < 2 :
        print("Can not give book. Missing parameter(s).")
        return
    take = x[0].strip()
    ids = x[1].strip()
    for i in data:
        if i["Name"] == take or i["Number"] == take:
            if i["Status"] == "book has not taken":
                i["Status"] = "book has taken"
                i["ID"] = ids
                print(i["Name"],"has given with no problem.")
                control = 1
            else:
                print("Can not give book. Someone has already taken it.")
                control = 1
    if control == 0:
        print("Can not give book. There is no book like this in this system.")

def listbook():
    control = 0
    for i in data:
        print(i['Name'],i['Number'], sep=" ")
        control = 1
    if control == 0:
        print("There are no books in the system")
        

def returnbook():
    control = 0
    take = input('''"book’s name" / "book’s number"''')
    if len(take) == 0:
        print("Can not return book(s). Missing parameter(s).")
        return
    for i in data:
        if i["Name"] == take or i["Number"] == take:
            if i["Status"] == "book has taken":
                i["Status"] = "book has not taken"
                print(i["Name"],"has been returned.")
                control = 1
            else:
                print("Can not return book. It has not been taken by anyone.")
                control = 1
    if control == 0:
        print("Can not return book. There is no book like this in this system.")

def listtaken():
    control =0
    for i in data:
        if i["Status"] == "book has taken":
            print(i["Name"], i["Number"] , i["ID"])
            control = 1
    if control == 0:
        print("No one has taken books :(")

def listyear():
    control = 0
    x = input('"year", "before" / "after"')
    x = x.split(",")
    if len(x) < 2 :
        print("Can not list books. Missing parameter(s).")
        return
    fyear = x[0].strip()
    when = x[1].strip()
    if fyear.isnumeric() == False:
        print("Can not list book(s). Improper input.")
        return
    if when == "before":
        for i in data:
            if i["Year"] < fyear:
                print(i['Name'],i['Number'], sep=" ")
                control = 1
    elif when == "after":
        for i in data:
            if i["Year"] > fyear:
                print(i['Name'],i['Number'], sep=" ")
                control = 1
    else:
        print("Can not list book(s). Improper input.")
    if control == 0 and when == "before":
        print("There are no books that is published before", fyear ,"in the system.")
    elif control == 0 and when == "after":
        print("There are no books that is published after", fyear ,"in the system.")
        
            


        
    


x=1
while x == 1:
    job = input("What would you want to do? (Write help for command list)")
    match job:
        case "help" | "-h":
            print("add Book\t|-a|\tadds a new book to the system\n" "find Book\t|-f|\tthis command finds a book at the system\n" "list an author's books\t|-la|\tfinds the books of an author which are in the system\n"
                  "take book\t|-t|\tgive a book to someone\n" "return book\t|-r|\treturns a book which have taken by someone\n" "list books\t|-l|\tlists every book in the system\n"
                  "list taken books\t|-lt|\tlists every taken book in the system\n" "list books before/after year\t|-ly|\tlists every book in the system with given dates\n"
                  "help\t|-h|\tprints all commands and their descriptions\n" "quit\t|-q|\tquits program\n")

        case "-q" | "quit":
            x=0
            print("See you later :)")
        
        case "-a" | "add book":
            addbook()
            data = sorted(data, key=lambda x: x['Number'])
        case "-f" | "find book":
            findbook()
        case "-la" |"list an author's books":
            listauthor()
        case "-t" | "take book":
            takebook()
        case "-l" | "list books":
            listbook()
        case "-r" | "return book":
            returnbook()
        case "-lt" | "list taken books":
            listtaken()
        case "-ly" | "list books before/after year":
            listyear()
        case "":
            pass
        case other:
            print("You have entered a command that does not exist. Write ‘help’ to get to know commands.")
        
            
          
                          
            


