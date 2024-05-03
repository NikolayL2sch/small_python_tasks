from functools import wraps
import datetime
import inspect


def logging_decorator(log_list):
    def decorator(func):
        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_arguments = signature.bind(*args, **kwargs)
            bound_arguments.apply_defaults()  # Применяем значения по умолчанию
            call_args = dict(bound_arguments.arguments)
            result = func(*args, **kwargs)
            log_list.append({
                'name': f'{func.__name__}',
                'arguments': call_args,
                'call_time': datetime.datetime.now(),
                'result': result
            })
            return result

        return wrapper

    return decorator


logger = []  # этот словарь будет хранить наш "лог"


@logging_decorator(logger)  # в аргументы фабрики декораторов подается логгер
def test_simple(a, b=2):
    return 127


test_simple(1)  # при вызове функции в список logger должен добавиться словарь с
# информацией о вызове функции
test_simple(1, 6)
print(logger)
