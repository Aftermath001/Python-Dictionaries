# A Dictionary
books = {
1 :{
    "title": "When the Sun Goes Down",
    "Author": "Jephy Maina",
    "Publisher":"Longhorn",
    "Month" :"January" },
2 :{
    "title": "The River And The Source",
    "Author": "Alvin Adams",
    "Publisher":"Longhorn",
    "Month" :"December"
    },
3 :{
    "title": "Things Fall Apart",
    "Author": "Kimani Bonnke",
    "Publisher":"Kenya Publishers",
    "Month" :"October"
    },
4 :{
    "title": "Happy Together",
    "Author": "Ephy Orina",
    "Publisher":"Longhorn",
    "Month" :"May"
    }
    
}

# Reading the data
print(books[1].get("title"), books[2].get("title"),books[3].get("title"),books[4].get("title"))




#  creating a new book
books[5]= {"title":"My People's King","Author":"Maina Jephy","Publisher":"Kisii Publishers","Month":"February"}
print(books)
 

# Updating
books[3].update({"Color":"Green"})

# Deletion
del books[1]
print(books)