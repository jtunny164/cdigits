#   Puzzle: Find a ten-digit number that uses each of the digits
#   0 through 9, such that the first digit is evenly divisable by
#   1 (trivially true), the number formed by the first two digits
#   is evenly divisible by 2, the number formed by the first three
#   digits is evenly divisible by 3, and so on for each of the ten
#   digits.

import time

def gen_possible():
    # This is sort of an optimized brute force approach. Given the
    # constraints of the problem, the various digits must correspond
    # to numbers divisible by that place index. For example, because the final
    # number must be divisible by 10, the final digit must be zero, which
    # means it can't be used in any other position. That means the fifth
    # position (divisible by 5) must be 5. The even positions must be
    # even (and not 0), and because that uses up all the even digits, all
    # the odd positions must be odd (and not 5). It reduces the numbers to
    # be tested from 10 billion to just 64K, a factor of over 150,000.
    #
    d = [0] * 11                # just pre-size digit list
    odddigit = [1,3,7,9]
    evendigit = [2,4,6,8]
    d[1] = odddigit             # must be odd [1,2,7,9]
    d[2] = evendigit            # must be even
    d[3] = odddigit             # must be odd [1,2,7,9]
    d[4] = evendigit            # must be even
    d[5] = [5]                  # must be 5 (0 will be in the final place)
    d[6] = evendigit            # must be even
    d[7] = odddigit             # must be odd [1,2,7,9]
    d[8] = evendigit            # must be even
    d[9] = odddigit             # must be odd [1,2,7,9]
    d[10] = [0]                 # must be zero
    for d1 in d[1]:
        for d2 in d[2]:
            for d3 in d[3]:
                for d4 in d[4]:
                    for d5 in d[5]:
                        for d6 in d[6]:
                            for d7 in d[7]:
                                for d8 in d[8]:
                                    for d9 in d[9]:
                                        for d10 in d[10]:
                                            yield [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]

def meets_constraints(digits, debug=False):
    test_val = 0
    power = 0
    pos = 1
    for dig in digits:
        test_val = test_val * 10 + dig
        power += 1
        if ((test_val % pos) != 0):
            return False        # give up at first failure
        pos += 1
    return True

def digits_to_int(digits):
    val = 0
    power = 0
    for dig in reversed(digits):
        val += dig * (10 ** power)
        power += 1
    return val

def find_solutions():
    cnt = 0
    found = 0
    digitset = frozenset([0,1,2,3,4,5,6,7,8,9])
    t0 = time.perf_counter()
    for p in gen_possible():
        cnt += 1
        if (set(p) == digitset):    # solution must use all digits 0-9
            if (meets_constraints(p)):
                # Found an answer!
                first_found_at = time.perf_counter()
                elapsed = first_found_at - t0
                # Show that it works
                print(f"Found solution: {digits_to_int(p)} in {elapsed:.3f} seconds -- validating:")
                validate_answer(p)
                found += 1
    elapsed = time.perf_counter() - t0
    print(f"\nDone, found {found} solutions in {elapsed:.3f} seconds")
    print(f"Total of {cnt} possible values tested")

def validate_answer(p):
    val = 0
    div = 1
    for digit in p:
        val = val * 10 + digit
        print(f"{val} is {div} times {val / div:.0f}")
        div += 1

def main():
    print("Puzzle: Find a ten-digit number that uses each of the digits")
    print("0 through 9, such that the first digit is evenly divisable by")
    print("1 (trivially true), the number formed by the first two digits")
    print("is evenly divisible by 2, the number formed by the first three")
    print("digits is evenly divisible by 3, and so on for each of the ten")
    print("digits.\n")
    input("Hit return to compute solution...")
    print()
    find_solutions()

if __name__ == "__main__":
    main()

