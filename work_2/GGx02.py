"""
GGx02.py

Модуль для проверки попадания в тройку победителей

Основные функции:
 - check_winners - проверяет, попадает ли студент в тройку победителей

 Автор: Иванов Владислав РИ-150911
 Версия: 1.0 (beta)
 Дата: 08.10.2025
"""


def check_winners(scores: list[int], student_score: int) -> None:
    """
    функция проверяет, попадает ли студент в тройку победителей
    :param scores: list[int]
    :param student_score: int
    :return: None -> print
    я мог использовать метод sorted, но решил не использовать его, так как думаю,
    что цель задачи - сделать алгоритм самому
    """

    for j in range(len(scores)):
        for i in range(len(scores)):
            if scores[j] > scores[i]:
                scores[i], scores[j] = scores[j], scores[i]
    print("Вы в тройке победителей!" if student_score in scores[:3] else "Вы не попали в тройку победителей.")


if __name__ == '__main__':
    test_scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]

    print(f"___start_test___: scores: {test_scores}")
    for number, student_score in enumerate(test_scores):
        print(number, student_score)

        print(f"test {number + 1}) | student_score: {student_score} -> ", end="")
        check_winners(test_scores, student_score)

