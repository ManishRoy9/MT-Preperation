import sys
import sentencepiece as spm

model_path = sys.argv[1]
raw_file = sys.argv[2]
subworded_file = raw_file + ".subword"

print("Model Path:", model_path)
print("Raw Dataset:", raw_file)

sp = spm.SentencePieceProcessor()
sp.load(model_path)

with open(raw_file) as raw, open(subworded_file, "w+") as subworded:
    for line in raw:
        line = line.strip()
        line = sp.encode_as_pieces(line)
        # line = ['<s>'] + line + ['</s>']    # add start & end tokens; optional
        line = " ".join([token for token in line])
        subworded.write(line + "\n")

print("Done subwording the dataset! Output:", subworded_file)