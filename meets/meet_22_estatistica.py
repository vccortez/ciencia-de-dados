from model import Meet, Resource

meet = Meet(
    title="Estatística descritiva",
    description="Fundamentos; escalas de medida; medidas descritivas: tendência e dispersão; coeficiente de variação; NumPy",
    module_number=2,
    topics=["Escalas de medida", "Medições descritivas", "Biblioteca NumPy"],
    resources=[
        Resource(title="Capítulo", value="[@carvalho:2024:cdfa, cap. 5]", kind="bib")
    ],
)
