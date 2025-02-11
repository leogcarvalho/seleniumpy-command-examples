# O assert sempre verifica se o retorno da condição é True
# assert True

# assert numbers
# num_esperado = 3
# num_obtido = 2
# assert num_esperado != num_obtido, f"Esperado {num_esperado} não é maior que o numero Atual {num_obtido}."

# assert text
# text_esperado = "Selenium Webdriver"
# text_obtido = "Selenium webdriver"
# assert text_esperado == text_obtido, f"Esperado {text_esperado}. Atual {text_obtido}."

# assert text in string
text_esperado = "Seleniumzzzzzz"
text_obtido = "Selenium Webdriver"
assert text_esperado not in text_obtido, f"Esperado '{text_esperado}' dentro da string Atual '{text_obtido}'."

# assert is_displayed/is_enabled/is_selected

