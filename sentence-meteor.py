import sys
from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize

target_test = sys.argv[1]   # Test file argument
target_pred = sys.argv[2]   # MTed file argument

# Open the test dataset human translation file
with open(target_test) as test:
    refs = test.readlines()

# Open the translation file by the NMT model
with open(target_pred) as pred:
    preds = pred.readlines()

# Tokenize the sentences
refs = [word_tokenize(ref.strip()) for ref in refs]
preds = [word_tokenize(pred.strip()) for pred in preds]

# Calculate METEOR for each sentence pair
meteor_scores = [meteor_score([refs[i]], preds[i]) for i in range(len(refs))]

# Calculate the average METEOR score
average_meteor = sum(meteor_scores) / len(meteor_scores)

print("Average METEOR Score:", average_meteor)
