from hofu import Iterator


def main():
    Iterator(range(10)) \
        .map(lambda x: x ** 2) \
        .filter(lambda x: x % 2 == 0 and x != 0) \
        .map(lambda x: "Next even power is " + str(x)) \
        .for_each(print)

    # +- equivalent to sum(range(10))
    total = Iterator(range(10)).reduce(lambda x, y: x + y)
    print("Sum of 1-10:", total)

    Iterator(range(10)) \
        .rev() \
        .skip(5) \
        .take(2) \
        .map(lambda x: "Next number: " + str(x)) \
        .for_each(print)

    people = [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25},
        {"name": "Bob", "age": 40},
        {"name": "Alice", "age": 35},
    ]
    average_age = Iterator(people).reduce(lambda x, y: x + y["age"], 0) / len(people)
    print("Average age:", average_age)

    data = Iterator(range(10)).filter(lambda x: x % 2 == 0).collect()
    print("Even numbers:", list(data))

    even_formatted = Iterator(range(10)).map(lambda x: f"{x}={'even' if x % 2 == 0 else 'odd'}").collect()
    print("Even/odd:", list(even_formatted))


if __name__ == '__main__':
    main()
