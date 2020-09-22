// div = document.createElement("div")
// p = document.createElement("p");
// p.style.color="red";
// p.textContent ="Hey am red!"
// document.body.appendChild(div)
// div.appendChild(p)
// heading = document.createElement("h3")
// heading.style.color = "blue"
// heading.textContent ="I am a blue h3"
// div.appendChild(heading)
// // divs =document.createElement("div")
// heads = document.createElement("h1");
// heads.style.color="blue"

// heads.textContent ="I am in a div"
// div.appendChild("heads")
// p2= document.createElement("p")
// p2.textContent = "Me too"
// div2.appendChild("p2")
// div.appendChild(div2)

//get reference to element node object
// var nodeAnchor = document.querySelector('a');

// //create props array to store property keys for element node object
// var props = [];

// //loop over element node object getting all properties & methods (inherited too)
// for(var key in nodeAnchor){
//     props.push(key);   
// }

// //log alphabetical list of properties & methods 
// console.log(props.sort());

// REPLACE ELEMENT

// // Create Element
// const newHeading = document.createElement('h2');
// // Add id
// newHeading.id = 'task-title';
// // New text node
// newHeading.appendChild(document.createTextNode('Task List'));

// // Get the old heading
// const oldHeading = document.getElementById('task-title');
// //Parent
// const cardAction = document.querySelector('.card-action');

// // Replace
// cardAction.replaceChild(newHeading, oldHeading);

// // REMOVE ELEMENT
// const lis = document.querySelectorAll('li');
// const list = document.querySelector('ul');

// // Remove list item
// lis[0].remove();

// // Remove child element
// list.removeChild(lis[3]);

// // CLASSES & ATTR
// const firstLi = document.querySelector('li:first-child');
// const link = firstLi.children[0];

// let val;

// // Classes
// val = link.className;
// val = link.classList;
// val = link.classList[0];
// link.classList.add('test');
// link.classList.remove('test');
// val = link;

// // Attributes
// val = link.getAttribute('href');
// val = link.setAttribute('href', 'http://google.com');
// link.setAttribute('title', 'Google');
// val = link.hasAttribute('title');
// link.removeAttribute('title');
// val = link;

// console.log(val);


// const newHeading = document.createElement('h2')

// newHeading.id = 'task-title';

// newHeading.appendChild(document.createTextNode('Task List'));

// const cardAction = document.querySelector('.card-action');
// const oldHeading = document.getElementById('task-title')

// cardAction.replaceChild(newHeading, oldHeading)

// // remove element

// const lis = document.querySelectorAll('li');
// const list = document.querySelector('ul')

// // remove list item

// lis[0].remove();

// list.removeChild(lis[3])

// // classes & attributes

// const firstLi = document.querySelector('li:first-child');

// console.log(firstLi.children[0])
// const link = firstLi.children[0]

// let val;

// val = link.className;
// val - link.classList.add('test')
// val = link.classList.remove('test')

// val = link.getAttribute('href')
// val = link.setAttribute('href', 'http://google.com')
// link.setAttribute('title', 'Google');
// val = link.hasAttribute('title')
//  link.removeAttribute('title')
//  val = link

// console.log(val)

// document.querySelector('.clear-tasks').addEventListener("click", function(e){
//     console.log('Hello World');

//     // e.preventDefault();
// // })
// document.querySelector('.clear-tasks').addEventListener("click", onClick)
// function onClick(e){
//     console.log('Hello World');

//     let val;
//     val = e
//     console.log(val)

//     val = e.target;
//     val = e.target.className;
//     val = e.target.classList;

//     e.target.innerText = 'Hello'

//     val = e.type;

//     val = e.timeStamp;
// // relative to the window
//     val = e.clientY;
//     val = e.clientX;
// // relative to element
//     val = e.offsetY;
//     val = e.offsetX;

//     e.preventDefault();
//     console.log(val)
// }

// const clearBtn = document.querySelector('.clear-tasks');
// const card = document.querySelector('.card');
// const heading = document.querySelector('h5');


// // clearBtn.addEventListener('click', runEvent)
// // clearBtn.addEventListener('mousemove', runEvent)
// // clearBtn.addEventListener('mouseover', runEvent)
// // clearBtn.addEventListener('mousedown', runEvent)
// card.addEventListener('mousemove', runEvent)


// // event handler
// function runEvent(e) {
//     console.log(`Event Type: ${e.type}`);

//     heading.textContent= `MouseX: ${e.offsetX} MouseY: ${e.offsetY}`

//     document.body.style.backgroundColor = `rgb(${e.offsetX}, ${e.offsetY}, 40 )`
//     e.preventDefault();
// }
// // // runEvent(e)

// const form = document.querySelector('form');
// const taskInput = document.querySelector("#task")
// const heading = document.querySelector('#task-title')

// taskInput.value = ''

// // form.addEventListener('keydown', runEvent);

// taskInput.addEventListener("keydown", runEvent)
// function runEvent(e){
//     console.log(`Event Type: ${e.type}`);

//     // console.log(taskInput.value);
    
//     console.log(e.target.value)
//     heading.innerText = e.target.value


//     // e.preventDefault()
// }

// eVENT bUBBLING
// document.querySelector(".card-title").addEventListener('click', function(){
//     console.log('card title');
// })
// document.querySelector(".card-content").addEventListener('click', function(){
//     console.log('card content');
// })
// document.querySelector(".card").addEventListener('click', function(){
//     console.log('card');
// })
// document.querySelector(".col").addEventListener('click', function(){
//     console.log('col');
// })

// Event delegation

// const delItem = document.querySelector(".delete-item");

// document.body.addEventListener('click', deleteItem);

// function deleteItem(e) {

// //     console.log(e.target)
// //     if (e.target.parentElement.className === 'delete-item secondary-content'){
// //     console.log('delete item');
// // }
// console.log(e.target)
//     if (e.target.parentElement.classList.contains('delete-item')){
//     console.log('delete item');
//     e.target.parentElement.parentElement.remove();
// }

// }


// // Add to local storage
// localStorage.setItem('name', 'John')
// localStorage.setItem('age', '30')

// add to session storage
// sessionStorage.setItem('name', 'Paulo')

// remove from storage
// localStorage.removeItem('name')

// get from storage
// const name = localStorage.getItem('name')
// const age = localStorage.getItem('age')
// console.log(name)
// console.log(age)

document.querySelector('form').addEventListener('submit',
function(e){
    const task = document.getElementById('task').value;

    let tasks;
    if (localStorage.getItem('tasks') === null){
        tasks = [];

    } else{
        tasks = JSON.parse(localStorage.getItem('tasks'));
    }

    tasks.push(task);

    localStorage.setItem('tasks', JSON.stringify(tasks))
    alert('Task saved')
    e.preventDefault()
});

const tasks = JSON.parse(localStorage.getItem('tasks'));


tasks.forEach(function(task){
    console.log(task);
  });