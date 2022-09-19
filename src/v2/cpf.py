BASE_FIRST_DIGIT = 11
BASE_SECOND_DIGIT = 12
BASE_ZERO_DIGIT = 2
BASE_CALCULATE_SECOND_DIGIT = 2
CPF_LENGHT = 11
DIGIT_ZERO = 0
MIN_CPF_LENGHT = 11
MAX_CPF_LENGHT = 14
UNIQUE_CARACTER = 1


def _is_valid_cpf_digits(cpf: str) -> bool:
    validation = len(cpf) >= MIN_CPF_LENGHT and len(cpf) <= MAX_CPF_LENGHT
    return validation


def _remove_cpf_special_caracters(cpf: str) -> str:
    return (
        cpf.replace('.', '').replace('.', '').replace('-', '').replace(' ', '')
    )


def _calculate_cpf_solution(cpf: str) -> str:
    solution_first_digit = solution_second_digit = 0
    for cpf_index in range(1, (len(cpf) - 1)):
        digit_index = int(cpf[cpf_index - 1 : cpf_index])
        solution_first_digit += (BASE_FIRST_DIGIT - cpf_index) * digit_index
        solution_second_digit += (BASE_SECOND_DIGIT - cpf_index) * digit_index

    rest_number_checker = solution_first_digit % CPF_LENGHT
    first_digit = (
        DIGIT_ZERO
        if rest_number_checker < BASE_ZERO_DIGIT
        else CPF_LENGHT - rest_number_checker
    )

    solution_second_digit += BASE_CALCULATE_SECOND_DIGIT * first_digit
    rest_number_checker = solution_second_digit % CPF_LENGHT
    second_digit = (
        DIGIT_ZERO
        if rest_number_checker < BASE_ZERO_DIGIT
        else CPF_LENGHT - rest_number_checker
    )
    return f'{first_digit}{second_digit}'


def validate_cpf(cpf: str) -> bool:
    if cpf is None or cpf == '':
        raise Exception('CPF is None or Empty')
    if not _is_valid_cpf_digits(cpf):
        raise Exception('CPF incomplete digits')
    cpf = _remove_cpf_special_caracters(cpf)
    if len(set(cpf)) == UNIQUE_CARACTER:
        raise Exception('CPF is the same caractere in all digits')
    try:
        digit_number_checker = cpf[len(cpf) - 2 : len(cpf)]
        digit_number_checker_solution = _calculate_cpf_solution(cpf)
        return digit_number_checker == digit_number_checker_solution
    except Exception as err:
        raise err
