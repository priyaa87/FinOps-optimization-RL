import os
from openai import OpenAI
from env import FinOpsEnv
from agent import agent_action
from grader import grade_performance

def run_finops():
    print("\n🚀 [START] FinOps Optimization Loop")

    # [STEP] Initializing environment
    print("[STEP] Initializing environment...")
    env = FinOpsEnv(level="medium")
    state = env.reset()
    initial_cost = env.initial_cost
    print(f"📊 Initial State: {state}")
    print(f"💰 Initial Cost: {initial_cost}")

    # [STEP] Running agent
    print("[STEP] Running agent...")
    for i in range(15):
        action = agent_action()
        state, reward, done = env.step(action)
        print(f"  ↳ Step {i+1} | Action: {action}, Reward: {reward}")
        if done:
            break

    final_cost = env.calculate_cost()
    print(f"✅ Final Cost: {final_cost}")

    # [STEP] Grading performance
    print("[STEP] Grading performance...")
    score = grade_performance(initial_cost, final_cost)
    print(f"🏆 Performance Score: {score}")

    # [STEP] Calling AI model
    print("[STEP] Calling AI model...")

    # Mandatory Hackathon Variables
    api_base = os.getenv("API_BASE_URL", "https://router.huggingface.co/hf-inference/v1")
    model_name = os.getenv("MODEL_NAME", "openai-community/gpt2")
    hf_token = os.getenv("HF_TOKEN") 

    if not hf_token:
        print("❌ Error: HF_TOKEN missing in Settings.")
        return

    try:
        # Rules ke mutabiq OpenAI client initialize karna
        client = OpenAI(base_url=api_base, api_key=hf_token)

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": f"Initial cost {initial_cost}, final cost {final_cost}. Quick FinOps tip?"}
            ],
            max_tokens=50
        )

        print("\n🤖 [AI FEEDBACK]:")
        print(response.choices[0].message.content.strip())

    except Exception as e:
        print(f"⚠️  AI Model Error: {e}")

    print("\n🏁 [END]")

if __name__ == "__main__":
    run_finops()