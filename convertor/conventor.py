def convert_to_text(dataset, name):
    filename = "/home/jovyan/work/data/output/" + name + ".txt"
    words = dataset["word"].astype(str).tolist()
    text = " ".join(words)
    with open(filename, "w") as file:
        file.write(text)
