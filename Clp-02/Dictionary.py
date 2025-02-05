text = "My Name is Razin Razin loves to play video game His favourite video game is GTA5"
w_count = {}

for word in text.split():
    w_count[word] = w_count.get(word, 0) + 1
    
print(w_count)