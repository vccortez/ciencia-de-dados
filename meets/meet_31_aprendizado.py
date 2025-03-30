from model import Meet, Resource

meet = Meet(
    title="Aprendizado de máquina",
    description="Definições; treinamento",
    module_number=3,
    topics=["Modelagem estatística", "Tipos de aprendizado", "Tarefas de modelagem"],
    resources=[
        Resource(title="Seção", value="[@carvalho:2024:cdfa, sec. 11.1]", kind="bib")
    ],
)
