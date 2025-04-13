from model import Meet, Resource

meet = Meet(
    title="Qualidade de dados",
    description="Ausências; ruídos; outliers; limpeza",
    module_number=2,
    topics=[
        "Dados faltantes",
        "Dados ruidosos",
        "Pontos fora da curva",
        "Dados enviesados",
        "Limpeza de dados",
    ],
    resources=[
        Resource(title="Capítulo", value="[@carvalho:2024:cdfa, cap. 7]", kind="bib")
    ],
)
