from model import Meet, Resource

meet = Meet(
    title="Ciência de dados",
    description="Histórico; definições; KDD e CRISP-DM; Big Data; Data mining; processos de desenvolvimento",
    topics=[
        "Introdução à ciência de dados",
        "Áreas e termos relacionados",
        "Processos de desenvolvimento",
    ],
    date_span=2,
    resources=[
        Resource(
            title="Capítulos", value="[@carvalho:2024:cdfa, cap. 1--2]", kind="bib"
        ),
        Resource(title="Definição", value="resenhas/12_definicao.qmd", kind="file"),
        Resource(
            title="Relacionados",
            value="resenhas/12_relacionados.qmd",
            kind="file",
        ),
        Resource(title="Processos", value="resenhas/12_processos.qmd", kind="file"),
    ],
)
