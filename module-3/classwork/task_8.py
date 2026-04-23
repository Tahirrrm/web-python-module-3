text= "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore etdolore magna aliqua.ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex eacommodo consequat.duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nullapariatur.Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
sentences = [s.strip() for s in text.split('.') if s.strip()]
capitalized_sentences = []
for sentence in sentences:
    if sentence: 
        capitalized = sentence[0].upper() + sentence[1:]
        capitalized_sentences.append(capitalized)
result = ". ".join(capitalized_sentences) + "."
print(result)
count= sum(x.isdigit() for x in text)
print(count)
signs= "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
signs_count= sum(1 for y in text if y in signs)
print (signs_count)
exclamation_mark=sum(1 for y in text if y in "!")
print(exclamation_mark)