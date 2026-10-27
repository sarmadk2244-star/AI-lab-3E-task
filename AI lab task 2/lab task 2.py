class TemperatureController:
    def __init__(self):
        self.previous_mode = None

    def choose_mode(self, temperature, occupied):
        
        if not occupied:
            target = "OFF"
        elif temperature < 18:
            target = "HEAT"
        elif temperature > 30:
            target = "COOL"
        else:
            
            target = "NORMAL"

        # Send a command only when the target differs from the last target.
        send_command = (target != self.previous_mode)
        previous = self.previous_mode
        self.previous_mode = target
        return previous, target, send_command


tests = [
    ("Repeated percept, first time", 22, True),
    ("Repeated percept, same again", 22, True),
    ("Lower exact boundary", 18, True),
    ("Upper exact boundary", 30, True),
    ("Mode transition to cooling", 31, True),
    ("Empty room overrides temperature", 25, False),
    ("Repeated empty-room percept", 25, False),
]

controller = TemperatureController()
for label, temperature, occupied in tests:
    previous, target, send = controller.choose_mode(temperature, occupied)
    action = "SEND COMMAND" if send else "NO COMMAND"
    print(f"{label}: previous={previous}, percept=(temp={temperature}, occupied={occupied}), "
          f"target={target}, outcome={action}"