https://josehoras.github.io/lstm-pure-python/

#Forward pass
h_states, h_cache = lstm_forward(inputs, prev_h, Wx, Wh, b)
scores = np.dot(h_states, Why.T) + by
probabilities = np.exp(scores) / np.sum(np.exp(scores), axis=1, keepdims=True)
cross_entropy = -np.log(probs[range(seq_length), np.argmax(targets, axis=1)])
loss = np.sum(correct_logprobs) / seq_length
_, H = prev_h.shape
a = prev_h.dot(Wh) + x.dot(Wx) + b      # (1, 4*hidden_dim)
i = sigmoid(a[:, 0:H])
f = sigmoid(a[:, H:2*H])
o = sigmoid(a[:, 2*H:3*H])
g = np.tanh(a[:, 3*H:4*H])              # (1, hidden_dim)
next_c = f * prev_c + i * g             # (1, hidden_dim)
next_h = o * (np.tanh(next_c))          # (1, hidden_dim)
cache = x, prev_h, prev_c, Wx, Wh, b, a, i, f, o, g, next_c
return next_h, next_c, cache

scores = np.dot(h_states, Why.T) + by

probabilities = np.exp(scores) / np.sum(np.exp(scores), axis=1, keepdims=True)

cross_entropy = -np.log(probs[range(seq_length), np.argmax(targets, axis=1)])

loss = np.sum(correct_logprobs) / seq_length

#Backward pass

dscores = probs
dscores[range(seq_length), np.argmax(targets, axis=1)] -= 1
dWhy = dscores.T.dot(h_states)
dby = np.sum(dscores, axis=0)
dh_states = dscores.dot(Why)
dx, dh_0, dWx, dWh, db = lstm_backward(dh_states, h_cache)

for param, dparam in zip([Wx, Wh, Why, b, by], [dWx, dWh, dWhy, db, dby]):
    param -= learning_rate * dparam
    
def sample(x, h, txt_length):
    txt = ""
    c = np.zeros_like(h)
    for i in range(txt_length):
        h, c, _ = lstm_step_forward(x, h, c, Wx, Wh, b)
        scores = np.dot(h, Why.T) + by
        prob = np.exp(scores) / np.sum(np.exp(scores))
        pred = np.random.choice(range(input_dim), p=prob[0])
        x = aux.encode([pred], vocab_size)
        next_character = idx_to_char[pred]
        txt += next_character
    return txt