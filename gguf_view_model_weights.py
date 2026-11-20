from gguf import GGUFReader
from gguf.quants import dequantize

# Update this path to point to your GGUF model file, currently set to a ABB_path
path = r"C:\Users\DEABREH\.ollama\models\blobs\sha256-667b0c1932bc6ffc593ed1d03f895bf2dc8dc6df21db3042284a6f4416b06a29"
reader = GGUFReader(path)

# Total number of parameters (should be about 8 billion)
total = sum(int(t.n_elements) for t in reader.tensors)
print(f"Total parameters: {total:,}")

# List the first few tensors (blocks of numbers)
for t in reader.tensors[:10]:
    print(t.name, t.shape.tolist(), t.tensor_type.name)

# Show actual raw numbers from one tensor
t = next(t for t in reader.tensors if t.name == "blk.0.attn_q.weight")
values = dequantize(t.data, t.tensor_type)
print(values.flatten()[:200])
