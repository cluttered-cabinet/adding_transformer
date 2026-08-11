class AddTokenizer:
    def __init__(self, vocab: dict):
        # mappings
        self.str_to_int = vocab
        self.int_to_str = {i:j for (j,i) in vocab.items()}
    def encode(self, text: str) -> list[int]:   
        preprocessed = [i if i in self.str_to_int else "<UNK>" for i in text]
        ids = [self.str_to_int[i] for i in preprocessed]
        return ids
    def decode(self, ids: list[int]) -> str:
        text = "".join([self.int_to_str[i] for i in ids])
        return text