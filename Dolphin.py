from dolphin import controller, event


class Dolphin:
    def __init__(self):
        self.controls = None

    def getControls(self, A, B, X, Y, Z, Left, Right, RTrigger, LTrigger, Start):
        if not self.controls:
            self.controls = {
                        "A": A or "A" ,
                        "B": B or"B",
                        "X": X or "X",
                        "Y": Y or "Y",
                        "Z": Z or "Z",
                        "Left": Left or "Left",
                        "Right": Right or "Right",
                        "RTrigger": RTrigger or "Q", 
                        "LTrigger": LTrigger or "E",
                        "Start": Start or "Enter"
                        }
            return self.controls

    async def accelerate():
        ...

    async def steer(direction):
        ...

    async def useItem():
        def checkItem():
            ...

        

        


d = Dolphin()

controls = d.getControls()
print(controls, controller.get_gc_buttons(0))
