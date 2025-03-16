from model import Meet, Resource

meet = Meet(
    title="Fundamentos de Python",
    description="Revisão da linguagem; entrada e saída; ambientes virtuais; interoperabilidade",
    topics=["Linguagem Python", "Ambientes virtuais"],
    resources=[
        Resource(title="Livro", value="[@carvalho:2024:cdfa, cap. 3]", kind="bib")
    ],
)
