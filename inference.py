import os
import requests
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

    # Latest Stable Router URL
    API_URL = "https://router.huggingface.co/hf-inference/v1/chat/completions"
    
    api_token = os.getenv('finops_ui')
    if not api_token:
        print("❌ Error: 'finops_ui' secret not found in Settings.")
        return

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # Prompt and Payload for Chat Interface
    prompt = f"FinOps Report: Initial Cost {initial_cost}, Final Cost {final_cost}. Suggest one quick optimization tip."
    
    payload = {
        "model": "openai-community/gpt2",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 50
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        
        if response.status_code == 200:
            result = response.json()
            # Extracting text from the chat completion response
            ai_text = result['choices'][0]['message']['content']
            print("\n🤖 [AI FEEDBACK]:")
            print(ai_text.strip())
        else:
            print(f"⚠️  AI Model Error (Status {response.status_code}):")
            print(f"Message: {response.text}")

    except Exception as e:
        print(f"❌ Connection Error: {e}")

    print("\n🏁 [END]")

if __name__ == "__main__":
    run_finops()