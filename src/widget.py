from src.masks import get_mask_account,get_mask_card_number

def mask_account_card(card_string: str) -> str | None:
    """Функции маскируют счеты и карты"""
    list_card_string = card_string.split()
    if "Visa Platinum" in card_string or "Maestro" in card_string:
        return f'{" ".join(list_card_string[:-1])} {get_mask_card_number(list_card_string[-1])}'
    else:
        return f'{"".join(list_card_string[:-1])} {get_mask_account(list_card_string[-1])}'
    return None

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))

def get_date(date: str) -> str:
    """Функция меняет формат даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"

print(get_date("2024-03-11T02:26:18.671407"))


