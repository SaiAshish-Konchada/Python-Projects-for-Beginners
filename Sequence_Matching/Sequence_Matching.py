from difflib import SequenceMatcher
text1 = "Coding is awesome!"
text2 = "Isn't coding awesome and amazing?"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")