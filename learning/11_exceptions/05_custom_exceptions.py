def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError(f"{flavor} unsupported chai flavor...")
    print(f"Brewing {flavor}...")

brew_chai("masala")