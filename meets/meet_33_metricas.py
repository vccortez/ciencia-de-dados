from model import Meet, Resource

meet = Meet(
    title="Avaliação de modelos",
    description="Métricas de resultados; hiperparâmetros; hipóteses; SciPy",
    module_number=3,
    topics=["Métricas avaliativas", "Teste de hipóteses", "SciPy"],
    resources=[
        Resource(title="Capítulo", value="[@carvalho:2024:cdfa, cap. 12]", kind="bib")
    ],
)
