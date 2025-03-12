/**
 * preenche tabela do SIGAA a partir de JSON de aulas da disciplina
 * @param {string} selector seletor da tabela
 * @param {object} plan plano de aulas
 */
function fill_table(selector, plan) {
  let table = document.querySelector(selector)
  if (!table) {
    console.error("table not found")
    return
  }

  let rows = Array.from(table.querySelectorAll("tbody tr"))

  /**
   * converte de dd/MM/yyyy para yyyy-MM-dd
   * @param {string} date_string 
   * @returns string
   */
  function convert_date(date_string) {
    let [day, month, year] = date_string.split("/").map(Number)
    return `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`
  }

  // mapping of date -> meet title
  let date_map = {}
  for (let meet of plan.meets) {
    for (let date of meet.dates) {
      date_map[date] = meet.title
    }
  }

  let last_topic_name = null
  for (row of rows) {
    let cells = row.querySelectorAll("td")
    if (cells.length >= 4) {
      let date_cell = cells[0] // date is in the first cell
      let btn_cell = cells[2]
      let input_cell = cells[3] // input element is in the fourth cell

      let input = input_cell.querySelector("input")
      let btn = btn_cell.querySelector("img")

      if (date_cell && input) {
        let date = convert_date(date_cell.innerText.trim())
        let topic_name = date_map[date]
        if (topic_name == null) continue
        if (topic_name != last_topic_name) {
          input.click() // sigaa requires focus
          input.value = date_map[date]
        } else {
          btn.click()
        }
        last_topic_name = topic_name
      }
    }
  }

  console.log("table inputs filled with subject names.")
}

