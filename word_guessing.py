from random import choice

from module_requests import date_request


def get_game_variables(
    level_difficulty: int, list_words: list[str]
) -> tuple[str, list[str], int]:
    random_word = choice(list_words)
    if level_difficulty == 0:
        remaining_attempts = 6
    else:
        remaining_attempts = 7
    list_unsolved_letters = ['_' for _ in range(len(random_word))]

    print('~' * 40)
    print('Загаданное слово: ', end='')
    print(*list_unsolved_letters)
    print(f'Попыток: {remaining_attempts}')

    return random_word, list_unsolved_letters, remaining_attempts


def start_game(
    random_word: str, list_unsolved_letters: list[str], remaining_attempts: int
) -> None:
    print()
    letter_or_word = input('Введите букву или слово: ').lower()

    if len(letter_or_word) == 1 and letter_or_word.isalpha():
        for ind, char in enumerate(random_word):
            if letter_or_word == char:
                list_unsolved_letters[ind] = letter_or_word

        temporary_string = ''.join(list_unsolved_letters)
        if temporary_string == random_word:
            print('Загаданное слово: ', end='')
            print(*list_unsolved_letters)
            print('Вы угадали!')
            print(f'Оставшееся количество попыток: {remaining_attempts}')
            return
        else:
            remaining_attempts -= 1
            if remaining_attempts == 0:
                print('Вы проиграли!')
                print(f'Загаданное слово: {random_word}')
                return
            else:
                print()
                print('Загаданное слово: ', end='')
                print(*list_unsolved_letters)
                print(f'Попыток осталось: {remaining_attempts}')
                start_game(
                    random_word, list_unsolved_letters, remaining_attempts
                )
    elif (
        len(letter_or_word) > 1
        and letter_or_word.isalpha()
        and letter_or_word == random_word
    ):
        print(f'Загаданное слово: {random_word}')
        print('Вы угадали!')
        print(f'Оставшееся количество попыток: {remaining_attempts}')
        return
    elif len(letter_or_word) > 1 and letter_or_word.isalpha():
        if len(letter_or_word) > len(random_word):
            print('Вы ввели слишком длинное слово :(')
            start_game(random_word, list_unsolved_letters, remaining_attempts)
        else:
            print('Вы не угадали слово :(')
            start_game(random_word, list_unsolved_letters, remaining_attempts)
    else:
        print('Вы ввели неверное значение!')
        start_game(random_word, list_unsolved_letters, remaining_attempts)


def main() -> None:
    start_game(*get_game_variables(*date_request()))


if __name__ == '__main__':
    main()
