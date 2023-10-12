document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    form.addEventListener('submit', function(e) {
      e.preventDefault();
  
      // Get the input values from the form
      var phoneNumber = document.getElementById('number').value;
      var numberOfPeople = document.getElementById('people').value;
      var selectedDate = document.getElementById('date').value;
      var selectedTime = document.getElementById('time').value;
  
      // Check if any field is empty
      if (!phoneNumber || !numberOfPeople || !selectedDate || !selectedTime) {
        alert('Барлық ақпаратты толтырыңыз!');
        return;
      }
  
      // Create a new object with the booking details
      var booking = {
        phoneNumber: phoneNumber,
        numberOfPeople: numberOfPeople,
        selectedDate: selectedDate,
        selectedTime: selectedTime
      };
  
      // Store the booking details in localStorage
      localStorage.setItem('booking', JSON.stringify(booking));
  
      // Display success message
      alert('Бронь қойылды!');
  
      // Clear the input fields
      document.getElementById('number').value = '';
      document.getElementById('people').value = '';
      document.getElementById('date').value = '';
      document.getElementById('time').value = '';
    });
  });