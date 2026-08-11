def get_vocab() -> dict[str, int]:
    tks = list(map(lambda x: str(x), range(0, 10)))
    tks.extend(["+", "=", "<PAD>", "<EOS>"])
    add_vocab = {t: i for (i,t) in enumerate(tks)}
    return add_vocab