from nltk.tokenize import word_tokenize
question_words = ["what", "why", "when", "where",
             "name", "is", "how", "do", "does",
             "which", "are", "could", "would",
             "should", "has", "have", "whom", "whose", "don't", "am"]

question = input("Input a sentence: ")
question = question.lower()
question = word_tokenize(question)

if any(x in question[0] for x in question_words):
    print("This is a question!")
else:
    print("This is not a question!")