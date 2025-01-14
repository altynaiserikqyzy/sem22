text = "   hello world!   "
new_text = text.strip()
new_text = new_text.upper()
new_text = new_text.replace("WORLD", "PYTHON")
word_list = new_text.split()
final_text = " ".join(word_list)
print(final_text)