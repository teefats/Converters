
const search =  document.querySelector(".search")
const term = search.value;

  // Check for empty
  if (term.trim()) {
    fetch(`https://www.dnd5eapi.co/api/spells/acid-arrow`)
      .then(res => res.json())
      .then(data => {
        console.log(data);
      })}
