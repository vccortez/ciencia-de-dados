from model import Meet, Resource

meet = Meet(
    title="Manipulação de dados",
    description="Dados tabulares; Pandas; DataFrames",
    topics=["Dados tabulares", "Biblioteca Pandas", "Planilhas e DataFrame"],
    resources=[
        Resource(title="Capítulo", value="[@carvalho:2024:cdfa, cap. 4]", kind="bib"),
        Resource(
            title="Capítulo", value="[@vanderplas:2016:python, cap. 3]", kind="bib"
        ),
        Resource(title="Capítulo", value="[@verri:2024:dsp, cap. 5]", kind="bib"),
    ],
)
