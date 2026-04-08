import random

def agent_action():
    return random.choice([
        "reduce_vms",
        "increase_vms",
        "optimize_storage"
    ])