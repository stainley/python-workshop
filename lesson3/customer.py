def format_customer(first_name, last_name, location=None):
    full_name = '%s %s' % (first_name, last_name)

    if location:
        return '%s (%s)' % (full_name, location)
    else:
        return full_name


def is_prime(x):
    for i in range(2, x):
        if (x % i) == 0:
            return False
        return True


print(is_prime(1000))
