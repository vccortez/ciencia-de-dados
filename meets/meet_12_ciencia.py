from model import Meet, Resource

meet = Meet(
    title="Ciência de dados",
    description="Histórico; definições; KDD e CRISP-DM; Big Data; Data mining; processos de desenvolvimento",
    topics=[
        "Introdução à ciência de dados",
        "Áreas e termos relacionados",
        "Processos de desenvolvimento",
    ],
    resources=[
        Resource(title="Livro", value="[@carvalho:2024:cdfa, cap. 1--2]", kind="bib")
    ],
)
