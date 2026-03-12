let session_id
let current_question

async function startTest(){

document.getElementById("startBtn").style.display="none"

let res = await fetch("http://localhost:8000/start-session",{
method:"POST"
})

let data = await res.json()

session_id = data.session_id

getQuestion()

}

async function getQuestion(){

let res = await fetch(
`http://localhost:8000/next-question?session_id=${session_id}`
)

let data = await res.json()

if(data.test_complete){

    localStorage.setItem("ability_score", data.ability_score)
    localStorage.setItem("study_plan", data.study_plan)

    window.location.href = "result.html"

    return

}

current_question = data

document.getElementById("progress").innerText =
`Question ${data.q_no} / 10`

document.getElementById("question").innerText =
data.question

let options_html=""

data.options.forEach(opt=>{

options_html += `
<label class="option">
<input type="radio" name="opt" value="${opt}" onclick="enableSubmit()">
${opt}
</label>
`

})

document.getElementById("options").innerHTML = options_html

document.getElementById("submitBtn").disabled = true

document.getElementById("status").innerText=""

}

function enableSubmit(){

document.getElementById("submitBtn").disabled=false

}

async function submitAnswer(){

let selected = document.querySelector(
'input[name="opt"]:checked'
).value

let res = await fetch(
"http://localhost:8000/submit-answer",
{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
session_id:session_id,
question_id:current_question.question_id,
answer:selected
})
}
)

let data = await res.json()

if(data.correct){

document.getElementById("status").innerText="✅ Correct!"

}else{

document.getElementById("status").innerText="❌ Incorrect"

}

setTimeout(getQuestion,800)

}

function showResult(data){

document.getElementById("question").innerText="Test Completed"

document.getElementById("options").innerHTML=""

document.getElementById("submitBtn").style.display="none"

document.getElementById("progress").innerText=""

document.getElementById("result").innerHTML=`
Ability Score: ${data.ability_score.toFixed(2)}

Study Plan:
${data.study_plan}
`

}