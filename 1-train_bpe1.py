import sys
import sentencepiece as spm

train_dataset_file_tok = sys.argv[1]
lang = sys.argv[2]

# Train SentencePiece model from the dataset file
# and create `model_prefix.model` and `model_prefix.vocab`

# If the training data is too small and the maximum pieces reserved is less than 4000,
# you can decrease --vocab_size or --hard_vocab_limit=false, which automatically shrinks the vocab size.

model_prefix = lang  # Use language code as the model prefix

train_value = '--input=' + train_dataset_file_tok + ' --model_prefix=' + model_prefix + ' --vocab_size=50000 --hard_vocab_limit=false --model_type=bpe --split_digits=true'
spm.SentencePieceTrainer.train(train_value)

print("Done, training a SentencePiece model for", lang, "finished successfully!")
