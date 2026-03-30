async function predict(){

let data = {

battery_power: document.getElementById("battery_power").value,
ram: document.getElementById("ram").value,
px_height: document.getElementById("px_height").value,
px_width: document.getElementById("px_width").value,
mobile_wt: document.getElementById("mobile_wt").value,
int_memory: document.getElementById("int_memory").value,
pc: document.getElementById("pc").value,
fc: document.getElementById("fc").value,
clock_speed: document.getElementById("clock_speed").value,
sc_h: document.getElementById("sc_h").value,
sc_w: document.getElementById("sc_w").value

}

let response = await fetch("/predict",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)

})

let result = await response.json()

document.getElementById("result").innerText =
"Predicted Price Range: " + result.prediction

}