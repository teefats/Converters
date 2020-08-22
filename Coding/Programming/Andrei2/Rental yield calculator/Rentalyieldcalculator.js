// Listen for submit
document.getElementById('yield-form').addEventListener('submit', function(e){
  // Hide results
  document.getElementById('results').style.display = 'none';
  
  // // Show loader
  document.getElementById('loading').style.display = 'none';

  setTimeout(calculateResults, 200);

  e.preventDefault();
});

// Calculate Results
function calculateResults(){
  console.log('Calculating...');
  // UI Vars
  const monthlyRent = document.getElementById('monthly-rent');
  const propValue = document.getElementById('property-value');
  const rentalYield = document.getElementById('rental-yield');
  
  //declare variable values
  const yearlyRental = parseFloat(monthlyRent.value) * 12;
  const yield = parseFloat((yearlyRental / propValue.value)*100) ;
  
  const percentageYield = parseFloat(yield)  ;
  
  // Compute monthly payment
 

  if(isFinite(yield)) {
   console.log("word");
   rentalYield.value = percentageYield.toFixed(2);

   if(yield > 8){
     console.log("great");
     document.getElementById('rental-yield').style.backgroundColor = 'green';
     document.getElementById('rental-yield').style.color = 'white';
   }else{
     console.log("Not so much");
     document.getElementById('rental-yield').style.backgroundColor = 'tomato';
     document.getElementById('rental-yield').style.color = 'white';

   }

   
    // Show results
    document.getElementById('results').style.display = 'block';

    // Hide loader
    document.getElementById('loading').style.display = 'none';
    
   

  } else {
    
    showError('Please check your numbers');
    
    
  }
}

// Show Error
function showError(error){
  // Hide results
  document.getElementById('results').style.display = 'none';
  
  // Hide loader
  document.getElementById('loading').style.display = 'none';

  // Create a div
  const errorDiv = document.createElement('div');

  // Get elements
  const card = document.querySelector('.card');
  const heading = document.querySelector('.heading');

  // Add class
  errorDiv.className = 'alert alert-danger';

  // Create text node and append to div
  errorDiv.appendChild(document.createTextNode(error));

  // Insert error above heading
  card.insertBefore(errorDiv, heading);

  // Clear error after 3 seconds
  setTimeout(clearError, 3000);
}

// Clear error
function clearError(){
  document.querySelector('.alert').remove();
}