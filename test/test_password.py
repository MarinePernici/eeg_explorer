# import pytest
# from front.functions.validity_functions import is_password_safe

# def test_input_not_safe():
#     result, errors = is_password_safe("Abc;--")
#     assert not result
#     assert len(errors) == 1
#     assert "n'est pas valide" in str(errors)

# def test_password_length():
#     result, errors = is_password_safe("Abc1!")
#     assert not result
#     assert len(errors) == 1
#     assert "12 caractères" in str(errors)

# def test_password_uppercase():
#     result, errors = is_password_safe("abcdefghijk1!")
#     assert not result
#     assert len(errors) == 1
#     assert "une lettre majuscule" in str(errors)

# def test_password_lowercase():
#     result, errors = is_password_safe("ABCDEFGHIJK1!")
#     assert not result
#     assert len(errors) == 1
#     assert "une lettre minuscule" in str(errors)

# def test_password_digit():
#     result, errors = is_password_safe("Abcdefghijkl!")
#     assert not result
#     assert len(errors) == 1
#     assert "un chiffre" in str(errors)

# def test_password_special_char():
#     result, errors = is_password_safe("Abcdefghijk1")
#     assert not result
#     assert len(errors) == 1
#     assert "un caractère spécial" in str(errors)

# # Test with two violations
# def test_password_short_no_digit():
#     result, errors = is_password_safe("Abcdef!")
#     assert not result
#     assert len(errors) == 2
#     assert "12 caractères" in str(errors)
#     assert "un chiffre" in str(errors)

# # Test with three violations
# def test_password_short_no_digit_no_upper():
#     result, errors = is_password_safe("abcdef!")
#     assert not result
#     assert len(errors) == 3
#     assert "12 caractères" in str(errors)
#     assert "un chiffre" in str(errors)
#     assert "une lettre majuscule" in str(errors)

# # Test with four violations
# def test_password_short_no_digit_no_upper_no_special():
#     result, errors = is_password_safe("abcdef")
#     assert not result
#     assert len(errors) == 4
#     assert "12 caractères" in str(errors)
#     assert "un chiffre" in str(errors)
#     assert "une lettre majuscule" in str(errors)
#     assert "un caractère spécial" in str(errors)

# # Test with all violations - empty password
# def test_password_all_violations():
#     result, errors = is_password_safe("")
#     assert not result
#     assert len(errors) == 5
#     assert "12 caractères" in str(errors)
#     assert "un chiffre" in str(errors)
#     assert "une lettre majuscule" in str(errors)
#     assert "une lettre minuscule" in str(errors)
#     assert "un caractère spécial" in str(errors)

# # Test avec un mot de passe valide
# def test_valid_password():
#     result, errors = is_password_safe("Abcdefghijk1!")
#     assert result
#     assert not errors
