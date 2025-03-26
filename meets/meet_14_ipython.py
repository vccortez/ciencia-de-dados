from model import Meet, Resource

meet = Meet(
    title="Python em computação científica",
    description="Fundamentos; IPython; Jupyter notebooks",
    topics=["Ambiente de desenvolvimento", "IPython", "Jupyter Notebooks"],
    resources=[
        Resource(
            title="Capítulo", value="[@vanderplas:2016:python, cap. 1]", kind="bib"
        )
    ],
)
