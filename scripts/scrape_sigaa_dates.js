function scrapeTableToCSV(tableSelector) {
  // Get the table element by ID
  const table = document.querySelector(tableSelector);
  if (!table) {
    console.error("Table not found");
    return;
  }

  // Extract rows from the tbody of the table
  const rows = table.querySelectorAll("tbody tr");

  // Initialize an array for CSV data
  const csvData = [];
  csvData.push("date,canceled"); // Add header row

  // Iterate over each row and extract the date
  rows.forEach(row => {
    const cells = row.querySelectorAll("td");
    if (cells.length >= 4) {
      const date = cells[0].innerText.trim(); // Date is in the first cell
      csvData.push(`${date},false`); // Assume no session is canceled
    }
  });

  // Convert the array to a CSV string
  const csvContent = csvData.join("\n");

  // Trigger a download of the CSV file
  const blob = new Blob([csvContent], { type: "text/csv" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "sessions.csv";
  a.click();

  // Clean up the URL object
  URL.revokeObjectURL(url);
}

// Example usage: Call this function and pass the table's ID
// scrapeTableToCSV("sessionsTable");
