from point import Point
from random import randint


class unitCircle:
    """Class to create a unit circle and generate a quiz based on it, made for practicing trigonometry mental conversions"""

    def __init__(self):
        self.radToDeg: dict[int, str] = {
            0: "0π", 30: "π/6", 45: "π/4", 60: "π/3", 90: "π/2", 120: "2π/3", 135: "3π/4", 150: "5π/6",
            180: "π", 210: "7π/6", 225: "5π/4", 240: "4π/3", 270: "3π/2", 300: "5π/3", 315: "7π/4", 330: "11π/6", 360: "2π"
        }
        self.degCoords: dict[int, Point] = {
            0: Point("1", "0"), 30: Point("√3/2", "1/2"), 45: Point("√2/2", "√2/2"), 60: Point("1/2", "√3/2"),
            90: Point("0", "1"), 120: Point("-1/2", "√3/2"), 135: Point("-√2/2", "√2/2"), 150: Point("-√3/2", "1/2"),
            180: Point("-1", "0"), 210: Point("-√3/2", "-1/2"), 225: Point("-√2/2", "-√2/2"), 240: Point("-1/2", "-√3/2"),
            270: Point("0", "-1"), 300: Point("1/2", "-√3/2"), 315: Point("√2/2", "-√2/2"), 330: Point("√3/2", "-1/2"), 360: Point(1, 0)
        }
        self.radCoords: dict[str, Point] = {
            "0π": Point("1", "0"), "π/6": Point("√3/2", "1/2"), "π/4": Point("√2/2", "√2/2"), "π/3": Point("1/2", "√3/2"),
            "π/2": Point("0", "1"), "2π/3": Point("-1/2", "√3/2"), "3π/4": Point("-√2/2", "√2/2"), "5π/6": Point("-√3/2", "1/2"),
            "π": Point("-1", "0"), "7π/6": Point("-√3/2", "-1/2"), "5π/4": Point("-√2/2", "-√2/2"), "4π/3": Point("-1/2", "-√3/2"),
            "3π/2": Point("0", "-1"), "5π/3": Point("1/2", "-√3/2"), "7π/4": Point("√2/2", "-√2/2"), "11π/6": Point("√3/2", "-1/2"),
            "2π": Point(1, 0)
        }

    def generateQuiz(self, numQuestions: int, quizType: str) -> str:
        """Generates a string that is a quiz, quizType can be degtorad for a quiz of
        radians to degrees or degrees to radians, or it can be degradtocoor which is
        a quiz that asks to find the coordinate for each degree or radian."""
        quiz: str = ""
        if quizType == "degtorad":
            quiz += "Convert the following degrees to radians and radians to degrees\n"
            for i in range(numQuestions):
                if (randint(0, 1) == 0):
                    quiz += str(i+1) + ". " + str(list(self.radToDeg)
                                                  [randint(0, len(self.radToDeg)-1)]) + "\n"
                else:
                    quiz += str(i+1) + ". " + str(list(self.radToDeg.values())
                                                  [randint(0, len(self.radToDeg)-1)]) + "\n"
        elif (quizType == "degradtocoor"):
            quiz += "Write the corresponding coordinate pair for each problem\n"
            for i in range(10):
                if (randint(0, 1) == 0):
                    quiz += str(i+1) + ". " + str(list(self.degCoords)
                                                  [randint(0, len(self.degCoords)-1)]) + "\n"
                else:
                    quiz += str(i+1) + ". " + str(list(self.radCoords)
                                                  [randint(0, len(self.radCoords)-1)]) + "\n"
        return quiz
