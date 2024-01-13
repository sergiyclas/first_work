"""Without modules"""


class Musician:
    """
    Musician description
    """

    def __init__(self, name="Endryu", age=24, salary=100.00, rank=100):
        """
        Initialisation of name, age, salary and ранку rank of popularity
        """
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__rank = rank

    def __del__(self):
        return f"Musician {self.__name} was destroyed"

    def __repr__(self):
        return "Musician object"

    def get_info(self):
        """
        Return an information about musucian
        """
        return {
            "Musician": self.__name,
            "Age": self.__age,
            "Salary": f"{self.__salary}$",
            "Rank of popularity": self.__rank,
        }

    @property
    def name(self):
        """
        name setter
        """
        return self.__name

    @property
    def age(self):
        """
        age setter
        """
        return self.__age

    @property
    def salary(self):
        """
        salary setter
        """
        return self.__salary

    @property
    def rank(self):
        """
        rank setter
        """
        return self.__rank

    def get_salary(self):
        """
        Gives salary
        """
        return self.__salary

    def get_rank(self):
        """
        Gives rank
        """
        return self.__rank


class MusicFestival:
    """
    Festival description
    """

    def __init__(self, *args, max_money=1000.00):
        """
        Initialisation of max budget and musicians, who will perfom on festival(list of musicians)
        """
        self.musician_list = []
        self.all_musician_dict = {}
        self.max_money = max_money
        self.musicians = list(args)

    def get_main_information(self):
        """
        Return main information about fest
        """
        return {
            "Max budget": f"{self.max_money}$",
            "List of musicians": self.musicians,

        }

    def input_all_musician_dict(self, dict_):
        """
        Imput all musician dict
        """
        self.all_musician_dict = dict_.copy()

    def sort_musician_by_rank(self):
        """
        Sorting musicians by using rank
        """
        count = 0
        error_ = "Not found musician"
        for _ in range(len(self.musicians) ** 2):
            count += 1
            if count >= len(self.musicians):
                count = 1
            first = self.all_musician_dict.get(self.musicians[count - 1], "Not found musician")
            second = self.all_musician_dict.get(self.musicians[count], "Not found musician")

            if first is error_ or second is error_:
                if first == error_:
                    del self.musicians[count - 1]
                if second == error_:
                    del self.musicians[count]
            elif first.get_rank() > second.get_rank():
                self.musicians[count - 1], self.musicians[count] = (
                    self.musicians[count], self.musicians[count - 1])

    def del_musician(self, musician):
        """
        Delete musician from list
        """
        self.musician_list.remove(musician)

    def add_musician(self, musician):
        """
        Add musician to list
        """
        self.musician_list.append(musician)

    def sum_money(self):
        """
        Summing all salary musicians of list
        """
        sum_ = 0
        if not lst:
            return 0

        for musician in self.musician_list:
            member_musician = self.all_musician_dict.get(musician, "Not found musician")
            if member_musician == "Not found musiciant":
                print("Not found such a musician in list")
                return None
            sum_ += member_musician.get_salary()

        return sum_

    def valid_musicians(self):
        """
        Validation of musicians, who has too big salary
        """
        for i in self.musicians:
            musician = self.all_musician_dict.get(i, "Not found")
            if musician == "Not found":
                continue

            money_ = musician.get_salary()
            possible_budget = self.max_money - self.sum_money()
            if possible_budget - money_ >= 0:
                self.add_musician(i)

    def returning(self):
        """
        Return all values
        """
        return {
            "List of musicians": self.musician_list,
            "Need budget": self.sum_money(),
        }


all_musician_dict = {}

if __name__ == "__main__":
    all_musician_dict = {"Andriy": Musician("Andriy", 12, 123, 234),
                         "Serhiy": Musician("Serhiy", 32, 1233, 14),
                         "Tedy": Musician("Tedy", 54, 899, 15),
                         }


    music_festival = MusicFestival("Andriy", "Serhiy", "Tedy", max_money=2000)
    music_festival.input_all_musician_dict(all_musician_dict)
    music_festival.sort_musician_by_rank()
    music_festival.valid_musicians()
    print(music_festival.returning())

musician_12 = all_musician_dict.get("Andriy", "Hasn`t found")
