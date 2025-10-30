def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            # Raise a ValueError if the rate is out of a sensible range
            raise ValueError(rate)  # raise Exception_class, <value>

        interest = (amount * year * rate) / 100.0
        print('The Simple Interest is', interest)
        return interest
    except ValueError:
        # Catches the ValueError that was explicitly raised
        print('interest rate is out of range', rate)

print('Case 1')
simple_interest(800, 6, 8)

print('Case 2')
simple_interest(800, 6, 800)

# Output:
# Case 1
# The Simple Interest is 384.0
# Case 2
# interest rate is out of range 800