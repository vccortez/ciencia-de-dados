from model import Meet, Resource

meet = Meet(
    title="Abertura da disciplina",
    description="Apresentações; plano de ensino; ambiente de desenvolvimento; próximas aulas",
    has_content=False,
    date_span=2,
    resources=[
        Resource(title="Apresentação", value="slides/11_abertura.qmd", kind="file"),
    ],
)
