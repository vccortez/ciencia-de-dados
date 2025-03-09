function fillTableWithSubjects(tableSelector, subjectSchedule) {
  // Get the table element by ID
  const table = document.querySelector(tableSelector);
  if (!table) {
    console.error("Table not found");
    return;
  }

  // Extract rows from the tbody of the table
  const rows = Array.from(table.querySelectorAll("tbody tr"));

  // Helper function to convert dd/MM/yyyy to yyyy-MM-dd
  function convertDateFormat(dateStr) {
    const [day, month, year] = dateStr.split("/").map(Number);
    return `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
  }

  // Create a mapping of date -> subject name(s)
  const dateToSubjectMap = {};
  subjectSchedule.forEach(subject => {
    subject.dates.forEach(date => {
      dateToSubjectMap[date] = subject.subject;
    });
  });

  // Iterate over each row and fill the input with the corresponding subject name
  let lastSubjectName = null
  for (row of rows) {
    const cells = row.querySelectorAll("td");
    if (cells.length >= 4) {
      const dateCell = cells[0]; // Date is in the first cell
      const imgCell = cells[2];
      const inputCell = cells[3]; // Input element is in the fourth cell
      const inputElement = inputCell.querySelector("input");
      const imgElement = imgCell.querySelector('img')

      if (dateCell && inputElement) {
        const date = convertDateFormat(dateCell.innerText.trim());
        let newSubjectName = dateToSubjectMap[date]
        if (newSubjectName == null) continue
        if (newSubjectName != lastSubjectName) {
          inputElement.value = dateToSubjectMap[date];
        } else {
          imgElement.click()
        }
        lastSubjectName = newSubjectName
      }
    }
  }

  console.log("Table inputs filled with subject names.");
}

// Example usage:
// Assuming `subjectSchedule` is the JSON object from the Subject Syllabus Scheduler
// fillTableWithSubjects("sessionsTable", subjectSchedule);
