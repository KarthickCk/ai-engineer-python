class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = "water , milk , giner , masala "
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)


