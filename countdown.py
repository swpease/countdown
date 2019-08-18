import sys
import itertools

from Num import Num


def main():
    input_nums = [int(i) for i in sys.argv[1:7]]
    target = int(sys.argv[7])
    products = []

    base_nums = []
    for index, num in enumerate(input_nums):
        base_nums.append(Num(num, index))
    products.append(base_nums)

    while len(products) < len(input_nums):
        lo = 0
        hi = len(products) - 1
        row = []

        while lo <= hi:
            if lo == hi:
                pairs = itertools.combinations(products[lo], 2)
            else:
                pairs = itertools.product(products[lo], products[hi])

            for pair in pairs:  # type(pair) = (Num, Num)
                if Num.is_disjoint(*pair):
                    possible_answers = Num.combine(*pair)  # type(p_a) = list(Num)
                    for answer in possible_answers:
                        if answer.value == target:
                            print(answer)
                            return
                        else:
                            row.append(answer)
            lo += 1
            hi -= 1

        products.append(row)

    print("No answer found")
    return


if __name__ == "__main__":
    main()
