# Ollama Local LLM

This is a small side project where I test local AI models with Ollama.

`Ollama_main.py` sends a prompt to a model and shows its response and timing. `gguf_view_model_weights.py` lets me explore model weights.

## Just Run and try it out, it won't bite

1. Install [Ollama](https://ollama.com/download/windows).
2. Download a model, for example: `ollama pull llama3.1:latest`
3. Install the Python package: `python -m pip install ollama`
4. Run: `python Ollama_main.py`

## Settings you can change

In `Ollama_main.py`:

- `model`: choose a model already downloaded to your computer.
- `prompt`: change the question and instructions sent to the model.
- `temperature`: controls how varied the answer is. Lower is more consistent; higher is more creative.
- `num_predict`: maximum number of tokens in the answer.
- `stream`: shows the answer as it is generated (`True`) or all at once (`False`).
- `CONTEXT_LENGTH`: used only to estimate context usage in the printed stats.


### Other options you can add

Add these to the `options` dictionary in `client.generate()`:

- `num_ctx`: set the model's context size.
- `top_k` and `top_p`: control how broadly the model chooses the next word.
- `min_p`: filter out unlikely next words.
- `repeat_penalty`: reduce repeated words or phrases.
- `repeat_last_n`: choose how many recent tokens to check for repetition.
- `presence_penalty` and `frequency_penalty`: discourage repeated topics or words.
- `typical_p`: adjust how predictable the answer is.
- `mirostat`, `mirostat_tau`, and `mirostat_eta`: alternative controls for answer variety.
- `seed`: make results more repeatable.
- `stop`: stop generation when a chosen word or phrase appears.
- `num_thread`: set how many CPU threads to use.
- `num_batch`: set the prompt-processing batch size.

For example: `options={"temperature": 0.4, "num_predict": 1000, "num_ctx": 8192, "top_p": 0.9}`

Options can behave differently depending on the model and your computer. You usually only need to change a few.

## Useful terminal commands

- `ollama list` — show downloaded models.
- `ollama ps` — show models currently running.
- `ollama pull llama3.1:latest` — download a model.
- `ollama run llama3.1:latest` — chat with a model in the terminal.
- `ollama stop llama3.1:latest` — stop a running model.
- `ollama rm llama3.1:latest` — delete a downloaded model and free disk space.
- `ollama show llama3.1:latest` — show model details.
- `ollama cp llama3.1:latest my-model` — make a copy of a model with a new name.
- `ollama serve` — start the Ollama server.
- `ollama help` — show available commands.

## Hardware tips and things to remember

- **GPU is optional.** Ollama can use your CPU, but a compatible GPU usually makes answers faster.
- **Rough memory guide for 4-bit models:** 7B needs about 4–6 GB, 14B about 9–12 GB, and 30B about 18–24 GB. Leave extra memory for the system and context.

- Model files also need disk space. Check `ollama list` and remove models you no longer use with `ollama rm MODEL`.
