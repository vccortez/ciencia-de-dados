from model import Meet, Resource

meet = Meet(
    title="Visualização de dados",
    description="Gráficos; Matplotlib; Seaborn; análise exploratória de dados (EAD)",
    module_number=2,
    topics=[
        "Análise exploratória de dados",
        "Gráficos estatísticos",
        "Biblioteca Matplotlib",
        "Biblioteca Seaborn",
    ],
    resources=[
        Resource(title="Capítulo", value="[@carvalho:2024:cdfa, cap. 6]", kind="bib")
    ],
)
