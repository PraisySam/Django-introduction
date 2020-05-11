var body = document.getElementsByTagName('body')[0];

var dark = document.getElementById('dark-mode');
dark.addEventListener('click',function(){
     dark.classList.toggle('active');
     body.classList.toggle()

})









var request = new XMLHttpRequest()

request.open('GET','https://avatars0.githubusercontent.com/u/51412172?v=4', true)

request.onload = function(){
   
  var data = JSON.parse(this.response);
  console.log(data);
}

request.send();
