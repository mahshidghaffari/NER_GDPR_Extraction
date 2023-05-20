import pandas as pd

def convert_to_text(dataset, name):
    filename = "/home/jovyan/work/data/output/" + name + ".txt"
    words = dataset["word"].astype(str).tolist()
    text = " ".join(words)
    with open(filename, "w") as file:
        file.write(text)


def create_dataframe_from_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    df = pd.DataFrame({'word': words})
    return df