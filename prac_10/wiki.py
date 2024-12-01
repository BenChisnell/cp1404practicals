import wikipedia

search_phrase = input("Enter page title: ")
while search_phrase != "":
    try:
        search_phrase = wikipedia.page(search_phrase)
        print(f"{search_phrase.title}\n{search_phrase.summary}\n{search_phrase.url}")

    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search: ")
        print(e.options)

    except wikipedia.exceptions.PageError:
        print(f"Page id {search_phrase} does not match any pages. Try another id!")

    search_phrase = input("Enter page title: ")
print("Thank you.")
