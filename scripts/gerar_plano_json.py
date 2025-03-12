if __name__ == "__main__":
    import os, sys

    sys.path.insert(1, os.path.join(sys.path[0], ".."))

from model import Plan
from aulas import meets
from scripts import agendador

dates = agendador.load_dates("dados/datas.csv")

# atribuindo cada aula a uma data
meets_with_dates = agendador.assign_meet_dates(meets, dates)

plan = Plan(meets=meets)
json_str = plan.model_dump_json(indent=2, by_alias=True)
print(json_str)
