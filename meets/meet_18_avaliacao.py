from textwrap import dedent
from model import Meet, Resource

meet = Meet(
    title="Primeira avaliação",
    description="Apresentações de bases de dados",
    has_content=False,
    is_exam=True,
    is_closing=True,
    date_span=2,
    resources=[
        Resource(
            title="Detalhes",
            value=dedent(
                """
                Trabalho em grupo.
                Cada grupo deve gerar e apresentar uma base de dados inédita.

                Critérios de avaliação:

                - Volume e variedade
                - Procedimentos de coleta
                - Conhecimento esperado
                - Criatividade
                - Organização e compartilhamento
                """
            ),
        )
    ],
)
