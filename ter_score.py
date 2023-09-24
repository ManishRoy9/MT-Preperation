import sys
from nltk.translate.gleu_score import sentence_gleu

def ter_score(reference_file, hypothesis_file):
    reference_file = reference_file.strip()
    hypothesis_file = hypothesis_file.strip()

    # Load references and hypotheses as lists of sentences
    with open(reference_file) as ref_file:
        references = ref_file.readlines()
    with open(hypothesis_file) as hyp_file:
        hypotheses = hyp_file.readlines()

    # Tokenize the sentences
    references = [ref.strip().split() for ref in references]
    hypotheses = [hyp.strip().split() for hyp in hypotheses]

    # Calculate TER score using GLEU for each sentence pair
    scores = [sentence_gleu([ref], hyp) for ref, hyp in zip(references, hypotheses)]

    # Calculate the average TER score
    ter_score = sum(scores) / len(scores)

    return ter_score

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ter_score.py reference_file hypothesis_file")
        sys.exit(1)

    reference_file = sys.argv[1]
    hypothesis_file = sys.argv[2]

    score = ter_score(reference_file, hypothesis_file)
    print("TER Score:", score)
