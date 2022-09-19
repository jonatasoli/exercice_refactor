def _is_valid_cpf_digits(cpf) -> bool:
    validation = len(cpf) >= 11 and len(cpf) <= 14
    return validation


def _remove_cpf_special_caracters(cpf) -> str:
    return (
        cpf.replace('.', '').replace('.', '').replace('-', '').replace(' ', '')
    )


def _calculate_cpf_solution(cpf) -> str:
    solution_first_digit = solution_second_digit = 0
    first_digit = second_digit = rest_number_checker = 0
    digit_index = None
    for cpf_index in range(1, (len(cpf) - 1)):
        digit_index = int(cpf[cpf_index - 1 : cpf_index])
        solution_first_digit = (
            solution_first_digit + (11 - cpf_index) * digit_index
        )
        solution_second_digit = (
            solution_second_digit + (12 - cpf_index) * digit_index
        )
    rest_number_checker = solution_first_digit % 11
    first_digit = first_digit = (
        0 if rest_number_checker < 2 else 11 - rest_number_checker
    )
    solution_second_digit += 2 * first_digit
    rest_number_checker = solution_second_digit % 11
    if rest_number_checker < 2:
        second_digit = 0
    else:
        second_digit = 11 - rest_number_checker
    return f'{first_digit}{second_digit}'


def validate_cpf(cpf) -> bool:
    if cpf is None:
        return False
    if not _is_valid_cpf_digits(cpf):
        return False
    cpf = _remove_cpf_special_caracters(cpf)
    if not len(set(cpf)) == 1:
        try:
            digit_number_checker = cpf[len(cpf) - 2 : len(cpf)]
            digit_number_checker_solution = _calculate_cpf_solution(cpf)
            return digit_number_checker == digit_number_checker_solution
        except Exception as e:
            print('Erro !' + str(e))

            return False

    else:
        return False
