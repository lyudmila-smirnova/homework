from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_account_card: str) -> str:
    """Функция маскировки карты и счета"""
    if "Счет" in number_account_card:
        return "Счет " + get_mask_account(number_account_card)
    else:
        number_card = get_mask_card_number(number_account_card[-16:])
        mask_card = number_account_card.replace(number_account_card[-16:], number_card)
        return mask_card


print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))


def get_date(date: str) -> str:
    """Функция изменения формата даты"""
    return date[8:10] + "." + date[5:7] + "." + date[0:4]


print(get_date("2024-03-11T02:26:18.671407"))
