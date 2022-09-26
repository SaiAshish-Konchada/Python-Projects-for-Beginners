from rake_nltk import Rake
rake_nltk_var = Rake()

text = """ Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation. 
Python is dynamically-typed and garbage-collected. 
It supports multiple programming paradigms, including structured, object-oriented and functional programming"""

rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)