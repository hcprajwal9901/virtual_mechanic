import pandas as pd

def preprocess(path_in: str, path_out: str):
    df = pd.read_csv(path_in)
    # TODO: clean text, normalize fields, label mapping
    df.to_csv(path_out, index=False)

if __name__ == "__main__":
    preprocess("../../data/raw/forum_scrapes.csv", "../../data/processed/training_data.csv")
