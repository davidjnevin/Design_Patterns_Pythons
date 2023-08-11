"The Factory Class"
from big_chair import BigChair
from medium_chair import MediumChair
from small_chair import SmallChair


class ChairFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"

    @staticmethod
    def get_chair(chair):
        "A static method to get a chair"
        if chair == "BigChair":
            return BigChair()
        if chair == "MediumChair":
            return MediumChair()
        if chair == "SmallChair":
            return SmallChair()
        return None
