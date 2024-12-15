def capitalize(word):
    if word:
        return word[0].upper() + word[1:]
    else:
        return word
def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_words = [capitalize(word) for word in words]
    return ' '.join(capitalized_words)

input_string = str(input())
output_string = capitalize_sentence(input_string)
print(output_string)