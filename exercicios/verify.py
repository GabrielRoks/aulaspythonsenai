def verify_float(*args: str) -> bool | None:

    for arg in args:
        try:
            float(arg)

        except (ValueError, TypeError):
            return False
    return True


def verify_int(*args: str) -> bool | None:
    for arg in args:
        try:
            int(arg)
        except (ValueError, TypeError):
            return False
    return True


def convert_float(*args: str) -> list[float]:
    return [float(arg) for arg in args]


def convert_int(*args: str) -> list[int]:
    return [int(arg) for arg in args]
