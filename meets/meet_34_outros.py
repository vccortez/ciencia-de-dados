from model import Meet, Resource

meet = Meet(
    title="Outros tópicos",
    description="Algoritmos bioinspirados; dados não estruturados; ética",
    module_number=3,
    topics=[
        "Algoritmos bioinspirados",
        "Hiperparâmetros",
        "Dados não estruturados",
        "Ética",
    ],
    resources=[
        Resource(
            title="Capítulos", value="[@carvalho:2024:cdfa, cap. 13--14]", kind="bib"
        )
    ],
)
