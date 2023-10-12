    /*var calendarDateInput = document.getElementById("date");

    calendarDateInput.addEventListener("change", function() {
      var selectedDate = calendarDateInput.value;
      if (selectedDate==date){
        const number = localStorage.setItem('number');
        const people = localStorage.setItem('people');
        const date = localStorage.setItem('date');
        const time = localStorage.setItem('time');
    
        // Get a reference to the table
        var table = document.getElementById("bookingTable");
    
        // Create a new row and cells
        var newRow = table.insertRow();
    
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        var cell3 = newRow.insertCell(2);
    
        // Add data to the cells
        cell1.innerHTML = time;
        cell2.innerHTML = number
        cell3.innerHTML = people;
      }
    });*/

    var myVar;
    
    function myFunction() {
      myVar = setTimeout(showPage, 3000);
    }
    
    function showPage() {
      document.getElementById("loader").style.display = "none";
      document.getElementById("myDiv").style.display = "block";
    }
    
    document.addEventListener("DOMContentLoaded", function() {
        // Get the date input element
        var dateInput = document.getElementById("date");
      
        // Add an event listener to detect changes in the date selection
        dateInput.addEventListener("change", function() {
          var selectedDate = dateInput.value;
          var tableBody = document.getElementById("table-body");
      
          // Clear the table body
          tableBody.innerHTML = "";
      
          // Check the selected date and populate the table accordingly
          if (selectedDate === "2023-06-20") {
            createTableRow(tableBody, "17:00", "87779239293", "5");
            createTableRow(tableBody, "20:00", "87474552225", "2");
            createTableRow(tableBody, "15:00", "87023477475", "1");
          } else if (selectedDate === "2023-06-25") {
            createTableRow(tableBody, "12:00", "87053005883", "9");
            createTableRow(tableBody, "10:00", "87771234567", "3");
          } else if (selectedDate === "2023-06-23") {
            createTableRow(tableBody, "16:00", "87058380005", "5");
          }
        });
      
        // Function to create a table row
        function createTableRow(tableBody, time, phoneNumber, numberOfPeople) {
          var row = document.createElement("tr");
          var timeCell = document.createElement("td");
          var phoneCell = document.createElement("td");
          var peopleCell = document.createElement("td");
      
          timeCell.textContent = time;
          phoneCell.textContent = phoneNumber;
          peopleCell.textContent = numberOfPeople;
      
          row.appendChild(timeCell);
          row.appendChild(phoneCell);
          row.appendChild(peopleCell);
      
          tableBody.appendChild(row);
        }
      });
      