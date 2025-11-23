from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def email(self) -> str:
        return self.faker.email()

    def password(self) -> str:
        return self.faker.password()

    def uuid(self) -> str:
        return self.faker.uuid()

    def description(self) -> str:
        return self.faker.sentence()

    def first_name(self) -> str:
        return self.faker.first_name()

    def last_name(self) -> str:
        return self.faker.last_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def estimated_time(self) -> str:
        return f"{self.int(start=1, end=30)} days"

    def int(self, start, end) -> int:
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        return self.int(start=50, end=100)

    def min_score(self) -> int:
        return self.int(start=0, end=49)

fake = Fake(faker=Faker())