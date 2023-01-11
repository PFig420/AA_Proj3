from collections import Counter
import string
import random
import time
import urllib.request  # the lib that handles the url stuff

def fixed_probability_count(file_name, probability):
    start = time.time()
    text_flag_fpc = False
    counter = {}
    for letter in string.ascii_uppercase:
        counter[letter] = 0
    with urllib.request.urlopen(file_name) as f:
        for line in f:
            line = line.decode('utf-8')
            if "*** S" in line:
                text_flag_fpc = True
            if "*** E" in line:
                break
            if text_flag_fpc:
                if len(line) == 2:
                    continue
                else:
                    for char in line:
                        if random.random() < probability:
                            if char in string.ascii_lowercase or char in string.ascii_uppercase:
                                counter[char.upper()] += 2   

    k = Counter(counter)
    high = k.most_common(3)     
    return high, time.time() - start


links = ["https://www.gutenberg.org/files/62615/62615-0.txt", "https://www.gutenberg.org/cache/epub/30/pg30.txt", "https://www.gutenberg.org/files/62383/62383-0.txt"]

for i in range(20):
    max_en = max_pt = max_fr = 0
    avg_en = avg_pt = avg_fr = 0
    min_en = min_pt = min_fr = 0
    for link in links:
        cnt_fpc, timer = fixed_probability_count(link, 0.5)
        print("Probability Counter")
        print(cnt_fpc)
        print(timer)
        if link == "https://www.gutenberg.org/files/62615/62615-0.txt":
            if cnt_fpc[0][1] > max_en:
                max_en = cnt_fpc[0][1]
            elif cnt_fpc[0][1] < min_en:
                min_en = cnt_fpc[0][1]
            avg_en += cnt_fpc[0][1]
        