from model import Meet, Resource

meet = Meet(
    title="Descoberta de dados",
    description="Seleção; web crawling ou scraping; Requests; BeautifulSoup",
    topics=["Seleção de dados", "Web scraping", "Biblioteca BeautifulSoup"],
    resources=[
        Resource(
            title="Seções",
            value="[@carvalho:2024:cdfa, sec. 13.2.1, 13.3.1]",
            kind="bib",
        )
    ],
)
