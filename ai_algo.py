class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def add_word(root, word):
    """Adds a word to the tree.

    Args:
        root: The root node of the tree.
        word: The word to add.
    """

    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = Node()
        node = node.children[char]
    node.is_end_of_word = True

def generate_sequences(words):
    """Generates all possible sequences of the given words.

    Args:
        words: A list of words.

    Returns:
        A list of all possible sequences of the given words.
    """

    root = Node()
    for word in words:
        add_word(root, word)

    sequences = []

    def find_sequence(current_node, current_sequence, used_words):
        """Recursively finds all possible sequences of the given words, starting
        from the given node.

        Args:
            current_node: The current node in the tree.
            current_sequence: The current sequence of words.
            used_words: A set of words that have already been used in the
                sequence.
        """

        if len(used_words) == len(words):
            # We have found a complete sequence.
            sequences.append(current_sequence)

        for char, node in current_node.children.items():
            if char not in used_words:
                # We have not used the current character yet.
                new_used_words = used_words.copy()
                new_used_words.add(char)
                find_sequence(node, current_sequence + char, new_used_words)

    find_sequence(root, '', set())
    return sequences

word_list = ['CHEN', 'ENNA', 'NAI.']
result_sequences = generate_sequences(word_list)

for index, sequence in enumerate(result_sequences):
    print("Sequence", index + 1, ":", sequence)
