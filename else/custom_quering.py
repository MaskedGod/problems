from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc, *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    data = selector(data)

    for filter_func in filters:
        data = filter_func(data)

    return data


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""

    def selector(data: DataType) -> DataType:
        """Takes a dataset (an iterable of dictionaries) as input and returns
        a new list of dictionaries where each dictionary contains only the specified columns.

        :param data: List of dictionaries with columns and values
        :return: data with selected columns
        """
        selected_rows = []

        for row in data:
            selected = {col: row.get(col, None) for col in columns}
            selected_rows.append(selected)

        return selected_rows

    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    def filter(data: DataType) -> DataType:
        """Takes a dataset and returns a new list where each dictionary contains only the specified columns.

        :param data: List of dictionaries with columns and values
        :return: data with filtered values
        """
        return [row for row in data if row.get(column, None) in values]

    return filter


def test_query():
    friends = [
        {"name": "Sam", "gender": "male", "sport": "Basketball"},
        {"name": "Emily", "gender": "female", "sport": "Volleyball"},
    ]
    value = query(
        friends,
        select(*("name", "gender", "sport")),
        field_filter(*("sport", *("Basketball", "Volleyball"))),
        field_filter(*("gender", *("male",))),
    )
    print(value)
    assert [{"gender": "male", "name": "Sam", "sport": "Basketball"}] == value


if __name__ == "__main__":
    test_query()
