def generate_sequence(sequence, words, index, count):
    if words[index] in sequence and words[index] != words[-1]:
        return generate_sequence(sequence, words, index + 1, count)
    else:
        if sequence[-2:] == words[index][:2]:
            sequence += words[index][2:]
        elif words[index][-2:] == sequence[:2]:
            sequence = words[index] + sequence[2:]
        elif sequence == '':
            sequence = words[index]

        if index == len(words) - 1:
            new_sequence = [sequence]
            all_words_used = True
            if count != len(words):
                for word in words:
                    if word not in sequence:
                        all_words_used = False
            else:
                for word in words:
                    if word not in sequence:
                        new_sequence.append(word)
                return [sequence] + generate_sequence('', new_sequence[1:], 0, 0)
            if all_words_used:
                return new_sequence
            else:
                count += 1
                return generate_sequence(sequence, words, 0, count)
        else:
            return generate_sequence(sequence, words, index + 1, count)

word_list = ['ADIT', 'ITHY', 'HYAV' , 'AVAR' , 'ARDA','DAN.']
result_sequence = generate_sequence('', word_list, 0, 0)
for index, word in enumerate(result_sequence):
    print("Sequence", index + 1, ":", word)
