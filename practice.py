"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]

    """
    words_with_number_of_times_appear = {}

    for word in words:
        if word in words_with_number_of_times_appear:
            words_with_number_of_times_appear[word] += 1
        else:
            words_with_number_of_times_appear[word] = 1

    final_list_of_words = words_with_number_of_times_appear.keys()

    return final_list_of_words


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]

    """
    unique_items1 = set()
    unique_items2 = set()

    for item in items1:
        unique_items1.add(item)

    for item in items2:
        unique_items2.add(item)

    return list(unique_items1.intersection(unique_items2))

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    numbers = set(numbers)
    numbers = list(numbers)
    pairs_that_add_to_zero = []

    for i, item in enumerate(numbers):
        if numbers[i] == len(numbers):
            break

        if numbers[i] == 0:
            pairs_that_add_to_zero.append([0, 0]) 

        for j in range(i+1, len(numbers)):
            total_of_two_items = numbers[i] + numbers[j]
            if (total_of_two_items == 0):
                pairs_that_add_to_zero.append([numbers[i], numbers[j]])   

    return pairs_that_add_to_zero


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    list_string = phrase.split(" ")
    phrase_without_spaces = "".join(list_string)

    letters_count = {}
    letters_count_list = []

    for letter in phrase_without_spaces:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1

    for letter, count in letters_count.items():
        letters_count_list.append([letter, count])

    max_count = 0
    letters_with_highest_count = ['a']

    for letter_and_count in letters_count_list:
        if letter_and_count[1] > max_count:
            letters_with_highest_count[:] = letter_and_count[0]
            max_count = letter_and_count[1]
        elif letter_and_count[1] == max_count:
            letters_with_highest_count.append(letter_and_count[0])

    return sorted(letters_with_highest_count)


    



    



    return []

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
