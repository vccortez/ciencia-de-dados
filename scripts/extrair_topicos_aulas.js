function extrair_topicos_aulas() {
  let table = document.querySelector('table.listing')

  let rows = table.querySelectorAll('tbody tr')

  let rows_list = Array.from(rows)

  let result = []

  for (let row of rows_list) {
    let topic = {}

    if (row.children[3].children[0].value.trim() == '') continue

    topic['start'] = row.children[0].innerHTML.trim()
    topic['end'] = row.children[1].innerHTML.trim()
    topic['description'] = row.children[3].children[0].value.trim()

    result.push(topic)
  }

  console.log(result)
}
