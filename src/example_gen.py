class ExGen:
    def __init__(self, tokenizer):
        self.tknzr = tokenizer

    def gen_ex_set(self):
        ex_list = []
        for i in range(0, 100):
            for j in range(0, 100):
                text = ''.join([str(i),'+', str(j), '=', str(i+j)])
                encoded: list[int] = self.tknzr.encode(text)
                encoded.append(self.tknzr.str_to_int['<EOS>'])
                decoded: str = self.tknzr.decode(encoded[:-1])
                assert text == decoded, f"Text doesn't match decoded:\n\ttext:{text}\n\t{decoded}"
                assert self.tknzr.str_to_int["<EOS>"] == encoded[-1], f"""End of sequence not matched:\n\texpected EOS:{self.tknzr.str_to_int["<EOS>"]}\n\tseen EOS: {encoded[-1]} """
                ex_list.append([text, encoded])
        return ex_list