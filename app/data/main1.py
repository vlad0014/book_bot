import json
books={
    "title":"Кладовище домашніх тварин",
    "desc":"Усе почалося з того, що улюбленця родини Луїса Кріда, кота Черча, збила вантажівка. Сусід запропонував йому поховати тварину на старому індіанському кладовищі. За легендами, воно має таємничу силу, яка здатна повертати до життя. І Луїс погодився... Уранці кіт прийшов додому живим. Майже живим...",
    "url":"https://uabooks.net/254-kladovyshche-domashnih-tvaryn.html",
    "photo":"https://uabooks.net/posters/254.jpg",
    "rating":"7/10"
}
with open("books.json",'w') as json_file:
    json.dump(books,json_file,indent=2)
with open("books.json") as json_file:
    data_from_file=json.load(json_file)
    print(data_from_file)
    print(data_from_file==books)