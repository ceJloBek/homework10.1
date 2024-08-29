def mask_account_card(card_number: str) -> str:
    if 3 == "Счет":
       return f'{card_number[:-20]}{card_number[:-16]}'
    else:
        return f'{card_number[:-16]}{card_number[:5]} {card_number[4:6]} {"*" * 2} {"*" * 4} {card_number[12:]}'



