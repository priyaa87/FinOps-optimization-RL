class FinOpsEnv:
    def __init__(self, level="easy"):
        self.level = level
        self.reset()

    def reset(self):
        if self.level == "easy":
            self.vms = 5
            self.cpu = 40
            self.storage = 200

        elif self.level == "medium":
            self.vms = 10
            self.cpu = 60
            self.storage = 400

        else:  # hard
            self.vms = 15
            self.cpu = 85
            self.storage = 800

        self.initial_cost = self.calculate_cost()
        return self.state()

    def state(self):
        return {
            "vms": self.vms,
            "cpu": self.cpu,
            "storage": self.storage
        }

    def calculate_cost(self):
        return self.vms * 10 + self.storage * 0.1

    def step(self, action):
        # ACTIONS
        if action == "reduce_vms":
            self.vms = max(1, self.vms - 1)

        elif action == "increase_vms":
            self.vms += 1

        elif action == "optimize_storage":
            self.storage = max(0, self.storage - 50)

        elif action == "increase_cpu":
            self.cpu = min(100, self.cpu + 10)

        # NEW COST
        new_cost = self.calculate_cost()

        # REWARD LOGIC 🔥
        cost_diff = self.initial_cost - new_cost

        reward = cost_diff / 100  # normalize

        # Penalty for bad decisions
        if self.cpu > 90:
            reward -= 1

        if self.vms > 20:
            reward -= 1

        # DONE condition
        done = new_cost < (self.initial_cost * 0.6)

        return self.state(), reward, done