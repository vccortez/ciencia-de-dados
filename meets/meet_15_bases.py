from model import Meet, Resource

meet = Meet(
    title="Bases de dados",
    description="Tipos de dados; formatos e arquivos; armazenamento; bancos de dados; dados tabulares",
    topics=["Tipos de dados", "Fontes de dados", "Estrutura de dados"],
    resources=[
        Resource(
            title="Seções", value="[@carvalho:2024:cdfa, sec. 1.2--1.3]", kind="bib"
        ),
        Resource(title="Capítulo", value="[@verri:2024:dsp, cap. 4]", kind="bib"),
    ],
)
