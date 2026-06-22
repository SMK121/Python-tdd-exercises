


def mask_email(email):
    """
    Mask an email address, leaving only first character of username visible.
    """

    # split email into username and domain
    username, domain = email.split("@")

    # keep first letter, replace rest with *
    masked_username = username[0] + "*" * (len(username) - 1)

    #  Return the masked email
    return masked_username + "@" + domain

print(mask_email("neo@gmail.com"))
print(mask_email("neo.anderson@yahoo.com"))