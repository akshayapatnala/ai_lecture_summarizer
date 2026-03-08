async function uploadFile(){

let fileInput = document.getElementById("audioFile")

let formData = new FormData()

formData.append("file", fileInput.files[0])

document.getElementById("transcript").innerText = "Processing..."
document.getElementById("summary").innerText = "Processing..."

let response = await fetch("http://127.0.0.1:8000/upload",{
method:"POST",
body:formData
})

let data = await response.json()

document.getElementById("transcript").innerText = data.transcript
document.getElementById("summary").innerText = data.summary

}