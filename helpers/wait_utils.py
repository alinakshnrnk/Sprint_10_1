import re


def parse_minutes_from_text(text: str) -> int:
    match = re.search(r"(\d+)\s*мин", text)
    if not match:
        raise ValueError(f"Не удалось найти количество минут в строке: {text!r}")
    return int(match.group(1))


def parse_price_from_text(text: str) -> int:
    if "Бесплатно" in text:
        return 0
    match = re.search(r"(\d+)\s*(₽|руб)", text)
    if not match:
        raise ValueError(f"Не удалось найти стоимость в строке: {text!r}")
    return int(match.group(1))
