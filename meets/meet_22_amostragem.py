from model import Meet, Resource

meet = Meet(
    title="Amostragem de dados",
    description="População; amostra; representatividade; variabilidade; inferência dedutiva e indutiva",
    module_number=2,
    topics=["População e amostra", "Representatividade", "Tipos de inferência"],
    resources=[
        Resource(title="Seção", value="[@carvalho:2024:cdfa, sec. 10.1]", kind="bib")
    ],
)
