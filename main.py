import requests

from collections import Counter


words_file = "words.txt"
url = "https://eng.mipt.ru/why-mipt/"

def get_text_counter(url):
    response = requests.get(url)
    return Counter(
        response.text.split()
    )

def main():
    with open(words_file, "r") as f:
        words = set(
            f.read().split()
        )

    original_text_counter = get_text_counter(url=url)
    frequencies = {
        w: original_text_counter.get(w, 0)
        for w in words
    }
    print(frequencies)

if __name__ == "__main__":
    main()
