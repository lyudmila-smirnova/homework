def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера банковской карты"""
    return number_card[:4] + " " + number_card[5:7] + "** **** " + number_card[-4:]

print(get_mask_card_number("7000792289606361"))


def get_mask_account(number_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    return "**" + number_account[-4:]


print(get_mask_account("73654108430135874305"))
