# Функтор - потрібний коли ми хочимо викликати екземпляр об'єкта як функцію
# Функтор - це коли екземпляр класу може сам себе викликати

class Count:
    def __init__(self, init_steps):
        self.steps = init_steps

    def __call__(self, *args, **kwargs):
        inc, = args  # (25,)
        self.steps += inc


count_step = Count(100)
count_step(25)
count_step(50)
print(count_step.steps)