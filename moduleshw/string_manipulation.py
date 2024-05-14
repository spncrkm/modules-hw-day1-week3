import moduleshw.text_utils as tu

input_str = "hi my name is Spencer"
reversed_str = tu.reversing_string(input_str)
capitalized_str = tu.capitalize_string(input_str)
capitalize_all_words = tu.cap_each_word(input_str)

print("Original string:", input_str)
print("Reversed string:", reversed_str)
print("Capitalized string:", capitalized_str)
print("Titled string:", capitalize_all_words)
