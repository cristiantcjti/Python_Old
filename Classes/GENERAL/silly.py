import random
import words


def silly_string(nouns, verbs, templates):
    template = random.choice(templates)
    output = []
    index = 0

    while index < len(template):
        if template[index : index + 8] == '{{noun}}':
            output.append(random.choice(nouns))
            index += 8
        elif template[index : index + 8] == '{{verb}}':
            output.append(random.choice(verbs))
            index += 8
        else:
            output.append(template[index])
            index += 1
    return ' '.join(output)

if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))
