from functions import get_only_executed_state, get_sort_by_date, print_trans
import json

if __name__ == "__main__":
    with open("operations.json") as file:
        operations_date = json.load(file)
        executed_date = get_only_executed_state(operations_date)
        sorted_by_date = get_sort_by_date(executed_date)
        sorted_by_date_last_5 = sorted_by_date[-5:]
        sorted_by_date_last_5 = list(reversed(sorted_by_date_last_5))
        for trans in sorted_by_date_last_5:
            print_trans(trans)