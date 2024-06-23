from libwords import list_levels_difficulty, list_topics, list_words_levels


def date_request(selected_topic=None) -> list[str]:
    if selected_topic is None:
        for index_topic, topic in enumerate(list_topics):
            print(f"{index_topic} - {topic.capitalize()}")
        print()

        try:
            user_topic = input("Выберите одну из тематик: ").strip()
            # Сделано для того, чтобы при вводе пользователем 01, 02..., вызывалась ошибка
            if len(user_topic) == 1:
                user_topic = int(user_topic)
            else:
                raise ValueError
            if user_topic not in range(len(list_topics)):
                raise ValueError
            selected_topic = user_topic
        except ValueError:
            print("Вы ввели неверное значение!")
            print("~" * 40)
            return date_request()

    print("~" * 40)
    for index_level, level in enumerate(list_levels_difficulty):
        print(f"{index_level} - {level.capitalize()}")
    print()

    try:
        user_level_difficulty = input(
            "Выберите уровень сложности слов: "
        ).strip()
        # Сделано для того, чтобы при вводе пользователем 01, 02..., вызывалась ошибка
        if len(user_level_difficulty) == 1:
            user_level_difficulty = int(user_level_difficulty)
        else:
            raise ValueError
        if user_level_difficulty not in range(len(list_levels_difficulty)):
            raise ValueError
        else:
            print("~" * 40)
            print(f"Тематика - {list_topics[selected_topic].capitalize()}")
            print(
                f"Уровень сложности - {list_levels_difficulty[user_level_difficulty].capitalize()}"
            )
            return (
                user_level_difficulty,
                list_words_levels[user_level_difficulty][selected_topic],
            )
    except ValueError:
        print("Вы ввели неверное значение!")
        return date_request(selected_topic)
