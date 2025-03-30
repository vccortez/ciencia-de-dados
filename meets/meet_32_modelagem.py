from model import Meet, Resource

meet = Meet(
    title="Modelagem de dados",
    description="Regressão linear; classificação; agrupamento; algoritmos; SciKit Learn",
    module_number=3,
    topics=["Regressão linear", "Classificação", "Agrupamento", "SciKit Learn"],
    resources=[
        Resource(title="Capítulo", value="[@carvalho:2024:cdfa, cap. 11]", kind="bib")
    ],
)
