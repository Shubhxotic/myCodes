/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function PurpleClick()
{
    document.getElementById("ColorDiv").style.backgroundColor="purple";
}

function RedClick()
{
    document.getElementById("ColorDiv").style.backgroundColor="red";
}

function BlueClick()
{
    document.getElementById("ColorDiv").style.backgroundColor="blue";
}


function YellowClick()
{
    document.getElementById("ColorDiv").style.backgroundColor="yellow";
}

function changeColor(color)
{
    document.getElementById("ColorDiv").style.backgroundColor=color;
}
function changeColorEvent(event)
{
    var x=event.srcElement;
    alert("clicked me");
    document.getElementById("ColorDiv").style.backgroundColor=x.innerHTML.toLowerCase();
}
