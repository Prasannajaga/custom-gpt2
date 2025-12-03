with open("input.txt" , "r" , encoding="utf-8") as f:
    text = f.read()


print("Length of the text" , len(text)) 
# text length === chars 
chars = sorted(set(list(text)))
vocab_size = len(chars)

# we have 65 unique chars tokens 
print("vocab_size" , vocab_size)


# for all the given chars map with integer for tokenizer
stoi = {ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)} 

# def encode(s):
#     data = []
#     for c in s:
#         data.append(stoi[c])
#     return data


# def decode(s):
#     response = []
#     for i in s:
#         response.append(itoi[i])
#     return "".join(response)

# the above and below is pretty much same but with lamba 

encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string
    
encodeX = encode("prasanna")
decodeX = decode(encodeX)

print(encodeX)
print(decodeX)

# so far tokenizer is ready now we have to implement this in a tensor 