#!/usr/bin/env python3


class TfnValidator:
    """
    Create object using potential TFN, run the validation algorithm using this number.
    """

    def __init__(self, candidate: list) -> None:
        """
        Instance variables
        """
        self.candidate: list = candidate
        self.weighting: list = [1, 4, 3, 7, 5, 8, 6, 9, 10]
        self.total: int = 0

    def validate(self):
        """
        Multiply each digit of the candidate TFN by the corresponding weighting
        and sum them together.
        """
        try:
            i = 0
            while i < len(self.candidate):
                result: int = int(self.candidate[i]) * int(self.weighting[i])
                self.total = self.total + result
                i += 1
        except Exception as e:
            raise SystemExit(e) from e

    def checkmod(self):
        """
        If the sum total of all digits multiplied by the weighting
        is divisible by 11, the candidate is a valid TFN.
        """
        try:            
            mod = self.total % 11
            if mod == 0:
                print("".join(self.candidate) + " is a valid TFN.")
            else:
                print("".join(self.candidate) + " is NOT a valid TFN.")
        except Exception as e:
            raise SystemExit(e) from e


def main():
    """
    main 
    """
    try:
        def get_candidate():
            candidate: list = list(input("Enter potential TFN: ").replace(" ", ""))
            return candidate
    except Exception as e:
        raise SystemError(e) from e
    tfn = TfnValidator(get_candidate())
    tfn.validate()
    tfn.checkmod()


if __name__ == "__main__":
    main()
