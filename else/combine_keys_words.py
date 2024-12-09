def filter_phrases_large_file(keywords_file, texts_file, output_file):

    with open(keywords_file, "r", encoding="utf-8") as kf:
        keywords = set(line.strip() for line in kf)

    def line_generator(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                yield line.strip()

    with open(output_file, "w", encoding="utf-8") as of:
        for line in line_generator(texts_file):
            words = set(line.split())
            if keywords & words:
                of.write(line + "\n")


# filter_phrases_large_file('keywords.txt', 'texts.txt', 'output.txt')
