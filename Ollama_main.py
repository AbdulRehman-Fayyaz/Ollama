import ollama
import time

client = ollama.Client()

# Download Ollama (https://ollama.com/download/OllamaSetup.exe) 
# then pip install ollama library (pip install ollama)
# then download and install the model you want to use locally (ollama run gemma4 {this model size is 6.6GB - 9.5GB}) (see more and find the models from https://ollama.com/search)
model = "llama3.1:latest" # specify the model version to use, that you have also installed locally
CONTEXT_LENGTH = 8192   # match your Ollama app setting (8k)

prompt = "what is the toughest material known to humans. " \
"Return only the requested answer and confidence in % on that answer." \
"Do not include reasoning or any extra fields."

start_time = time.perf_counter()
last = None   # will hold the final chunk with the statistics

print("Response from Ollama:")
for chunk in client.generate(
        model=model,
        prompt=prompt,
        stream=True,
        options={"temperature": 0.4, "num_predict": 1000}):  # num_predict is a hard limit on the number of tokens the model will generate
    print(chunk.response, end="", flush=True)

    if chunk.done:
        last = chunk

elapsed_time = time.perf_counter() - start_time
print()

# ---------- Summary ----------
prompt_tokens = last.prompt_eval_count or 0
answer_tokens = last.eval_count or 0
total_tokens = prompt_tokens + answer_tokens
ns = 1e9   # Ollama reports times in nanoseconds

print("\n--- Stats ---")
print(f"Total response time : {elapsed_time:.2f} s")
print(f"  Model load time   : {(last.load_duration or 0)/ns:.2f} s")
print(f"  Reading prompt    : {(last.prompt_eval_duration or 0)/ns:.2f} s")
print(f"  Writing answer    : {(last.eval_duration or 0)/ns:.2f} s")
print(f"Prompt tokens       : {prompt_tokens}")
print(f"Answer tokens       : {answer_tokens}")
print(f"Context used        : {total_tokens} of {CONTEXT_LENGTH} "
      f"({total_tokens / CONTEXT_LENGTH:.1%})")
if last.eval_duration:
    print(f"Speed               : {answer_tokens / (last.eval_duration/ns):.1f} tokens/s")
print(f"Stop reason         : {last.done_reason}  "
      f"('stop' = finished, 'length' = cut off by num_predict)")
