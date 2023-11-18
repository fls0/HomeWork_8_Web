from mongoengine import connect
from models import Author, Quote

def search_quotes_by_tag(tag):
    quote = Quote.objects(tags=tag)
    if quote:
        result = [q.quote for q in quote]
        print(result)
    else:
        print(f'Цитати з тегом {tag} не знайдено.')

def search_quotes_by_author(author_name):
    author = Author.objects(fullname = author_name).first()
    if author:
        quote = Quote.objects(author=author)
        result = [q.quote for q in quote]
        print(result)
    else:
        print(f'Автора {author_name} не знайдено.')

def search_quotes_by_tags(tags):
    quote = Quote.objects(tags__all=tags)
    if quote:
        result = [q.quote for q in quote]
        print(result)
    else:
        print(f'Цитати з тегом {tags} не знайдено.')

def main():
    connect(
        db="homework",
        host="mongodb+srv://sadurskyim:123123q@flsx.tisgnah.mongodb.net/?retryWrites=true&w=majority",
    )

    while True:
        command = input("Введіть команду (tag, author, tags): ")
        
        if command == "tag":
            tag_value = input("Введіть тег: ")
            search_quotes_by_tag(tag_value)
        elif command == "author":
            author_name = input("Введіть ім'я автора: ")
            search_quotes_by_author(author_name)
        elif command == "tags":
            tags_input = input("Введіть теги через кому: ")
            tags = [tag.strip() for tag in tags_input.split(',')]
            search_quotes_by_tags(tags)
        elif command == "exit":
            break
        else:
            print("Невідома команда. Доступні команди: tag, author, tags")

if __name__ == "__main__":
    main()