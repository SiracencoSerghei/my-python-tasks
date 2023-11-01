class Power:
    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, basis):
        return basis ** self.exponent


power_of_3 = Power(3)
print(power_of_3(3))
power_of_2 = Power(2)
print(power_of_2(3))

# =====================
