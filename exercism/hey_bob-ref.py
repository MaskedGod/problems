def response(hey_bob: str):
    """
    Extract conditionals into well-named variables: This will help make the logic more readable.
    Use the strip() function once: It can be called once and reused instead of multiple times in different conditions.
    Rearrange conditions: Handle strip() earlier to avoid repeated use and streamline the logic.
    """
    hey_bob = hey_bob.strip()

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if not hey_bob:
        return "Fine. Be that way!"
    elif is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"

    return "Whatever."


def response(hey_bob: str) -> str:
    # Strip whitespace to handle empty input easily
    hey_bob = hey_bob.strip()

    # Since checking for an empty or whitespace-only string is a base case, we can handle it upfront and
    # return immediately, reducing unnecessary checks for other conditions.
    if not hey_bob:
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"

    return "Whatever."


def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    responses = {
        (True, True): "Calm down, I know what I'm doing!",  # Question + Yelling
        (True, False): "Sure.",  # Question only
        (False, True): "Whoa, chill out!",  # Yelling only
    }

    return responses.get((is_question, is_yelling), "Whatever.")


def response(hey_bob: str, responses=None) -> str:
    # This function now allows passing custom responses as a dictionary argument.
    # Customization: You can pass Bob's responses as arguments if
    # you foresee needing different types of responses based on specific inputs, keeping the core function flexible.
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return responses.get("silence", "Fine. Be that way!")

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    default_responses = {
        (True, True): "Calm down, I know what I'm doing!",
        (True, False): "Sure.",
        (False, True): "Whoa, chill out!",
        "silence": "Fine. Be that way!",
        "default": "Whatever.",
    }

    responses = responses or default_responses
    return responses.get((is_question, is_yelling), responses["default"])
