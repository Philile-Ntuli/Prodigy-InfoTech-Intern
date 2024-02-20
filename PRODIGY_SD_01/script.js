let celsius = document.getElementById("celsius");
let fahrenheit = document.getElementById("fahrenheit");
let kelvin = document.getElementById("kelvin");

celsius.oninput = function(){
 fahrenheit.value = (parseFloat(celsius.value)*9/5 + 32).toFixed(2);
 kelvin.value = (parseFloat(celsius.value)+ 273.15).toFixed(2);
};

fahrenheit.oninput = function(){
  celsius.value = (parseFloat(fahrenheit.value) - 32) * 5/9;
  kelvin.value = (parseFloat(fahrenheit.value)- 32)* 5/9 + 273.15;
};

kelvin.oninput = function(){
  celsius.value = parseFloat(kelvin.value)- 273.15;
  fahrenheit.value = (parseFloat(kelvin.value)- 273.15)* 9/5 + 32;
};
