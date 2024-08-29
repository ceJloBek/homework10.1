def get_mask_card_number(card_number: str):
    return f'{card_number[:5]} {card_number[4:6]} {"*" * 2} {"*" * 4} {card_number[12:]}'


def get_mask_account(score_number: str):
    return f'{"*" * 2} {score_number[16:]}'
