from model import Meet, Resource

meet = Meet(
    title="Fundamentos de Python",
    description="Revisão da linguagem; entrada e saída; ambientes virtuais; interoperabilidade",
    topics=["Linguagem Python", "Ambientes virtuais"],
    resources=[
        Resource(title="Capítulo", value="[@carvalho:2024:cdfa, cap. 3]", kind="bib"),
        Resource(title="Capítulo", value="[@grus:2015:data, cap. 2]", kind="bib"),
        Resource(title="Ferramentas", value="resenhas/13_ferramentas.qmd", kind="file"),
    ],
)
